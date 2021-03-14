from django.db import models

# Create your models here.
class Student(models.Model):
    studentName = models.CharField(default="Null", max_length=250)
    studentClass = models.CharField(default="Null", max_length=250)
    
    def __str__(self):
        return self.studentName
