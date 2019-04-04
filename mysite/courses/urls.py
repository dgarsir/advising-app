from django.urls import path
from . import views

urlpatterns=[
	path('courses/',views.courses_add,name='courses_add')
]