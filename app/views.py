from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView
from app.models import *

class Home(TemplateView):
    template_name='app/Home.html'


class Student_list(ListView):
    model=School
    template_name='app/Student_list.html'
    context_object_name='schools'

class School_Detail(DetailView):
    model=School
    context_object_name='Schooolobj'
    template_name='app/School_Detail.html'
    