from django.shortcuts import render
from .models import Hobby

def index(request):
    hobbies = Hobby.objects.all()
    return render(request, "hobby/index.html", {'hobbies': hobbies})
