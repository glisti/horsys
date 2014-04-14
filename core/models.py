from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from core.fields import AutoDateTimeField

class HorsysBaseModel(models.Model):
    # created_by  = models.ForiegnKey(User)
    # modified_by = models.ForiegnKey(User)
    created     = AutoDateTimeField(editable=False)
    modified    = AutoDateTimeField()

    class Meta:
        abstract = True

    # def save(self, *args, **kwargs):
    #     super(HorsysBaseModel, self).save(*args,**kwargs)