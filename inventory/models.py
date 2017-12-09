from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Thing(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(unique=True)
	user = models.ForeignKey(User, blank=True, null=True)
	active = models.BooleanField(default=True)