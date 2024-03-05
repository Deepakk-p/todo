from django import forms
from .models import Todomodel

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todomodel
        fields="__all__"
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Title"}),
            "description":forms.Textarea(attrs={"class":"form-control","placeholder":"Enter Description"}),
            "date":forms.DateInput(attrs={"class":"form-control","placehoder":"Enter Date"}),
            # "image":forms.FileInput(attrs={"class":"form-control","placehoder":"Enter Image"}),
        }