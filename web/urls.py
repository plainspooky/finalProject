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
    path("matrix", views.MatrixListView.as_view(), name="matrix-list"),
    path("matrix/new", views.MatrixCreateView.as_view(), name="matrix-create"),
    path(
        "matrix/<int:pk>/edit",
        views.MatrixUpdateView.as_view(),
        name="matrix-update",
    ),
    path(
        "matrix/<int:pk>/delete",
        views.MatrixDeleteView.as_view(),
        name="matrix-delete",
    ),
path("sample", views.SampleListView.as_view(), name="sample-list"),
    path("sample/new", views.SampleCreateView.as_view(), name="sample-create"),
    path(
        "sample/<int:pk>/edit",
        views.SampleUpdateView.as_view(),
        name="sample-update",
    ),
    path(
        "sample/<int:pk>/delete",
        views.SampleDeleteView.as_view(),
        name="sample-delete",
    ),
]