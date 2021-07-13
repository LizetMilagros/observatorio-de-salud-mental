from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class userSuscription(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email']
		exclude = ('password1', 'password2',)
		help_texts = {k:"" for k in fields }