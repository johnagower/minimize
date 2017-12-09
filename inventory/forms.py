from django.forms import ModelForm
from inventory.models import Thing

class ThingFormEdit(ModelForm):
	class Meta:
		model = Thing
		fields = ('name', 'description','active',)

class ThingFormCreate(ModelForm):
	class Meta:
		model = Thing
		fields = ('name', 'description',)
