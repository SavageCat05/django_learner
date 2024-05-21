from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
from django.template.loader import render_to_string

all_months = {
    "january": "Eat meat everyday for this month",
    "february": "Walk for atleast 20 minutes every day!",
    "march": "for everyday of this month, Aj mei udega!",
    "april": "for everyday of this month, Aj mei udega!",
    "may": "for everyday of this month, Aj mei udega!",
    "june": "for everyday of this month, Aj mei udega!",
    "july": "for everyday of this month, Aj mei udega!",
    "august": "for everyday of this month, Aj mei udega!",
    "september": "for everyday of this month, Aj mei udega!",
    "october": "for everyday of this month, Aj mei udega!",
    "november": "for everyday of this month, Aj mei udega!",
    "december": "for everyday of this month, Aj mei udega!",
}

# Create your views here.

# the challenge was when to call this index function and when will python know to call it


# def january(request):
#     return HttpResponse("Eat meat everyday for this month")  # line 2 above unstantiates this object("HttpResponse")

# def february(request):
#     return HttpResponse("Walk for atleast 20 minutes every day!")

# def december(request):
#     return

# search why month:str or month:int did not work !!
# def monthly_challenges(request, month):
#     challenge_status = None
#     if month == "january":
#         challenge_status = "Eat meat everyday for this month"
#     elif month == "february":
#         challenge_status = "Walk for atleast 20 minutes every day!"
#     elif month == "march":
#         challenge_status = "for everyday of this month, Aj mei udega!"
#     else:
#         return HttpResponseNotFound("Service is not supported for this month")
#     return HttpResponse(challenge_status)

def monthly_challenges(request, month):
    try:
        challenge_status = all_months[month]
        return HttpResponse(f"<h1>{challenge_status}</h1>")
    except:
        return HttpResponseNotFound("<h1>Not a valid month</h1>")

# def monthly_no_challenge(request, month):
#     return HttpResponse(month)


def monthly_no_challenge(request, month):
    if 1 <= month <= 12:
        months = list(all_months.keys())  # converting it to a list
        redirect_month = months[month-1]
        absolute_path = reverse("apple_potato", args = [redirect_month]) # Note:
        return HttpResponseRedirect(absolute_path)
    # an important factor is that exact wese ka wesa ana chahiye
    elif month > len(month):
        return HttpResponseNotFound("Not a valid month")

def get_list_of_months(dict_a:dict):
    str_a = "" 
    months = list(dict_a.keys())
    for i in range(1,len(months)):
        redirect_month = months[i-1]
        absolute_path = reverse("apple_potato", args = [redirect_month])
        str_a += f"<li><a href = '{absolute_path}'>{redirect_month}</a></li>"
    return str_a
    # correct the lower part!!

    # str_a = ""
    # for month in dict_a:
    #     str_a += f"<li><a href = \"{reverse("originalo", month)}\">{month}</a></li>"
    # return str_a

def index(request):

    response_str = f"""<ul>
    {get_list_of_months(all_months)}
    </ul>
    """
    # response_list = """<ul>
    # <li><a href = "/challenges/january">Wu shang clan</a></li>
    # </ul>"""
    return HttpResponse(response_str)

# def weekly_challenge(request):