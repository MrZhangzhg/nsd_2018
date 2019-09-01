from django.contrib import admin
from .models import Group, Host, Module, Arg

# Register your models here.
for item in [Group, Host, Module, Arg]:
    admin.site.register(item)

