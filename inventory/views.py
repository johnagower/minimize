from django.shortcuts import render, redirect
from inventory.forms import ThingForm
from inventory.models import Thing

# Create your views here.
def index(request):
	number = Thing.objects.count()
	things = Thing.objects.all()
	return render (request, 'index.html', {
		'number': number,
		'things': things
	})

def thing_detail(request, slug):
	thing = Thing.objects.get(slug=slug)
	return render (request, 'things/thing_detail.html', {
		'thing': thing,
	})

def edit_thing(request, slug):
	thing = Thing.objects.get(slug=slug)
	form_class = ThingForm
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=thing)
		if form.is_valid():
			form.save()
			return redirect('thing_detail', slug=thing.slug)
	else:
		form = form_class(instance=thing)
		
	return render(request, 'things/edit_thing.html', {
		'thing': thing,
		'form': form,
	})