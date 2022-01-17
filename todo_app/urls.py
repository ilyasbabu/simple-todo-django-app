# from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', view, name='view'),
    path('done/<int:task_id>',done,name='done'),
    path('update/<int:task_id>',update,name="update"),
]