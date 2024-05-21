from django.urls import path
# this syntax means that from the same folder as urls.py files i.e(challenges), import this!!
from . import views

urlpatterns = [
     # this is done to have a main page where we get list of options of what months we can choose from 
    # this will be used in case for /challenge/ as there is nothing after this!
    path("", views.index),
    path("<int:month>", views.monthly_no_challenge),
    path("<str:month>", views.monthly_challenges, name="apple_potato"),
    path("aim", views.weekly_challenge)
]
