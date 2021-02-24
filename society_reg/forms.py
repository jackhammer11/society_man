from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateSocietyForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','password1','password2']

class SocietyForm(ModelForm):
	class Meta:
		model = Visitor
		fields = '__all__'
