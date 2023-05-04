from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "description",
            "responsible_technician",
            "inital_date",
            "final_date",
        ]