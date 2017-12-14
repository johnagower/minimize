from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Timestamp(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
		
class Thing(Timestamp):
	def __unicode__(self):
		return self.name

	name = models.CharField(max_length=255)
	description = models.TextField()
	slug = models.SlugField(unique=True)
	user = models.ForeignKey(User, blank=True, null=True)
	active = models.BooleanField(default=True)

class ThingTag(models.Model):
	TAG_OPTIONS = (
		('gift', 'gift'),
		('seasonal', 'seasonal'),
		('inherited', 'inherited'),
		('clothing', 'clothing'),
		('shoes', 'shoes'),
		('furniture', 'furniture'),
	)
	tag = models.CharField(max_length=255,
		choices=TAG_OPTIONS)
	thing = models.ForeignKey(Thing,
		related_name="tags")
	# override the admin name
	class Meta:
		verbose_name_plural = "Tags"