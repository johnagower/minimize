from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from inventory.models import Thing, Upload, Item

class ThingFormEdit(ModelForm):
	class Meta:
		model = Thing
		fields = ('name', 'description','active',)

class ThingUploadForm(ModelForm):
	class Meta:
		model = Upload
		fields = ('image',)

class ThingFormCreate(ModelForm):
	class Meta:
		model = Thing
		fields = ('name', 'description',)

class ContactForm(forms.Form):
	contact_name = forms.CharField(required=True)
	contact_email = forms.EmailField(required=True)
	content = forms.CharField(
		required=True,
		widget=forms.Textarea
	)

	def __init__(self, *args, **kwargs):
		super(ContactForm, self).__init__(*args, **kwargs)
		self.fields['contact_name'].label = "Your name:"
		self.fields['contact_email'].label = "Your email:"
		self.fields['content'].label = "What do you want to say?"

class EditUserForm(ModelForm):
	class Meta:
		model = User
		fields = ('email',)

class ItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ['name', 'last_used', 'replacement_cost', 'joy', 'decision',]
		labels = {
		    'name': ('What\'s the item?'),
		    'last_used': ('When did you use it last?'),
		    'replacement_cost': ('How much would it cost to replace?'),
		    'joy': ('Does it bring you joy?'),
		    'decision': ('What will you do with it?')
		}