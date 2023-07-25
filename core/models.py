from django.db import models

# Create your models here.


class Specialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class University(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    enrolled_in = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    LMU_ID = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    

