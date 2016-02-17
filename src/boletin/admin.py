from .models import Registrado
from django.contrib import admin
from .forms import RegistradoForm
# Register your models here.



class AdminRegistrado(admin.ModelAdmin):
	list_display = ["nombre","email" , "timestamp"]
	form = RegistradoForm
	#class  Meta:
		#model = Registrado 

admin.site.register(Registrado, AdminRegistrado)