from core.models import *
from django import forms 

class student_enrollment_form(forms.ModelForm): # student_enrollment_form is the name of the form
    class Meta:
        model = Student # name of the model
        fields = "__all__" # specifying the field we want to show in the form

