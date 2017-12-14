from django.contrib import admin
from inventory.models import Thing, ThingTag, BlogArticle

class ThingAdmin(admin.ModelAdmin):
	model = Thing
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

class ThingTagAdmin(admin.ModelAdmin):
	model = ThingTag
	list_display = ('tag',)

class BlogArticleAdmin(admin.ModelAdmin):
	model = BlogArticle
	list_display = ('title', 'description', 'content', 'slug',)


admin.site.register(Thing, ThingAdmin)
admin.site.register(ThingTag, ThingTagAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)