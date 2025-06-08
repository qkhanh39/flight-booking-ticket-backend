from django.urls import path
from flight import views

urlpatterns = [
    path("airports/", views.AirportListView.as_view()),
    path("airports/create/", views.AirportCreateView.as_view())
]
