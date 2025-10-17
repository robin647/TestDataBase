from rest_framework import serializers
from .models import ContactForm, behab

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = '__all__'

class behabSerializer(serializers.ModelSerializer):
    class Meta:
        model = behab
        fields = '__all__'
