from django.shortcuts import render , redirect 
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse , HttpResponseRedirect 
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *

def index(request):
    competitions = Competition.objects.all()
    return render(request , "index.html" , { 'competitions' : competitions })



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index")) 
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('index')



def vote(request, id):
    competition = Competition.objects.get(pk=id)
    teams = Team.objects.filter(competition=competition)
    user = request.user

    
    if request.method == 'POST':
        if 'voted_for_competition_{}'.format(id) in request.session:
            return redirect('index')
        team_id = request.POST.get('team_id')  # Assuming you have an input field with name 'team_id' in your form
        team = Team.objects.get(pk=team_id)

        if user.is_authenticated:
            points = 10
        else:
            points = 1

        # Check if the user has already voted for this team
        existing_vote = Vote.objects.filter(team=team).first()

        if existing_vote:
            existing_vote.points += points
            existing_vote.save()
        else:
            vote = Vote.objects.create(team=team, points=points)

        request.session['voted_for_competition_{}'.format(id)] = True
        return redirect('index')

    return render(request, 'vote_page.html', {'competition': competition, 'teams': teams})


from django.db.models import Sum
def result(request):
    competitions = Competition.objects.all()
    results = []

    for competition in competitions:
        teams = Team.objects.filter(competition=competition)
        team_results = []

        for team in teams:
            points = Vote.objects.filter(team=team).aggregate(Sum('points'))['points__sum'] or 0
            team_results.append({'team': team, 'points': points})

        results.append({'competition': competition, 'team_results': team_results})

    return render(request, 'results.html', {'results': results})


    




