from django.urls import path,include
from rest_framework import routers
from app.views import ContactViewsets

router = routers.DefaultRouter()
router.register(r'contact',ContactViewsets)


urlpatterns = [
    path("",include(router.urls)),
]
