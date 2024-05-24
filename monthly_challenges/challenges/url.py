from django.urls import path
# this syntax means that from the same folder as urls.py files i.e(challenges), import this!!
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:month>", views.monthly_challenges, name="apple_potato"),
]
