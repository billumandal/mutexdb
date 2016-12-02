from __future__ import unicode_literals
from django.db import models

class Mutexs(models.Model):
    mutexs = models.CharField(max_length=500) 

    def __unicode__(self):
        return self.mutexs

class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=False)
    company = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=70, blank=True)
    email_address = models.EmailField(max_length=100, blank=True)
    message = models.CharField(max_length=500, blank=True)
    
