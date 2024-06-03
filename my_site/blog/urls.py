from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.starting_page),
    path('post', views.post),
    path('post/<slug>', views.selected_post),
]
