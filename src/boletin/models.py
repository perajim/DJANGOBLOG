from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Registrado(models.Model):
	nombre = models.CharField(max_length=120)
	email = models.EmailField()
	codigo_postal = models.IntegerField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	actualizado = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __str__(self):
		return self.email