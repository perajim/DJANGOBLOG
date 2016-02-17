from django.shortcuts import render
from .forms import RegForm
# Create your views here.

def inicio(request):
	form = RegForm(request.POST or None)
	context = {
		"form" : form 
	}
	if form.is_valid():
	   form_dicc= (form.cleaned_data)
	   print (form_dicc.get("nombre"))
	return render(request, "inicio.html", context)
