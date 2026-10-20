from django.shortcuts import render
from .models import Task

# Create your views here.
def task_list(request):
    # sorts tasks from newest to oldest.
    tasks = Task.objects.all().order_by ("-created_at")

    context = {
        "tasks": tasks,
    }

    return render(request, "tasks/task_list.html", context)