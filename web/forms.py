from django import forms

from .models import Event, Client

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "description",
            "responsible_technician",
            "inital_date",
            "final_date",
        ]

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "corporate_name",
            "address",
            "phone_fax",
            "cnpj",
            "email",
            "responsible_contact",
        ]