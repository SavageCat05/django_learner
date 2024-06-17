from django.urls import path
from . import views 

urlpatterns = [
    # path("", views.write_review),
    path("", views.reviewView.as_view()),
    path('thankyou', views.thankyou, name = "alpha"),
]