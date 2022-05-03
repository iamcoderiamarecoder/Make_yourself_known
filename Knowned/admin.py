from django.contrib import admin

# Register your models here.
from .models import About, investors

admin.site.register(investors)
admin.site.register(About)