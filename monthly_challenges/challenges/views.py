from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# the challenge was when to call this index function and when will python know to call it


# def january(request):
#     return HttpResponse("Eat meat everyday for this month")  # line 2 above unstantiates this object("HttpResponse")

# def february(request):
#     return HttpResponse("Walk for atleast 20 minutes every day!")

def monthly_challenges(reuest, month):
    challenge_status = None
    if month == "january":
        challenge_status = "Eat meat everyday for this month"
    elif month == "february":
        challenge_status = "Walk for atleast 20 minutes every day!"
    elif month == "march":
        challenge_status = "for everyday of this month, Aj mei udega!"
    else:
        challenge_status = "Service is not supported for this month"
    return challenge_status
