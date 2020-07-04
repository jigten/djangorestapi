from django.urls import path, include
from .views import SchoolViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('schools', SchoolViewSet, basename='schools')
router.register('students', StudentViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls)),
    path('/<int:pk>', include(router.urls)),
]