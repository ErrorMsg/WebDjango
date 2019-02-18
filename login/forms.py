from django import forms

class UserForm(forms.Form):
	username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={"class":"form-control"}))
	password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={"class":"form-control"}))
	
class RegisterForm(forms.Form):
	SEX_CHOICES = (
		(1, "male"),
		(2, "female"),
	)
	username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={"class":"form-control"}))
	password1 = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput(attrs={"class":"form-control"}))
	password2 = forms.CharField(label="Confirm Password", max_length=256, widget=forms.PasswordInput(attrs={"class":"form-control"}))
	email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class":"form-control"}))
	sex = forms.ChoiceField(label="Sex", choices=SEX_CHOICES)
	
class AuthForm(forms.Form):
	username = forms.CharField(label="Username", max_length=128, widget=forms.TextInput(attrs={"class":"form-control"}))
	email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={"class":"form-control"}))
	
class ResetForm(forms.Form):
	password0 = forms.CharField(label="Current password", max_length=256, widget=forms.PasswordInput(attrs={"class":"form-control"}))
	password1 = forms.CharField(label="New password", max_length=256, widget=forms.PasswordInput(attrs={"class":"form-control"}))
	password2 = forms.CharField(label="Confirm new password", max_length=256, widget=forms.PasswordInput(attrs={"class":"form-control"}))
	
