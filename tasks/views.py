from django.shortcuts import render
from tasks.forms import TaskModelForm
from tasks.models import *
from datetime import date

# Create your views here.

def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    context = {
        "name": ["Shifat", "Rifat", "Abir"]
    }
    return render(request, "test.html", context)

def create_task(request):
    form = TaskModelForm() # GET

    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():

            form.save()

            return render(request, "task_form.html", {"form": form, "message": "Task Added Successfully"})
        
    context = {"form": form}
    return render(request, "task_form.html", context)

def view_task(request):
    # Retrieve all data from task model
    # tasks = Task.objects.all()
    # task_3 = Task.objects.get(id=1)

    # Filter data with status
    # pending_task = Task.objects.filter(status="PENDING")

    # Filter with today's due task
    # due_date_task = Task.objects.filter(due_date=date.today())

    # Show the task which priority is not low
    tasks = TaskDetail.objects.exclude(priority="L")

    # return render(request, "show_task.html", {"tasks": tasks, "task3": task_3})
    return render(request, "show_task.html", {"tasks": tasks})