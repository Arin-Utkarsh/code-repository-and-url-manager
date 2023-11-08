from django.contrib import admin

from .models import photo,category,urlClass,snippet_class

# Register your models here.

admin.site.register(category)

admin.site.register(photo)

admin.site.register(urlClass)

admin.site.register(snippet_class)

