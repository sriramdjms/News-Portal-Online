from django.db import models
from django.contrib.auth.models import User
from datetime import date
gender_list=(("M","Male"),("F","Female"))

class personDetails(models.Model):
	name=models.CharField(max_length=50)
	email=models.CharField(max_length=70, null=True, blank=True, unique=True)
	phonenumber=models.CharField(max_length=10, null=True, blank=True)
	password = models.CharField(max_length=50,null=True, blank=True)

	def __str__self(self):
		return '%s' %(self.name)
