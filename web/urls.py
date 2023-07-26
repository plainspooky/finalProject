from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event-list"),
    path("event/new", views.EventCreateView.as_view(), name="event-create"),
    path(
        "event/<int:pk>/edit",
        views.EventUpdateView.as_view(),
        name="event-update",
    ),
    path(
        "event/<int:pk>/delete",
        views.EventDeleteView.as_view(),
        name="event-delete",
    ),
    path("client", views.ClientListView.as_view(), name="client-list"),
    path("client/new", views.ClientCreateView.as_view(), name="client-create"),
    path(
        "client/<int:pk>/edit",
        views.ClientUpdateView.as_view(),
        name="client-update",
    ),
    path(
        "client/<int:pk>/delete",
        views.ClientDeleteView.as_view(),
        name="client-delete",
    ),

]