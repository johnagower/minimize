import datetime
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from inventory.models import BlogArticle

class BlogSitemap(Sitemap):
	changefreq = "weekly"
	priority = 0.5

	def items(self):
		return BlogArticle.objects.all()

	def lastmod(self, obj):
		return obj.updated

class StaticSitemap(Sitemap):
	lastmod = None
	priority = 0.5
	changefreq = "weekly"

	def items(self):
		return ['about', 'contact', 'browse', 'articles',]
	def location(self, item):
		return reverse(item)

class HomepageSitemap(Sitemap):
	priority = 1
	changefreq = "daily"

	def items(self):
		return ['home',]
	def lastmod(self, obj):
		return datetime.date.today()
	def location(self, item):
		return reverse(item)