from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from . models import *

class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super(VenueForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})