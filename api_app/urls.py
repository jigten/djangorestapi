from django.urls import path, include
from .views import SchoolViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.SimpleRouter()
router.register('schools', SchoolViewSet)
router.register('students', StudentViewSet)

schools_router = routers.NestedSimpleRouter(router, 'schools', lookup='school')
schools_router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include(schools_router.urls)),
]