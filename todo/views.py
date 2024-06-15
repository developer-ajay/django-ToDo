from django.shortcuts import get_object_or_404, redirect, render

from todo.models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

def mark_as_done(request , pk):
    task = Task.objects.get(id = pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_undone(request , pk):
    task = Task.objects.get(id = pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def deleteTask(request ,pk):
    task = Task.objects.get(id = pk)
    task.delete()
    return redirect('home')

def editTask(request , pk):
    task = get_object_or_404(Task ,pk=pk)
    if request.method == 'POST':
        new_task = request.POST['task']
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context ={
            'task' : task
        }

        return render(request , 'edit.html', context)
