from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def write_review(request):
    if request.method == 'POST':
        entered_username = request.POST['username'] # this is the name = "" tag, the data is stored in a dictionary as key value pair 
        print(entered_username)
        return HttpResponseRedirect("all/thankyou")
    return render(request, "reviews/review.html")

def thankyou(request):
    print("yes, i was redirected !")
    return render(request, 'reviews/thankyou.html')