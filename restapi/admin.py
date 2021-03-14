from django.contrib import admin
from .models import Student
# Register your models here.
class filterStudent(admin.ModelAdmin):
    list_display = ('studentName','studentClass')
admin.site.register(Student,filterStudent)