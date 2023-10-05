from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .models import Event, Client, Matrix
from .forms import EventForm, ClientForm


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

class EventUpdateView(EventViewMixin, UpdateView):
    ...
class EventView(EventViewMixin, DeleteRecordMixin, DeleteView):
    ...

class EventDeleteView(EventViewMixin, DeleteRecordMixin, DeleteView):
    ...



class ClientViewMixin:
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("client-list")


class ClientCreateView(ClientViewMixin, CreateView):
    ...


class ClientListView(ClientViewMixin, ListView):
    ...

class ClientUpdateView(ClientViewMixin, UpdateView):
    ...
class ClientView(ClientViewMixin, DeleteRecordMixin, DeleteView):
    ...

class ClientDeleteView(ClientViewMixin, DeleteRecordMixin, DeleteView):
    ...


class MatrixViewMixin:
    model = Matrix
    form_class = MatrixForm
    success_url = reverse_lazy("matrix-list")


class MatrixCreateView(MatrixViewMixin, CreateView):
    ...


class MatrixListView(MatrixViewMixin, ListView):
    ...

class MatrixUpdateView(MatrixViewMixin, UpdateView):
    ...
class MatrixView(MatrixViewMixin, DeleteRecordMixin, DeleteView):
    ...

class MatrixDeleteView(MatrixViewMixin, DeleteRecordMixin, DeleteView):
    ...