from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("detail/<int:mineral_id>/", views.detail, name="detail"),
	path("random/", views.random, name="random")
]