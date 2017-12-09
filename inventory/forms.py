from django.forms import ModelForm
from inventory.models import Thing

class ThingForm(ModelForm):
	class Meta:
		model = Thing
		fields = ('name', 'description', 'active',)
