from django.db import models
from django.urls import reverse
from datetime import datetime, timedelta

from screens.models import Source
from screens.models.schedule import Schedule


class Screen(models.Model):
    name = models.TextField()
    schedule = models.ForeignKey(Schedule, on_delete=models.PROTECT, null=True)
    interspersed_source = models.ForeignKey(Source,
                                            null=True,
                                            default=None,
                                            on_delete=models.SET_NULL,
                                            blank=True,
                                            help_text="Optional. Plays randomly between other content")
    ip = models.GenericIPAddressField()
    last_seen = models.DateTimeField(auto_now_add=True, blank=True)
    
    def online(self):
        return self.last_seen and self.last_seen >= datetime.now()-timedelta(minutes=2)
    online.boolean = True
        

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('screens/screen_view', args=[str(self.id)])
