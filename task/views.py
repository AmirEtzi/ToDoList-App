from django.shortcuts import render
from task.models import Category, ToDoTask
from task.forms import CreateTask
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404, redirect


def show_task(request):
    query = ToDoTask.objects.all().order_by("created")

    # Create form part
    if request.method == "POST":
        form = CreateTask(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/task")
    else:
        form = CreateTask()
    context = {
        "query": query,
        "form": form,
    }

    return render(request, "task/index.html", context)


class TaskDetail(DetailView):
    model = ToDoTask
    template_name = "task/detail.html"


def delete_task(request, id):
    task = get_object_or_404(ToDoTask, id=id)
    task.delete()
    return redirect("show_task")
