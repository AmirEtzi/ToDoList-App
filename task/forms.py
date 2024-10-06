from django import forms
from task.models import ToDoTask


class DataInput(forms.DateInput):
    input_type = "date"


class CreateTask(forms.ModelForm):
    created = forms.DateField(widget=DataInput)

    class Meta:
        model = ToDoTask
        fields = ("title", "created", "category", "description")
