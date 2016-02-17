from .models import Registrado
from django.contrib import admin

# Register your models here.



class AdminRegistrado(admin.ModelAdmin):
	list_display = ["nombre", "timestamp"]
	class  Meta:
		model = Registrado 

admin.site.register(Registrado, AdminRegistrado)