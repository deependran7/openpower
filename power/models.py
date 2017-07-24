from django.db import models

# Create your models here.


class Documents(models.Model):
    subheading = models.CharField(max_length=100)
    dimages = models.CharField(max_length = 50)
    text = models.TextField()

class UploadFile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    file = models.FileField()