from .serializers import SchoolSerializer, StudentSerializer, SchoolStudentSerializer
from .models import School, Student
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

# Pagination classes
class SchoolResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50

class StudentResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

# Viewsets
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    pagination_class = SchoolResultsSetPagination
    queryset = School.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name',]
    ordering_fields = ['name',]

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    pagination_class = StudentResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', '=student_id', 'birth_date']
    ordering_fields = ['first_name', 'last_name', 'student_id', 'birth_date']

    def get_queryset(self):
        return Student.objects.all()
    
class SchoolStudentViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolStudentSerializer
    pagination_class = StudentResultsSetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', '=student_id']
    ordering_fields = ['first_name', 'last_name', 'student_id', 'birth_date']
    
    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])

