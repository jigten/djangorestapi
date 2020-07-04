from django.contrib import admin
from .models import Student, School

# Registering models for API
admin.site.register(Student)
admin.site.register(School)