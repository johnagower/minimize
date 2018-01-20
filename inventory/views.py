from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.template import Context
from django.core.mail import EmailMessage, mail_admins
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from inventory.forms import (
	ThingFormEdit, 
	ThingFormCreate, 
	ContactForm, 
	ThingUploadForm,
	EditUserForm,
	ItemForm
	)
from inventory.models import Thing, BlogArticle, Upload

# Create your views here.
def index(request):	
	form_class = ItemForm
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			item = form.save(commit=False)
			item.user = request.user
			item.save()
			return redirect('home')
	else:
		form = form_class()
	return render(request, 'index.html', {
		'form': form,
	})

def blog_article(request, slug):
	# grab article
	article = BlogArticle.objects.get(slug=slug)
	# pass to template
	return render (request, 'articles/single_article.html', {
		'article': article,
	})

def articles_home(request):
	articles = BlogArticle.objects.all().order_by('title')
	return render (request, 'articles/articles.html', {
		'articles': articles,
	})

@login_required
def thing_detail(request, slug):
	# grab object
	thing = Thing.objects.get(slug=slug)
	# grab tags
	tags = thing.tags.all()
	# grab associated images
	uploads = thing.uploads.all()

	if (not request.user.is_superuser and thing.user != request.user):
		raise Http404
	# pass to template
	return render (request, 'things/thing_detail.html', {
		'thing': thing,
		'tags': tags,
		'uploads': uploads,
	})

@login_required
def edit_thing(request, slug):
	thing = Thing.objects.get(slug=slug)
	uploads = thing.uploads.all()
	if thing.user != request.user:
		raise Http404
	form_class = ThingFormEdit
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=thing)
		if form.is_valid():
			form.save()
			messages.success(request, 'Details updated.')
			return redirect('thing_detail', slug=thing.slug)
	else:
		form = form_class(instance=thing)

	return render(request, 'things/edit_thing.html', {
		'thing': thing,
		'form': form,
		'uploads': uploads,
	})

@login_required
def edit_thing_uploads(request, slug):
	# grab the object
	thing = Thing.objects.get(slug=slug)
	if thing.user != request.user:
		raise Http404
	
	# set the form
	form_class = ThingUploadForm

	# if coming from a submitted form
	if request.method == 'POST':
		#grab the data from the submitted form
		form = form_class(data=request.POST,
			files=request.FILES, instance=thing)

		if form.is_valid():
			# create a new object from the submitted form
			Upload.objects.create(
				image=form.cleaned_data['image'],
				thing=thing,
			)

			return redirect('edit_thing_uploads', slug=thing.slug)

	# otherwise just create the form
	else:
		form = form_class(instance=thing)

	# grab all the objects images
	uploads = thing.uploads.all()

	# and render the template
	return render(request, 'things/edit_thing_uploads.html', {
		'thing': thing,
		'form': form,
		'uploads': uploads,
	})

@login_required
def delete_upload(request, id):
	# grab the image
	upload = Upload.objects.get(id=id)
	# security check
	if upload.thing.user != request.user:
		raise Http404
	# delete the image
	upload.delete()
	# refresh the edit page
	return redirect('edit_thing_uploads', slug=upload.thing.slug)

@login_required
def create_thing(request):
	form_class = ThingFormCreate
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			thing = form.save(commit=False)
			thing.user = request.user
			thing.slug = slugify(thing.name)
			thing.save()
			request.session["new_thing"] = thing.name
			return redirect('home')
			mail_admins("New thing added", "Someone added a new thing")
	else:
		form = form_class()
	return render(request, 'things/create_thing.html', {
		'form': form,
	})

@login_required
def browse_by_name(request, initial=None):
	number = Thing.objects.filter(user__exact=request.user).count()
	if initial:
		things = Thing.objects.filter(user__exact=request.user).filter(
			name__istartswith=initial).order_by('name')
	else:
		things = Thing.objects.filter(user__exact=request.user).order_by('name')
	return render(request, 'search/search.html', {
		'things': things,
		'initial': initial
	})

def contact(request):
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			contact_name = form.cleaned_data['contact_name']
			contact_email = form.cleaned_data['contact_email']
			form_content = form.cleaned_data['content']

			# email the profile with the contact info
			template = get_template('contact_template.txt')

			context = Context({
				'contact_name': contact_name,
				'contact_email': contact_email,
				'form_content': form_content,
			})
			content = template.render(context)

			email = EmailMessage(
				'New contact form submission',
				content,
				'Your website <hi@minimizeapp.com>',
				['johnagower@gmail.com'],
				headers = {'Reply-To': contact_email }
			)
			email.send()
			return redirect('contact')

	return render(request, 'contact.html', {
		'form': form_class
	})

@login_required
def edit_user(request):
	user = request.user
	form_class = EditUserForm

	if request.method == 'POST':
		form = form_class(data=request.POST, instance=user)
		if form.is_valid():
			form.save()
			messages.success(request, 'User settings updated.')
			return redirect('home')

	else:
		form = form_class(instance=user)

	return render(request, 'account_settings.html', {
		'form': form,
	})
