from django.urls import path, include
from .views import SchoolViewSet, StudentViewSet, SchoolStudentViewSet
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('schools', SchoolViewSet, basename="school")
router.register('students', StudentViewSet, basename="student")

schools_router = routers.NestedDefaultRouter(router, 'schools', lookup='school')
schools_router.register('students', SchoolStudentViewSet, basename="school-student")

urlpatterns = [
    path('', include(router.urls)),
    path('', include(schools_router.urls)),
]