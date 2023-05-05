from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Event
from .forms import EventForm


class DeleteRecordMixin:

    def post(self, request, pk):
        record = get_object_or_404(self.model, pk=pk)
        record.delete()

        return redirect(self.success_url)


class EventViewMixin:
    model = Event
    form_class = EventForm
    success_url = reverse_lazy("event-list")


class EventCreateView(EventViewMixin, CreateView):
    ...


class EventListView(EventViewMixin, ListView):
    ...


class EventView(EventViewMixin, DeleteRecordMixin, DeleteView):
    ...
