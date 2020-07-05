from django.db import models
import uuid

# Models
# School model
class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = models.PositiveSmallIntegerField() # Don't expect maximum number of students accomodated to exceed the limit of PositiveSmallIntegerField

    def __str__(self):
        return self.name

# Student model
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    school = models.ForeignKey(School, related_name='student', on_delete=models.CASCADE, default=None) # many-to-one relationship with School

    def __str__(self):
        return self.first_name + self.last_name