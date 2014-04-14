from django.db import models
from django.utils import timezone

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^horses\.models\.AutoDateTimeField"])

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()