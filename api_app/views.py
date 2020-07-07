from .serializers import SchoolSerializer, StudentSerializer, SchoolStudentSerializer
from .models import School, Student
from rest_framework import viewsets
from rest_framework import filters

# Viewsets
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name',]

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', '=student_id']

    def get_queryset(self):
        return Student.objects.all()
    
class SchoolStudentViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolStudentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', '=student_id']

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])

