from django.conf import settings
from django.db import models


class People(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=256,
    )
    image = models.URLField()
