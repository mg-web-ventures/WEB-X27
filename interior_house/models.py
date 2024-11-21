from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    username = models.EmailField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")


class ContactForm(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    project_location = models.TextField(max_length=100, default="")
    describe_project = models.TextField(max_length=200, default="")
    created_at = models.DateTimeField(auto_now_add=True)
