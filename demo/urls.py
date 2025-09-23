from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/start", views.start, name="start"),
    path("api/restart", views.restart, name="restart"),
    path("api/stop", views.stop, name="stop"),
    path("api/down", views.down, name="down"),
    path("api/logs", views.logs, name="logs"),
]
