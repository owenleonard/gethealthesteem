from django.contrib import admin
from website.models import SubService, Service, Event, Content

# Register your models here.
admin.site.register(SubService)
admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Content)