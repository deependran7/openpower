from django.db import models

# Create your models here.


# Create your models here.


class UploadFile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    institution = models.CharField(max_length=100)
    filename = models.CharField(max_length=100)
    filelink= models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name


    def __unicode__(self):
        return self.filename

    def __str__(self):
        return self.name

    def __str__(self):
        return self.filename



