from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *
class UserForm(ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))



	class Meta:
	    model = User
	    fields = ('username', 'email', 'password')

class ContactUsForm(ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile'}))
	comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20,'class':'form-control','placeholder':'Comment Here'}))




	class Meta:
	    model = ContactUs
	    fields = ('name', 'email', 'mobile','comment')