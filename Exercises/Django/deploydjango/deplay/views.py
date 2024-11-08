from django.shortcuts import render

def home(request):
    data = {'mensage': 'Olá a partir da views'}
    return render(request, 'home.html', data)
