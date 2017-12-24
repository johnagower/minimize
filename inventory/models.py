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

	# helper method
	def get_absolute_url(self):
		return "things/%s/" % self.slug

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

class BlogArticle(Timestamp):
	title = models.CharField(max_length=60, blank=False, null=False)
	description = models.CharField(max_length=160)
	content = models.TextField()
	slug = models.SlugField(unique=True)

	# helper method
	def get_absolute_url(self):
		return "articles/%s/" % self.slug

# image model
def get_image_path(instance, filename):
	return '/' .join(['thing_images', instance.thing.slug, filename])

class Upload(Timestamp):
	thing = models.ForeignKey(Thing, related_name="uploads")
	image = models.ImageField(upload_to=get_image_path)