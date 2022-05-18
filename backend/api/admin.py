from django.contrib import admin

# Register your models here.
from things.models import Thing

admin.site.register(Thing)
