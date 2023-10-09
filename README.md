# Voting system | CS50W - Capstone 
<br>

# Overview 
This project contains a Django Rest API with a (Html , css , js ) frontend , my prject name called "voting system"
There is no option to create a new account, only to log in. Public and audience users can use this website without logging in. As for the judge users, they are provided 
with special accounts by the admin for the purpose of logging in. <br>
The admin can add new competitions, and any user can vote for the teams within the competitions. If the vote is done by a judge, 10 points will be counted for the team, and if the vote is done by the audience, one point will be counted and
everyone can see the results and points for each team.

<br>

# Justification
I consider that this project meets all the expectations raised in the assignment of the CS50W final project, as it is a web platform that implements most of the concepts and techniques taught in the course.
<br> <br>
The whole application is based on the Django framework, which allowed managing user authentication, database models, http requests, static files and the page rendering.
<br> <br>
The web application is mobile responsive. I have included tailwind library to make the most of my frontend style. <br> <br> 

The difference between this web application and previous projects: <br>
For frontend, this project was distinguished from the other projects in the course by using tailwind Framework <br><br>
and for backend, this project was distinguished by preventing the user from voting for the same competition “for a certain period.” 
This is what we did not see in the rest of the projects in the course, as we see it was possible for any person buys any item more than once( in E-commerce )... sends an email more than once( in Mail )...
or writes a post more than once(in network)...etc. <br><br>
The project is also distinguished by the difference in reaction to the user’s action if he has logged in (which means he is a judge and ten points are counted)
or if he did not log in (which means he is an audience and one point is counted).... <br><br>
The voting process in this project also distinguished it from other projects in that in every voting process there is an update to the value of the team’s points in the database
(since the team and its points remain stored In Database, these points are updated for each voting process. <br>
Also, in the process of displaying the results, we had to resort to and use 3 models together, where first all competitions are called from the "competitions model"
(in order to display the results of all competitions) and then call All teams from the "Teams Model"
(in order to display all teams for each competition) and then the points for each team are withdrawn from the "vote Model" (to display the points for each team) 
and then all this information is injected into a specific array to send it to the results page...
where in Previous projects did not reach this level of complexity to use this number of models together to inject specific information into a page. <br> <br>

- [x] Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.
- [x] Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
- [x] Your web application must be mobile-responsive.

<br>

# Structre 
- <b>voting_system</b>: this folder is the project of Django
- <b>competition</b>: this folder is the app of Django project which contain the frontend and backend

<br> <br> 

# File contents 
### Frontend:
- ./competition/templates : this handels all html pages of website
- ./competition/static : this handles all stylesheets of the website and also contain a images folder that handle the images that used in the website

<br>

### Backend:
<h3>models in the app</h3>
There are 4 models for the web application's database.
<br>
1. User - A fully featured User model <br>
2. competition - Holds the information of competition <br>
3. Team - Holds the information of teams for each competition <br>
4. Vote - Holds the points of votes for each team <br>

<br>

#### Views and serializers py files:
'views.py' contains the funtions for the web application. These view functions sends and receives http request and response. <br>

### Manage.py file:
This file is used as a command-line utility and for deploying, debugging, or running the web application.This file contains code for runserver, makemigrations or migrations, etc. that we use in the shell. (Not changing anything here) <br>

### init.py files:
This file is empty and remains that way. they are present only to tell that this particular directory is a package. (No changes to this file either) <br>

### settings folder:
This file is present for adding all thr applications and the middleware application present. This also has informations about templates and databases. This is present in the main file of the Django web application.<br>

### urls.py files:
This file handles all the URLs of our Django web application. This file contains the lists of all the endpoints that we will have for our web application. Also, this files is like a link to the views in the app with the host web URL. <br>

### wsgi folder:
This file mainly concerns with the WSGI server and is used for deploying the web application on to the servers similar to apache, etc. (No changes to this file as well) <br>

### admin.py files:
Similar to the name of the file, this file is used for registering the models into the django administration. The models that are present have a superuser/admin who can control the information that is being stored. (they are pre-built) <br>

### apps.py files:
This file deals with the application configuration of the apps. The default configuration is sufficient enough in most of the cases. <br>

### models.py files:
This file contains the models of our web application (classes). They are the blueprints of the database we are using and hence contain the information regarding attributes and the fields, etc of the database. <br>

### views.py files:
This files are the crucial ones, it contains all the views. This file can be considered as the file that interacts with the client.  <br>

### test.py files:
This file containts the code that contains different test cases for the application. It is used to test the working of the application. (did not implement tests in this web application) <br>


# Installation & how to run the application
Run the application in their default ports (Django: 8000) <br>
<h3>Backend:</h3>

```
python manage.py makemigrations 
python manage.py migrate 
python manage.py runserver
```



