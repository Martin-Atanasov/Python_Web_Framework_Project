from django.contrib import admin

#from templates_advanced.models import
from book.models import Kids, Memory

admin.site.register(Kids)
admin.site.register(Memory)