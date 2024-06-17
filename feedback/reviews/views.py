from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ReviewForm


# Create your views here.

def write_review(request):
    # if request.method == 'POST':
    #     # this is the name = "" tag, the data is stored in a dictionary as key value pair
    #     entered_username = request.POST['username']

    #     if entered_username == "":
    #         return render(request, "reviews/review.html", {"invalid_form": True})
    #     print(entered_username)
    #     redirected_path = reverse('alpha')
    #     return HttpResponseRedirect(redirected_path)
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            redirected_path = reverse("alpha")
            return HttpResponseRedirect(redirected_path)

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {'form':form})


def thankyou(request):
    print("yes, i was redirected !")
    return render(request, 'reviews/thankyou.html')
