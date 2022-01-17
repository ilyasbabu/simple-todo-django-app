from asyncio import tasks
from dataclasses import field, fields
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
from .form import Taskform
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class TaskListView(ListView):
    model=Task
    template_name='task_view.html'
    context_object_name='task'

class TaskDetailView(DetailView):
    model=Task
    template_name='task_detail.html'
    context_object_name='task'

class TaskUpdateView(UpdateView):
    model=Task
    template_name='task_detail.html'
    context_object_name='form'
    fields=['title','priority']
    success_url='/'
    # def get_success_url(self):
    #     return reverse_lazy('',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=Task
    template_name='confirm.html'
    context_object_name='task'
    success_url=reverse_lazy('TaskListView')

#function based view to list out all the tasks
#_______________________________________________
# def view(request):
#     task=Task.objects.all().order_by('-id')
#     context={
#         'task':task
#     }
#     if request.method=="POST":
#         title=request.POST['title']
#         priority=request.POST['priority']
#         task=Task(title=title,priority=priority)
#         task.save()
#         return redirect('/')
#     return render(request,'task_view.html',context)

def add(request):
    if request.method=="POST":
        title=request.POST['title']
        priority=request.POST['priority']
        task=Task(title=title,priority=priority)
        task.save()
        return redirect('/')
    return render(request,'task_view.html')

def done(request,task_id):
    tasks=Task.objects.get(id=task_id)
    task=Task.objects.all().order_by('-id')
    if request.method=="GET":
        tasks.delete()
        return redirect('/')
    return render(request,'task_view.html',{'task':task})

def update(request,task_id):
    tasks=Task.objects.get(id=task_id)
    form=Taskform(request.POST or None,instance=tasks)
    task=Task.objects.all().order_by('-id')
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'task_view.html',{'tasks':tasks,'form':form,'task':task})