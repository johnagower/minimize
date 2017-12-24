from django.contrib import admin
from inventory.models import Thing, ThingTag, BlogArticle, Upload

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

# uploaded images
class UploadAdmin(admin.ModelAdmin):
	list_display = ('thing',)
	list_display_links = ('thing',)


admin.site.register(Thing, ThingAdmin)
admin.site.register(ThingTag, ThingTagAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(Upload, UploadAdmin)