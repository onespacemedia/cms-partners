from cms.apps.media.models import ImageRefField
from cms.models import OnlineBase
from django.db import models


class Partner(OnlineBase):
    title = models.CharField(
        max_length=200
    )

    summary = models.TextField(
        max_length=140,
        blank=True,
        null=True
    )

    logo = ImageRefField()

    website = models.CharField(
        max_length=140,
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.title
