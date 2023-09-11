from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator

from .models import User


class RegisterUserForm(UserCreationForm):

	#https://stackoverflow.com/questions/63524243/how-do-i-add-phone-number-field-to-django-usercreationform
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+2567....'. Up to 15 digits allowed.")

	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	phone_number = forms.CharField(validators=[phone_regex], required=True, max_length=17)
	business_name = forms.CharField(required=True)
	business_location = forms.CharField(required=True)
	business_website = forms.CharField(max_length=250, required=False)

	class Meta:
		model = User
		fields = ("first_name", "last_name", "email", "password1", "password2", "phone_number", "business_name", "business_location", "business_website")

	def save(self, commit=True):
		user = super(RegisterUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user