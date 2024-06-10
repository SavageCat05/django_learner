from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.mainpage),
    path('<slug:slug>', views.book_detail, name='page_detail')
]