from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
	def get_success_url(selt, request, user):
		return ('registration_create_thing')