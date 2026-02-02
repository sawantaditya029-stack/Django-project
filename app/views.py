from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .models import Contact
from .serializer import ContactSerializer

class ContactViewsets(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
