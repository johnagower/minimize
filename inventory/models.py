from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

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

	def save(self, *args, **kwargs):
		# this is required when you override save functions
		super(Upload, self).save(*args, **kwargs)
		# check image size
		if self.image:
			image = Image.open(self.image)
			i_width, i_height = image.size
			max_size = (1000, 1000)

			if i_width > 1000:
				image.thumbnail(max_size, Image.ANTIALIAS)
				image.save(self.image.path)

class Questions(models.Model):
	def __unicode__(self):
		return self.question

	ANSWER_OPTIONS = (
		('open', 'open'),
		('radio', 'radio'),
		('checkbox', 'checkbox'),
		('number', 'number'),
		('truefalse', 'truefalse'),
	)
	question = models.CharField(max_length=255, blank=False, null=False)
	question_desc = models.CharField(max_length=255, blank=True, null=True)
	answer_type = models.CharField(max_length=255,
		choices=ANSWER_OPTIONS)
	class Meta:
		verbose_name_plural = "Questions"

class QuestionOptions(models.Model):
	question_id = models.ForeignKey(Questions, related_name="options")
	option = models.CharField (max_length=255, blank=False, null=False)
	class Meta:
		verbose_name_plural = "QuestionOptions"

class Item(Timestamp):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=255, blank=False, null=False)
	user = models.ForeignKey(User, blank=True, null=True)

	LASTUSED_OPTIONS = (
		('7', 'Past week'),
		('31', 'Past month'),
		('365', 'Past year'),
		('99999', 'More than a year ago'),
	)
	last_used = models.CharField(max_length=255, choices=LASTUSED_OPTIONS)
	REPLACEMENTCOST_OPTIONS = (
		('10', 'Less than $10'),
		('50', 'Less than $50'),
		('100', 'Less than $100'),
		('99999', 'More than $100'),
		('priceless', 'Priceless'),
	)
	replacement_cost = models.CharField(max_length=255, choices=REPLACEMENTCOST_OPTIONS)
	JOY_OPTIONS = (
		('none', 'None'),
		('some', 'Some'),
		('a lot', 'A lot'),
	)
	joy = models.CharField(max_length=255, choices=JOY_OPTIONS)
	DECISION_OPTIONS = (
		('keep', 'Keep'),
		('toss', 'Toss'),
		('donate', 'Donate'),
		('sell', 'Sell'),
		('digitize', 'Digitize'),
		('other', 'Something else'),
	)
	decision = models.CharField(max_length=255, choices=DECISION_OPTIONS)


class QuestionResponse(models.Model):
	RESULTS = (
		('keep', 'keep'),
		('let go', 'let go'),
		('more', 'more'),
	)
	item = models.ForeignKey(Item, related_name="responses")
	question = models.ForeignKey(Questions, related_name="responses")
	response = models.CharField (max_length=255, blank=False, null=False)
	result = models.CharField (max_length=255,
		choices=RESULTS)


