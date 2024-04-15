from django import forms
from .models import Task


class UpdateTask(forms.Form):
    title = forms.CharField(max_length=255)


class CreateTaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ("title",)