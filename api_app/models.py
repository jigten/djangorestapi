from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    student_id = models.CharField(max_length=20)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + self.last_name

class School(models.Model):
    name = models.CharField(max_length=20)
    max_students = 10

    def __str__(self):
        return self.name