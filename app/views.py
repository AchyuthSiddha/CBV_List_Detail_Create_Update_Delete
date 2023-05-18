from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView
from app.models import *

class Home(TemplateView):
    template_name='app/Home.html'


class Student_list(ListView):
    model=School
    template_name='app/Student_list.html'
    context_object_name='schools'
    