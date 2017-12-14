from django.contrib import admin
from inventory.models import Thing, ThingTag

class ThingAdmin(admin.ModelAdmin):
	model = Thing
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

class ThingTagAdmin(admin.ModelAdmin):
	model = ThingTag
	list_display = ('tag',)


admin.site.register(Thing, ThingAdmin)
admin.site.register(ThingTag, ThingTagAdmin)