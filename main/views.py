from django.shortcuts import render, redirect
from main.forms import UnlimitedBaconForm
from main.models import UnlimitedBacon
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    product_entries = UnlimitedBacon.objects.all()

    context = {
        'app_name' : 'Unlimited Bacon',
        'name': 'Muhammad Ghaza Fadhlilbaqi',
        'class': 'PBP KKI',
        'product_entries': product_entries,
    }

    return render(request, "main.html", context)

def create_bacon_entry(request):
    form = UnlimitedBaconForm()

    if request.method == 'POST':
        form = UnlimitedBaconForm(request.POST)
        if form.is_valid():
            form.save()
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