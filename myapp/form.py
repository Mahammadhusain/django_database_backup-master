from django import forms
from .models import StudentModel


class StudentForm(forms.ModelForm):
  
   #Metadata
   class Meta:
       model = StudentModel
       fields = "__all__"
