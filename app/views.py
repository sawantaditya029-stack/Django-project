from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Contact
from .serializer import ContactSerializer

class ContactViewsets(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    