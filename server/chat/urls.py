from django.urls import path

from . import views

urlpatterns = [
    path("", views.room_list, name="rooms_list"),
    path("<slug:slug>/", views.room_detail, name="room_detail"),
]