from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import datetime

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='')
    datefield = models.DateField(default=datetime.date.today)
