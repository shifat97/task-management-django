from django.shortcuts import render
from tasks.forms import TaskModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q

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
    # tasks = TaskDetail.objects.exclude(priority="L")

    # Show tasks where 'c' word exits and status is PENDING
    # tasks = Task.objects.filter(title__icontains="c", status="PENDING")

    # Show tasks where status is PENDING or IN_PROGRESS
    # tasks = Task.objects.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))

    # Check if data is exits() or not
    taskTrue = Task.objects.filter(status="PENDING").exists()
    taskFalse = Task.objects.filter(status="jfsdofjos").exists()

    # return render(request, "show_task.html", {"tasks": tasks, "task3": task_3})
    return render(request, "show_task.html", {"taskTrue": taskTrue, "taskFalse": taskFalse})