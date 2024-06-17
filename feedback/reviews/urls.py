from django.urls import path
from . import views 

urlpatterns = [
    path("all", views.write_review),
    path('all/thankyou', views.thankyou, name = "alpha"),
]