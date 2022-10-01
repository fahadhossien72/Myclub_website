from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(MyclubUser)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')
    ordering = ('phone', 'name')
    search_fields = ('name', 'address')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'manager', 'event_date')
    list_filter = ('event_date', 'venue')
    
