from django.shortcuts import render
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