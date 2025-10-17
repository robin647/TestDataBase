from rest_framework import viewsets
from .models import ContactForm,behab
from .serializers import ContactFormSerializer,behabSerializer

class ContactFormViewSet(viewsets.ModelViewSet):
    queryset = ContactForm.objects.all()
    serializer_class = ContactFormSerializer


class behabViewSet(viewsets.ModelViewSet):
    queryset = behab.objects.all()
    serializer_class = behabSerializer