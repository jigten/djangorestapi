from rest_framework import serializers
from .models import School, Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SchoolStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'student_id', 'birth_date', 'school')
        read_only_fields = ('school',)

    def create(self, validated_data):
        school = School.objects.get(pk=self.context['view'].kwargs['school_pk'])
        validated_data['school'] = school
        return super(SchoolStudentSerializer, self).create(validated_data)