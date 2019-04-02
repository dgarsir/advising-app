from django.urls import path

from . import views

urlpatterns = [
    path('advising/', views.submit_advising, name='submit_advising')
]