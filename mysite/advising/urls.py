from django.urls import path

from . import views

urlpatterns = [
    path('submit/', views.submit_advising, name='submit_advising'),
    path('view/', views.view_advising, name='view_advising'),
    path('view_faculty/', views.view_advising_faculty, name='view_advising_faculty'),
]