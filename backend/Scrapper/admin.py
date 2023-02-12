from django.contrib import admin

# Register your models here.
from .models import *

class CrptoModelAdmin(admin.ModelAdmin):
    list_display = ('name','price')
    # pass

admin.site.register(Crypto, CrptoModelAdmin)