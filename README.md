# Unlimited Bacon
PWS link: 

```
http://muhammad-ghaza31-unlimitedbacon.pbp.cs.ui.ac.id/
```

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
    - Then open 
    
    ```bash
    http://localhost:8000/
    ```

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

## Assignment 3

### 1. Data Delivery Purpose
Data delivery is needed for various different purposes, with one of the biggest one is user experience. Data delivery ensures that users get timely and accurate information, which in turn, will improve their overall experience.

### 2. XML v JSON
In my opinion, I prefer the JSON formats for data. The reason JSON is more popular is because it uses a more straight forward key-value format, which leads it to be more human readable compared to the complicated tag-structured format used by XML.

### 3. Usage of ```is_valid()```
The ```is_valid()``` method in Django forms is essential for validating form data according to specific rules. For example, a "price" field would require inputs to be a numerical value, if the conditions are met, the data will be saved, and error messages will appear if conditions are not met. This method is essential because it ensures that only valid data is processed, helps provide clear feedback to users, and keeps the code organized by handling validation in a single place.

### 4. Purpose of the ```csfr_token```
The ```csrf_token``` is crucial for securing Django forms against Cross-Site Request Forgery (CSRF) attacks. This token helps verify that form submissions are coming from your site, not from a malicious third-party site trying to trick users. 
if this token is not implemented in a Django form, it could lead to a **CSFR attack**. In this type of attack, the attacker sends a link in the form of sms, email, or chat. In this way, the attacker tricks the user who is already authenticated on the website to perform various actions such as transfer of funds, change of email, and so on. Depending upon the nature of the attack the attacker may take full access to the account.

### 5. Steps:
1. Creating Base HTML template by:
   - Creating ```templates``` directory in the ```Root``` directory
   - Create ```base.html``` file with the contents:

   ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
    </head>

    <body>
        {% block content %} {% endblock content %}
    </body>
    </html>
    ```

2. Make ```base.html``` as a template file by:
    - Opening ```settings.py``` and adjust the code:
    
    ```python
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'], # FILLING THE LIST WITH THIS CONTENT
            ...
        }
    ```

3. Changing IDs of models using UUID by:
    - Importing the ```uuid``` library

    ```python
    import uuid 
    from django.db import models
    ```
    - Adding the ```id``` model in ```models.py```:

    ```python
    # Create your models here.
    class UnlimitedBacon(models.Model):
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        description = models.TextField()
        stock = models.IntegerField()    
    ```
    - Then migrate any changes in ```models.py``` as usual

4. Create ```forms.py``` in the ```main``` directory, and fill it in with the following contents:

    ```python
    from main.models import UnlimitedBacon
    from django import forms

    class UnlimitedBaconForm(forms.ModelForm):
        class Meta:
            model = UnlimitedBacon
            fields = '__all__'
    ```
5. Update the ```views.py``` file by:
    - Importing ```redirect``` from ```django.shortcuts```:

    ```python
    from django.shortcuts import render, redirect
    ```
    - Adding the ```create_bacon_entry``` function:

    ```python
    def create_bacon_entry(request):
        form = UnlimitedBaconForm()

        if request.method == 'POST':
            form = UnlimitedBaconForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main:show_main')
            
        context = {'form': form}
        return render(request, 'create_bacon_entry.html', context)
    ```
    - Updating the ```show_main``` function:

    ```python
    def show_main(request):
        product_entries = UnlimitedBacon.objects.all() # ADDED product_entries VARIABLE

        context = {
            'app_name' : 'Unlimited Bacon',
            'name': 'Muhammad Ghaza Fadhlilbaqi',
            'class': 'PBP KKI',
            'product_entries': product_entries, # ADDED product_entries VARIABLE... again...
        }

        return render(request, "main.html", context)
    ```

6. Updating ```urls.py``` in the ```main``` directory by:
    - Importing the recently created ```create_bacon_entry``` function

    ```python
    from main.views import show_main, create_mood_entry
    ```
    - Adding a new URL path to ```url_patterns``` list

    ```python
    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create_bacon_entry', create_bacon_entry, name='create_bacon_entry'),
    ]
    ```

7. Creating and modifying HTML files in ```main/templates``` by:
    - Creating a new HTML file named ```create_bacon_entry.html``` with the following contents:

    ```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Product Entry</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```
    - Modifying the ```main.html``` file into:

    ```html
    {% extends 'base.html' %}
    {% block content %}
    <h1>{{ app_name }}</h1>

    <h5>Name:</h5>
    <p>{{ name }}</p>

    <h5>Class:</h5>
    <p>{{ class }}</p>


    {% if not product_entries %}
    <p>There are no products available in the shop.</p>
    {% else %}
    <table>
    <tr>
        <th>Product Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Stock</th>
    </tr>

    {% for product_entry in product_entries %}
    <tr>
        <td>{{product_entry.name}}</td>
        <td>{{product_entry.price}}</td>
        <td>{{product_entry.description}}</td>
        <td>{{product_entry.stock }}</td>
    </tr>
    {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:create_bacon_entry' %}">
    <button>Add Product</button>
    </a>

    {% endblock content %}
    ```

8. Creating Functions for XML, JSON, XML by ID and JSON by ID:
    - the XML function

    ```python
    def show_xml(request):
        data = UnlimitedBacon.objects.all()
        return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
    ```
    
    - the JSON function

    ```python
    def show_json(request):
        data = UnlimitedBacon.objects.all()
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    ```

    - the XML by ID function

    ```python
    def show_xml_by_id(request, id):
        data = UnlimitedBacon.objects.filter(pk=id)
        return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
    ```

    - the JSON by ID function

    ```python
    def show_json_by_id(request, id):
        data = UnlimitedBacon.objects.filter(pk=id)
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    ```

9. Routing the 4 new functions the ```urls.py``` file in the ```main``` directory

    ```python
    urlpatterns = [
        ...
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]
    ```

10. Last but not least, testing the site in the localhost with

    ```bash
    python manage.py runserver
    ```
o(*￣▽￣*)o DONE!!!

### 6. Postman Screenshots:
1. **XML**
![](static/images/xml.png)

2. **JSON**
![](static/images/json.png)

3. **XML by ID**
![](static/images/xmlById.png)

4. **JSON by ID**
![](static/images/jsonById.png)

## Assignment 4

### 1. ```HttpResponseRedirect()``` Vs ```redirect()```
Although both functions purpose are the same (redirecting users to a different url), they function quite differently
- ```HttpResponseRedirect()```
    Only accepts a full direct URL for redirection. Example:

    ```python
    response = HttpResponseRedirect(reverse('main:show_main'))
    # the reverse function returns the url of it's parameter
    
    ```
- ```redirect()```
    A more flexible redirection function which accepts direct urls, view names,  or even model instances. Example:

    ```python
    return redirect('main:show_main')
    ```

### 2. ```mood_entry``` link with ```User```


### 3. Authentication vs Authorization


### 4.  Use of Cookies


### 5. Steps:
1. 