from django.shortcuts import render, redirect
from core.models import *
from core.forms import *
# Create your views here.

def home_page(request):
    form = student_enrollment_form() # the form we created
    if request.method == "POST": # checking the form method sent to us from the forms
        if form.is_valid(): # checks if the form is valid or not
            form.save() # saving all the data from the form to database
            return redirect("home_page")
    
    context = {
        "form": form
    }
    return render(request=request, template_name="index.html",context=context)



# getting the specialization from specialization model
def spec(request):
    # this is the syntax to get the data from model => model_name.object.all()
    the_specs = Specialization.objects.all()
    # context is the way of passing the data to the html file
    context = {
        # variable name to be passed in html
        "the_specs": the_specs
    }
    return render(request=request,template_name="spec.html",context=context)

def uni(request):
    the_uni = University.objects.all()
    context = {
        "the_uni": the_uni
    }
    return render(request=request,template_name="uni.html",context=context)

