from django import forms

from .models import Event, Client, Matrix, Sample, Document, Product, Service, Proposal

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
            "nickname",
            "address",
            "phone_fax",
            "cnpj",
            "email",
            "responsible_contact",
        ]

class MatrixForm(forms.ModelForm):

    class Meta:
        model = Matrix
        fields = [
            "description"
        ]

class SampleForm(forms.ModelForm):

    class Meta:
        model = Sample
        fields = [
            "description"
        ]

class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = [
            "description"
        ]

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            "description",
            "price",
        ]

class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = [
            "description",
            "price",
       ]

from django import forms
from .models import Proposal

class ProposalForm(forms.ModelForm):
    class Meta:
        model = Proposal
        fields = [
            "id",
            "client",
            "objective",
            "collection_date",
            "legal_basis",
            "services",
        ]
        widgets = {
            "collection_date": forms.DateInput(
                attrs={"type": "date", "class": "form-control"}
            ),
            "objective": forms.TextInput(attrs={"class": "form-control"}),
            "legal_basis": forms.TextInput(attrs={"class": "form-control"}),
            "client": forms.Select(attrs={"class": "form-control"}),
            "services": forms.SelectMultiple(attrs={"class":"form-control"}),
        }
        labels = {
            "client": "Cliente",
            "objective": "Objetivo",
            "collection_date": "Data de Coleta",
            "legal_basis": "Base Legal",
            "services":"Serviços",
        }
        help_texts = {
            "client": "Selecione o cliente associado à proposta.",
            "objective": "Informe o objetivo da proposta.",
            "collection_date": "Escolha a data de coleta.",
            "legal_basis": "Especifique a base legal relacionada.",
            "services": "Selecione um ou mais serviços para esta proposta."
        }
