from django.db import models
from django.contrib.auth.models import AbstractUser , User



class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



class Competition(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vote(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

