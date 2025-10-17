from django.db import models

# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
class behab(models.Model):
    sleep = models.CharField(max_length=100)
    read = models.TimeField()

    def __str__(self):
        return self.sleep