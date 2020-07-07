from django.http import HttpResponse
from .serializers import SchoolSerializer, StudentSerializer, SchoolStudentSerializer
from .models import School, Student
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Viewsets
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Student.objects.all()

    # override create method for maximum students check
    # def create(self, request):
    #     serializer_class = StudentSerializer
    #     serializer = serializer_class(data=request.data)

    #     if serializer.is_valid():
    #         # get the relevant school
    #         school_pk = serializer.validated_data.get("school").id
    #         school = get_object_or_404(School, pk=school_pk)
    #         # check if school has maximum number of students enrolled
    #         if(school.student.count() == school.max_students):
    #             # return error message if max students reached
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         else:
    #             # enroll the student otherwise
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SchoolStudentViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolStudentSerializer

    def get_queryset(self):
        return Student.objects.filter(school=self.kwargs['school_pk'])

    # override create method for maximum students check
    # def create(self, request, school_pk=None):
    #     serializer_class = StudentSerializer
    #     serializer = serializer_class(data=request.data)

    #     if serializer.is_valid():
    #         # get the relevant school
    #         school = get_object_or_404(School, pk=school_pk)
    #         # check if school has maximum number of students enrolled
    #         if(school.student.count() == school.max_students):
    #             # return error message if max students reached
    #             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #         else:
    #             # enroll the student otherwise
    #             serializer.save(school=school)
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

