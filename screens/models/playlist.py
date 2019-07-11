from django.db import models

from screens.models import Source


class Playlist(models.Model):
    name = models.TextField()
    description = models.TextField()
    plays_everything = models.BooleanField(default=False)
    interspersed_source = models.ForeignKey(Source, null=True, default=None, on_delete=models.SET_NULL, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def get_sources(self):
        if self.plays_everything:
            return Source.objects\
                .exclude(exclude_from_play_all=True)\
                .exclude(pk=self.interspersed_source_id)
        else:
            return Source.objects\
                .filter(playlistentry__playlist=self)\
                .exclude(pk=self.interspersed_source_id)\
                .order_by('playlistentry__number')

    def __str__(self):
        return self.name
