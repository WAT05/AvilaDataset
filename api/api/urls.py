from django.urls import path
from predictor.templates import views

urlpatterns = [
    path("", views.get, name="home"),
    path('classify/', views.get, name="home")
]
