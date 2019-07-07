from django.db import models

from screens.models.schedule import Schedule


class Screen(models.Model):
    name = models.TextField()
    schedule = models.ForeignKey(Schedule, on_delete=models.SET_NULL, null=True)
    ip = models.GenericIPAddressField()
