from django.urls import path, include, re_path

from image_repository_app import views

urlpatterns = [
    path('', views.index),
    path('search/<str:query>/', views.search),
    path('test/image_repository_app', views.run_tests),
]
