from django.shortcuts import render
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    # sorts tasks from newest to oldest.
    tasks = Task.objects.all().order_by ("-created_at")

    context = {
        "tasks": tasks,
    }

    return render(request, "tasks/task_list.html", context)

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm()

    context = {
        "form": form,
    }
    
    return render(request, "tasks/task_form.html", context)