from django.urls import path, include

from image_repository_app import views

urlpatterns = [
    path('', views.index)
]
