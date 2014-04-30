from django.db import models
from django.contrib.auth.models import User

from core.models import HorsysBaseModel

class DashboardMessage(HorsysBaseModel):
    message    = models.TextField()
    created_by = models.ForeignKey(User)