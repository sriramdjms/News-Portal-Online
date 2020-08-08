from django.contrib import admin
# Register your models here.
from .models import personDetails
class personAdmin(admin.ModelAdmin):
	list_display=('name','email','phonenumber','password')
admin.site.register(personDetails,personAdmin)
