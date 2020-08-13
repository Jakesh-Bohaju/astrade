from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


# Register your models here.

class ASTAdmin(UserAdmin):
    pass


admin.site.register(Profile, ASTAdmin)
