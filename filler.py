import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apphome.settings')

import django
django.setup()

from api_app.models import School, Student
from faker import Faker

obj = Faker()

def create_school():
    name = obj.random_elements(elements = ("AIT", "ETH Zurich", "MIT", "Sherubtse College"), length=1)[0]
    max_students = obj.random_int(min = 10, max = 50)
    school, created = School.objects.get_or_create(name = name, defaults = {'max_students' : max_students})
    return school

def fill(N=20):
    for i in range(N):
        first_name = obj.first_name()
        last_name = obj.last_name()
        student_id = obj.random_number(fix_len = 6)
        birth_date = obj.date_between(start_date = '-30y', end_date='-18y')
        school = create_school()

        Student.objects.get_or_create(first_name = first_name, last_name = last_name, student_id = student_id, birth_date = birth_date, defaults = {'school' : school})

if __name__ == '__main__':
    print("Populating database with random data...")
    fill()
    print("Done")
