import datetime

from django.db import models
from django.utils import timesince, timezone

class Schedule(models.Model):
    objects = models.Manager()      #To resolve the no objects warning
    id = models.AutoField(primary_key=True)
    task_brief = models.CharField("Task", max_length=100, blank=False)
    deadline = models.DateTimeField('Time Due', blank=False)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.id