from django.shortcuts import render
from .models import Project


def home(request):
    #Импорт всех данных из базы данных
    progects = Project.objects.all()
    return render(request, 'portfolio/home_page.html', {'projects' : progects})
