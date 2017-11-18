# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Baike(models.Model):
    url = models.TextField()
    name = models.TextField()
    text = models.TextField()
