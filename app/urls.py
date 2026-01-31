from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewsets

router = DefaultRouter()
router.register(r'contact', ContactViewsets, basename='contact')

urlpatterns = [
    path('api/', include(router.urls)),
]
