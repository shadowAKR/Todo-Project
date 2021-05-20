from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .forms import Todoforms
from django.views.generic import ListView,DetailView, UpdateView, DeleteView

# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task_view.html'
    context_object_name = 'obj'
    def post(self,request,format=None):
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
        return redirect('/')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'

class TaskUpdateView(UpdateView):
    model= Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','priority','date')
    success_url = reverse_lazy('cbvtask')

class TaskDeleteview(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')

