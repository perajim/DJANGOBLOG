from django import forms
from .models import Registrado

class RegistradoForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["email","nombre"]

	def clean_email(self):
		email =  (self.cleaned_data.get("email"))
		#if not "edu" in email:
			#raise forms.ValidationError("por favor utilize un email edu")
		#print (email )
		email_base, proovedor = email.split("@")
		dominio, extension = proovedor.split(".")
		if not extension == "edu":
			raise forms.ValidationError("utilize un correo edu")
		return email





class RegForm (forms.Form):
	nombre_form = forms.CharField(max_length=100)
	edad = forms.IntegerField()