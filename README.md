# Unlimited Bacon
pws link: 

## Assignment 2 

### 1. Steps: 
1. Make a new local directory named ```unlimited_bacon```
2. Initialized as well configuring ```git``` in the repository
3. Create a new repository in GitHub with the same name
4. Connecting local repository with the GitHub repository by:
   - Setting a new branch named ```main``` using:

    ```bash
    git branch -M main
    ```
   - Connecting the local repository to GitHub using:

    ```bash
    git remote add origin https://github.com/GhazaFadhlilbaqi/unlimited_bacon.git 
    ```
5. In the local directory, set up a virtual environment by running:

    ```bash
    python -m venv env
    ```
   And activating it by:

    ```bash
    env\Scripts\activate
    ```
6. Set up requirements in the same local directory by:
   - Creating a new directory called ```requirements.txt``` with the contents being: 

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
   - Running the command to enable the requirements

   ```bash
   pip install -r requirements.txt
   ```
7. Create a new Django project by running:
    ```bash
    django-admin startproject unlimited_bacon .
    ```
8. Add the following to ```ALLOWED_HOST``` to allow access to local host:
    
    ```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ```
9. Create the ```main``` app inside the main directory by:
    - Running the following command

    ```bash
    python manage.py startapp main
    ```
    - And adding ```main``` to the ```INSTALLED_APPS``` in ```settings.py```

    ```
    INSTALLED_APPS = [
    'main'
    ]
    ```
10. Create a new directory in ```main``` named ```templates``` with a ```html``` file named ```main.html``` with the contents:

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>UnlimitedBacon</title>
    </head>
    <body>
        <h1>
            {{ app_name }}
        </h1>

        <p>
            {{ name }}
        </p>
        <p>
            {{ class }}
        </p>
    </body>
    </html>
    ```
11. Adding new models by modifying ```models.py``` by:
    - Adding the following to the file:

    ```python
    from django.db import models

    class UnlimitedBacon(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    stock = models.IntegerField()
    ```
    - Execute the two commands to migrate any changes made to the ```model.py``` file:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
12. Integrating the ```views.py``` file with the ```main.html``` file:
    
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app_name': 'Unlimited Bacon',
            'name': 'Muhammad Ghaza Fadhlilbaqi',
            'class': 'KKI'
        }

        return render(request, 'main.html', context)
    ```
13. Route the ```main``` application to the ```urls.py``` file by:
    - Adding the following to ```urls.py``` in the ```main``` directory

    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
    - Add a URL route in the ```urls.py``` file in the ```unlimited_bacon``` directory by:
    
    ```python
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
14. Test the app by:
    - Running the application by running the command:
    
    ```bash
    python manage.py runserver
    ```
    - Then opening ```http://localhost:8000/``` in a browser

### 2. Diagram:
![](static/images/diagram.png)
According to the diagram above, when a user makes a request, the ```urls.py``` file routes requests to views in the ```views.py``` file, which process the request and interact with ```models.py``` for data. The view then uses the ```main.html``` template to format the response, which is sent back to the user’s browser.

### 3. Use of ```git```
```Git``` is a very important software used in software development for several different reasons:
- Version control: ```git``` allows devs to track any changes made to the code and even revert back to previous versions 
- Collaboration: ```git``` allows multiple developers to work on the same project simultaneously using **branches**. Each developer can work on their own branch without affecting the main codebase. Git also supports **pull requests**, enabling team members to review and discuss changes before merging them into the main project.

### 4. Reason to use Django
Django is often chosen as a starting point for learning software development because it offers a comprehensive framework that simplifies the development process with several built-in features. Its thorough, beginner-friendly documentation and use of the Model-View-Template (MVT) pattern help beginners grasp essential web development concepts. Django also emphasizes security, has a strong community, and is used in many professional applications.

### 5. ORM
The Django model is called an **ORM** (Object-Relational Mapping) because it allows developers to interact with a database using Python classes instead of raw SQL. It maps Python objects to database tables, automatically handling the translation between the two.