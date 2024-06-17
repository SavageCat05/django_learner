from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import review
from django.views import View


# Create your views here.

## Creating a class based view: 

class reviewView(View):

    def get(self, request):

        form = ReviewForm()
        return render(request, "reviews/review.html", {'form':form})

    def post(self, request):
        form = ReviewForm(request.POST)

        # if the form is valid, then end ho jaega with a thankyou
        if form.is_valid():
            form.save()
            redirected_path = reverse("alpha")
            return HttpResponseRedirect(redirected_path)
        
        #if not valid, it will load the same form again, with pre-occupied data
        return render(request, "reviews/review.html", {'form':form})
            


# def write_review(request):
#     # if request.method == 'POST':
#     #     # this is the name = "" tag, the data is stored in a dictionary as key value pair
#     #     entered_username = request.POST['username']

#     #     if entered_username == "":
#     #         return render(request, "reviews/review.html", {"invalid_form": True})
#     #     print(entered_username)
#     #     redirected_path = reverse('alpha')
#     #     return HttpResponseRedirect(redirected_path)

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             #3rd and last edit 
#             form.save() # this is only possible since we have ModelForm 

#             # 2nd edit
#             # print(form.cleaned_data)
#             # some_var = review(
#             #     username = form.cleaned_data['username'],
#             #     password = form.cleaned_data['password'],
#             #     your_review = form.cleaned_data['your_review'],
#             #     rating = form.cleaned_data['rating'])
#             # some_var.save()

#             # 1st edit
#             # some_var = review(
#             #     username = form.cleaned_data['user_name'],
#             #     password = form.cleaned_data['password'],
#             #     your_review = form.cleaned_data['review_text'],
#             #     rating = form.cleaned_data['rating'])
#             # some_var.save()

#             redirected_path = reverse("alpha")
#             return HttpResponseRedirect(redirected_path)

#     else:
#         form = ReviewForm()

#     return render(request, "reviews/review.html", {'form':form})


def thankyou(request):
    print("yes, i was redirected !")
    return render(request, 'reviews/thankyou.html')
