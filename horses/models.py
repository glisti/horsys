from django.core.urlresolvers import reverse
from django.db import models

import datetime
import os

FRONT_PASTURE = 'FRONT'
BACK_PASTURE  = 'BACK'
PONY_PASTURE  = 'PONY'
STALLS        = 'STALLS'
PLACEMENT_CHOICES = (
    (FRONT_PASTURE, 'Front Pasture'),
    (BACK_PASTURE, 'Back Pasture'),
    (PONY_PASTURE, 'Pony Pasture'),
    (STALLS, 'Stalls'),
)

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return datetime.datetime.now()

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^horses\.models\.AutoDateTimeField"])

# def photo_path(instance, file):
#     return os.path.join('horses',str(instance.id),'photo')

# def record_path(instance, file):
#     return os.path.join('horses',str(instance.id),'record', '%Y/%m/%d')

class Horse(models.Model):
    name                    = models.CharField(max_length=100)
    photo                   = models.ImageField(upload_to='horses/photos')
    description             = models.TextField()
    owner_name              = models.CharField(max_length=100)
    location                = models.CharField(max_length=6, choices=PLACEMENT_CHOICES,default=STALLS)
    feed                    = models.CharField(max_length=100)
    am_amount               = models.CharField(max_length=100)
    pm_amount               = models.CharField(max_length=100)
    beet_pulp               = models.CharField(max_length=30)
    rice_bran               = models.CharField(max_length=30)
    supplements             = models.CharField(max_length=100)
    hay                     = models.CharField(max_length=100)
    turnout                 = models.CharField(max_length=100)
    blanketing_instructions = models.TextField()
    created                 = AutoDateTimeField(editable=False)
    modified                = AutoDateTimeField()

    def get_absolute_url(self):
        return reverse('horse_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.name


class MedicalRecord(models.Model):
    horse    = models.ForeignKey('Horse')
    title    = models.CharField(max_length=100)
    form     = models.FileField(upload_to='horses/records')
    # added by
    created  = AutoDateTimeField(editable=False)
    modified = AutoDateTimeField()

    def get_absolute_url(self):
        return reverse('medicalrecord_detail', kwargs={'pk': self.pk})


class Task(models.Model):
    horse     = models.ForeignKey('Horse')
    task      = models.TextField()
    program   = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    # appointmenttime?
    # added by
    created   = AutoDateTimeField(editable=False)
    modified  = AutoDateTimeField()

    def get_absolute_url(self):
        return reverse('task_detail', kwargs={'pk': self.pk})


class Note(models.Model):
    horse   = models.ForeignKey('Horse')
    text    = models.TextField()
    # added by
    created = AutoDateTimeField(editable=False)
