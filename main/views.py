from django.shortcuts import render, redirect, reverse 
from main.forms import UnlimitedBaconForm
from main.models import UnlimitedBacon
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse

@login_required(login_url='/login')
def show_main(request):
    product_entries = UnlimitedBacon.objects.filter(user=request.user)

    context = {
        'app_name' : 'Unlimited Bacon',
        'name': request.user.username,
        'class': 'PBP KKI',
        'product_entries': product_entries,
        'last_login': request.COOKIES.get('last_login', 'Not set'),
    }

    return render(request, "main.html", context)

def create_bacon_entry(request):
    form = UnlimitedBaconForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')
        
    context = {'form': form}
    return render(request, 'create_bacon_entry.html', context)

def show_xml(request):
    data = UnlimitedBacon.objects.all()
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json(request):
    data = UnlimitedBacon.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def show_xml_by_id(request, id):
    data = UnlimitedBacon.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')

def show_json_by_id(request, id):
    data = UnlimitedBacon.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form': form}   
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                response  = HttpResponseRedirect(reverse('main:show_main'))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            
        else:
            messages.error(request, 'Invalid username or password. Try again.')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get mood entry based on id
    product = UnlimitedBacon.objects.get(pk = id)

    # Set mood entry as an instance of the form
    form = UnlimitedBaconForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood based on id
    mood = UnlimitedBacon.objects.get(pk = id)
    # Delete mood
    mood.delete()
    # Return to home page
    return HttpResponseRedirect(reverse('main:show_main'))
