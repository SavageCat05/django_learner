from django.urls import path
from . import views 

urlpatterns = [
    path("", views.write_review),
    path('thankyou', views.thankyou, name = "alpha"),
]