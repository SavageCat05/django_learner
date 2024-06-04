from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.starting_page, name="homepage"),
    path('post', views.post, name="all-posts"),
    path('post/<slug:slug>', views.selected_post, name="post-detail"),
]
