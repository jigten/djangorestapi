# Django School Management Rest API 
This is a REST API created using the Django REST framework to fulfill the requirements of the Manatal Django backend challenge. 

## Features
- Create schools and students
- Associate students with a school
- Creating a student generates a universally unique identifier (UUID) 
- Adding students to a school that has reached its maximum will return a validation error

## Endpoints
- `/schools/`
- `/schools/:id/`
- `/schools/:id/students/`
- `/schools/:id/students/:id`
- `/students/`
- `/students/:pk`

## Technologies/ Packages used
- Django / Django REST Framework
- DRF Nested Routers
- Pipenv
- PostgreSQL

## Time taken for each section
- Step 1 = 2 hours 30 minutes
- Step 2 = 4 hours
- Step 3 = 5 hours
- Bonus = 2 hours