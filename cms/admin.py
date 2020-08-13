from django.contrib import admin
from .models import *


# Register your models here.

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(FrontHeader)
admin.site.register(Banner)
admin.site.register(Page, PageAdmin)
admin.site.register(ContactUs)
admin.site.register(AboutUs)
admin.site.register(Services)
admin.site.register(FestivalGreeting)
admin.site.register(OpeningClosingDetail)
admin.site.register(WelcomeMessage)
