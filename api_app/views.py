from .serializers import SchoolSerializer, StudentSerializer, SchoolStudentSerializer
from .models import School, Student
from rest_framework import viewsets

# Viewsets
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()
    
class SchoolStudentViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolStudentSerializer

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])