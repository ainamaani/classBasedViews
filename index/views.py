from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . models import Task

# Create your views here.
class TaskList(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

class TaskDetail(DetailView):
    model = Task
    template_name = 'task.html'
    context_object_name = 'task'