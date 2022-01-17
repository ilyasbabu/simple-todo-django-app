# from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    # path('', view, name='view'),          #function based view
    path('',TaskListView.as_view(),name='TaskListView'),  #generic class based view
    path('add/', add, name='add'),  
    path('done/<int:task_id>',done,name='done'),
    path('update/<int:task_id>',update,name="update"),
    path('<pk>/',TaskDetailView.as_view(),name='TaskDetailView'),
    path('<pk>/update/',TaskUpdateView.as_view(),name='TaskUpdateView'),
    path('<pk>/delete/',TaskDeleteView.as_view(),name='TaskDeleteView'),
    
]