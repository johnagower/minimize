from django.contrib import admin
from inventory.models import (
	Thing, 
	ThingTag, 
	BlogArticle, 
	Upload, 
	Questions, 
	QuestionOptions,
)

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

class QuestionsAdmin(admin.ModelAdmin):
	model = Questions
	list_display = ('question', 'question_desc', 'answer_type',)

class QuestionOptionsAdmin(admin.ModelAdmin):
	model = QuestionOptions
	list_display = ('question_id', 'option',)

admin.site.register(Thing, ThingAdmin)
admin.site.register(ThingTag, ThingTagAdmin)
admin.site.register(BlogArticle, BlogArticleAdmin)
admin.site.register(Upload, UploadAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(QuestionOptions, QuestionOptionsAdmin)