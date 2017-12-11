from django import forms
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

class ContactForm(forms.Form):
	contact_name = forms.CharField()
	contact_email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea)