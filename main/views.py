from django.shortcuts import render

def show_main(request):
    context = {
        'app_name' : 'Unlimited Bacon',
        'name': 'Muhammad Ghaza Fadhlilbaqi',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)