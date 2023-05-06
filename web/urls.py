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
]