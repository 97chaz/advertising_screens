import os
import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.template.loader import get_template
from django.utils import timezone
from django.utils.html import escape, format_html


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return filename


class Source(models.Model):
    IMAGE = 'IMG'
    VIDEO = 'VID'
    IFRAME = 'FRM'
    YOUTUBEVIDEO = 'YTV'
    types = (
        (IMAGE, 'Image'),
        (VIDEO, 'Video'),
        (IFRAME, 'Website'),
        (YOUTUBEVIDEO, 'YouTube Video')
    )
    type = models.CharField(max_length=3, choices=types)
    name = models.TextField()
    file = models.FileField(upload_to=get_file_path,
                            null=True,
                            blank=True,
                            help_text="")
    url = models.URLField(blank=True, verbose_name="Website Address", help_text="Only required if website type")
    ytid = models.CharField(blank=True, max_length=20, verbose_name="YouTube Video ID", help_text="Only the YouTube Video ID is required. Only required if YouTube Type")
    exclude_from_play_all = models.BooleanField(default=False)
    expires_at = models.DateTimeField(blank=True, null=True, default=None)
    valid_from = models.DateTimeField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.type in [self.IMAGE, self.VIDEO] and self.file.name is None:
            raise ValidationError({'file': "File cannot be blank for image or video type sources"})
        if self.type == self.VIDEO and self.file.name[-4:] != ".mp4":
            raise ValidationError({'file': "Video files must have .mp4 extensions"})

    def src(self):
        if self.type in [self.IFRAME]:
            return self.url
        return self.file.url

    def image_preview(self):
        return get_template("screens/source_preview.html").render({"source": {"source": self}})

    image_preview.short_description = 'Preview'

    def playlist_names(self):
        result = set()
        for name in self.playlistentry_set.all().values_list("playlist__name", flat=True):
            result.add(name)
        for name in self.playlist_set.values_list("name", flat=True):
            result.add(name)
        return list(result)

    playlist_names.short_description = "Playlists"
