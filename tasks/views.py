from django.shortcuts import render, redirect
from tasks.forms import TaskModelForm, TaskDetailModelForm
from tasks.models import *
from datetime import date
from django.db.models import Q, Count
from django.contrib import messages

# Create your views here.

def manager_dashboard(request):
    type = request.GET.get('type', 'all')
    print(type)
    tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()

    # Getting task count
    # total_task = tasks.count()
    # total_pending = Task.objects.filter(status="PENDING").count()
    # total_in_progress = Task.objects.filter(status="IN_PROGRESS").count()
    # total_completed = Task.objects.filter(status="COMPLETED").count()

    # count = {
    #     'total_task':
    #     'total_completed':
    #     'total_in_progress':
    #     'total_pending': 
    # }

    counts = Task.objects.aggregate(
        total_task=Count('id'),
        total_completed=Count('id', filter=Q(status='COMPLETED')),
        total_in_progress=Count('id', filter=Q(status="IN_PROGRESS")),
        total_pending=Count('id', filter=Q(status="PENDING")),
    )

    # Retriving task data

    BASE_QUERY = Task.objects.select_related('details').prefetch_related('assigned_to')

    if type == 'completed':
        tasks = BASE_QUERY.filter(status='COMPLETED')
    elif type == 'in-progress':
        tasks = BASE_QUERY.filter(status='IN_PROGRESS')
    elif type == 'pending':
        tasks = BASE_QUERY.filter(status='PENDING')
    else:
        tasks = BASE_QUERY.all()

    context = {
        "tasks": tasks,
        "counts": counts
    }

    return render(request, "dashboard/manager-dashboard.html", context=context)

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    context = {
        "name": ["Shifat", "Rifat", "Abir"]
    }
    return render(request, "test.html", context)

def create_task(request):
    task_form = TaskModelForm() # GET
    task_detail_form = TaskDetailModelForm() 

    if request.method == "POST":
        task_form = TaskModelForm(request.POST) # GET
        task_detail_form = TaskDetailModelForm(request.POST)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, message='Task create successfully')

            return redirect('create-task')
        
    context = {"task_form": task_form, 'task_detail_form': task_detail_form}
    return render(request, "task_form.html", context)

# def update_task(request, id):
#     task = Task.objects.get(id = id)
#     task_form = TaskModelForm(instance=task) # GET

#     if task.details:
#         task_detail_form = TaskDetailModelForm(instance=task.details) 

#     if request.method == "POST":
#         task_form = TaskModelForm(request.POST) # GET
#         task_detail_form = TaskDetailModelForm(request.POST, instance=task.details)

#         if task_form.is_valid() and task_detail_form.is_valid():
#             task_form.save()
#             task_detail = task_detail_form.save(commit=False)
#             task_detail.task = task
#             task_detail.save()

#             messages.success(request, message='Task updated successfully')
#             print("Priority value:", task.details.priority)

#             return redirect('update-task', id)
        
#     context = {"task_form": task_form, 'task_detail_form': task_detail_form}
#     return render(request, "task_form.html", context)

def update_task(request, id):
    task = Task.objects.get(id=id)
    task_form = TaskModelForm(instance=task)

    try:
        task_detail = task.details
    except TaskDetail.DoesNotExist:
        task_detail = None

    task_detail_form = TaskDetailModelForm(instance=task_detail)

    if request.method == "POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_detail_form = TaskDetailModelForm(request.POST, instance=task_detail)

        if task_form.is_valid() and task_detail_form.is_valid():
            task = task_form.save()

            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task  # reattach OneToOne
            task_detail.save()

            messages.success(request, 'Task updated successfully')
            return redirect('update-task', id)

    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "task_form.html", context)

def delete_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.delete()

        # messages.success(request, 'Task deleted successfully')
        return redirect('manager-dashboard')
    else:
        # messages.error(request, 'Something went wrong!')
        return redirect('manager-dashboard')


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
    # taskTrue = Task.objects.filter(status="PENDING").exists()
    # taskFalse = Task.objects.filter(status="jfsdofjos").exists()

    # Select * from Task and TaskDetail
    # tasks = Task.objects.select_related('details').all()

    # For onetomany and manytomany relations
    tasks = Project.objects.prefetch_related('task_set').all()

    # return render(request, "show_task.html", {"tasks": tasks, "task3": task_3})
    return render(request, "show_task.html", {"tasks": tasks})