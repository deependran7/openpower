from django.db import models

# Create your models here.
class UploadFile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    file = models.FileField()