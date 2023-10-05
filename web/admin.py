from django.contrib import admin
from .models import Event, OtherDocuments, EnvironmentalConsultancy, Client , Matrix

"""Admin class to customize class's models."""
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_display_links = ("description",)
    search_fields = ("description",)

@admin.register(OtherDocuments)
class OtherDocumentsAdmin(admin.ModelAdmin):
    list_display = (
        "description",
        "registration_number",
    )
    list_display_links = ("description",)
    search_fields = ("description",)

@admin.register(EnvironmentalConsultancy)
class EnvironmentalConsultancyAdmin(admin.ModelAdmin):
    list_display = ("corporate_name",)
    list_display_links = ("corporate_name",)
    search_fields = ("corporate_name",)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        "corporate_name",
        "responsible_contact",
    )
    list_display_links = ("corporate_name",)
    search_fields = ("corporate_name",)

@admin.register(Event)
class MatrixAdmin(admin.ModelAdmin):
    list_display = ("description",)
    list_display_links = ("description",)
    search_fields = ("description",)
