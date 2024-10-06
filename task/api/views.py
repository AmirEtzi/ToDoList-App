from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from task.models import ToDoTask
from task.api.serializers import ToDoTaskSerializer


@api_view(["GET"])
def task_list(request):
    if request.method == "GET":
        query = ToDoTask.objects.all()
        serializer = ToDoTaskSerializer(query, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def api_task_detail(request, id):
    try:
        task = ToDoTask.objects.get(pk=id)

    except ToDoTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = ToDoTaskSerializer(task)
        return Response(serializer.data)


@api_view(["PUT"])
def api_task_update(request, pk):
    try:
        task = ToDoTask.objects.get(pk=pk)
    except ToDoTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {}
    if request.method == "PUT":
        serializer = ToDoTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data["Update"] = "Update is succesfull"
            return Response(data=data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
