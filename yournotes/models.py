from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.


def upload_location(instance,filename):
    return "%s/%s" %(instance.id, filename)

class NotesUpload(models.Model):
    name = models.CharField(max_length=120)
    institution = models.CharField(max_length=120)
    filename = models.CharField(max_length=120)
    #content = models.TextField()
    notefile = models.FileField(upload_to=upload_location ,null=True, blank=False)

    timestamp = models.DateTimeField(auto_now = False, auto_now_add=True)

    def __unicode__(self):
        return self.name + self.filename

    def __str__(self):
        return self.name + self.filename

    def get_absolute_url(self):
        return "%s/"%(self.id)

