from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Task
from .form import Taskform

# Create your views here.

def view(request):
    task=Task.objects.all().order_by('-id')
    context={
        'task':task
    }
    if request.method=="POST":
        title=request.POST['title']
        priority=request.POST['priority']
        task=Task(title=title,priority=priority)
        task.save()
        return redirect('/')
    return render(request,'task_view.html',context)

def done(request,task_id):
    tasks=Task.objects.get(id=task_id)
    task=Task.objects.all().order_by('-id')
    if request.method=="POST":
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