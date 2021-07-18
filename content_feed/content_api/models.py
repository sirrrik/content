from __future__ import unicode_literals

from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='Images')