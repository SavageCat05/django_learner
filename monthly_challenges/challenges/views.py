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
    "november": None,
    "december": None,
}



def monthly_challenges(request, month):
    try:
        challenge_status = all_months[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_status, "mymonth": month
        })
    except:
        no_response = render_to_string('404.html')
        return HttpResponseNotFound(no_response)


def get_list_of_months(dict_a: dict):
    str_a = ""
    months = list(dict_a.keys())
    for i in range(1, len(months)):
        redirect_month = months[i-1]
        absolute_path = reverse("apple_potato", args=[redirect_month])
        str_a += f"<li><a href = '{absolute_path}'>{redirect_month}</a></li>"
    return HttpResponse(str_a)


def index(request):
    months = list(all_months.keys())
    return render(request, "challenges/index.html", {"list_of_months": months})

def month_challenge_by_number(request, month):
    months = list(all_months.keys())

    if month>len(months):
        return HttpResponse("Invalid Month")
    
    redirected_month = month[month - 1]
    redirect_path = reverse('apple_potato', arg = [redirected_month])
    return HttpResponseRedirect(redirect_path)