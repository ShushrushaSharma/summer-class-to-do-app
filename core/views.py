from django.shortcuts import render
from core.models import *
# Create your views here.

def home_page(request):
    return render(request=request, template_name="index.html")

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