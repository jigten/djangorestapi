from django.http import HttpResponse
from .serializers import SchoolSerializer, StudentSerializer
from .models import School, Student
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

# Viewsets
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()

    # def list(self, request):
    #     queryset = School.objects.all()
    #     serializer = SchoolSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def create(self, request):
    #     serializer = SchoolSerializer(data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def retrieve(self, request, pk=None):
    #     queryset = School.objects.all()
    #     school = get_object_or_404(queryset, pk=pk)
    #     serializer = SchoolSerializer(school)
    #     return Response(serializer.data)

    # def update(self, request, pk=None):
    #     school = School.objects.get(pk=pk)
    #     serializer = SchoolSerializer(school, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()