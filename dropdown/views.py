from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *

def index(request):
    program = Programming.objects.all()
    d = {'program': program}
    return render(request,'index.html',d)

def load_courses(request):
    programming_id = request.GET.get('programming')
    courses = Course.objects.filter(programming_id=programming_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})