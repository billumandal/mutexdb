from __future__ import unicode_literals
from django.db import models
import datetime

class Mutexs(models.Model):
    mutexs = models.CharField(max_length=500) 

    verbose_name='mutexes'

    def __unicode__(self):
        return self.mutexs

class Userlog(models.Model):
    client_ip = models.GenericIPAddressField()
    visiting_time = models.DateTimeField()

    # verbose_name='Userlog'

class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=False)
    company = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=70, blank=True)
    email = models.EmailField(max_length=100, blank=False)
    message = models.CharField(max_length=500, blank=False)

    def __unicode__(self):
    	return "{0}, {1}".format(self.id, self.email, self.name)