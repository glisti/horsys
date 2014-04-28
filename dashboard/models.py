from django.db import models

from core.models import HorsysBaseModel

class SiteMessage(HorsysBaseModel):
    text       = models.TextField()
    created_by = models.ForeignKey('User')