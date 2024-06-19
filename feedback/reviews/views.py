from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView


# Create your views here.

## Creating a class based view: 

# class reviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thankyou"


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


# def thankyou(request):
#     print("yes, i was redirected !")
#     return render(request, 'reviews/thankyou.html')


# class thankyouView(View):
#     def get(self, request):
#         return render(request, 'reviews/thankyou.html')
    
# instead of doing this we can avoid the process completely and use class-inheritence property


class thankyouView(TemplateView):

    # def get(self, request):
    #     return render(request, 'reviews/thankyou.html')

    template_name = 'reviews/thankyou.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'if it works?'
        return context
    

def get_review_items(request):

    review_list = review.objects.all()
    return render(request, 'reviews/review_list.html', {
        'review_list': review_list
    })
    

class list_of_items(ListView):
    # print("Watashi wa kawai?")
    template_name = "reviews/review_list.html"
    model = review
    # print("Watashi wa kawai?")

    # context_object_name = "review_list"

    # print("Watashi wa kawai?")
    # def get_queryset(self):
    #     base_query = super().get_queryset()
    #     print_me = base_query.filter(rating = 5)
    #     return print_me
    # print("Watashi wa kawai?")


# class single_pageView(TemplateView):
#     template_name = "reviews/single_page.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs['id']
#         context['plot'] = review.objects.get(pk = review_id)
#         return context


class single_pageView(DetailView):
    template_name = "reviews/single_page.html"
    model = review


class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST['review_id']
        fav_review = review.objects.all(review_id)
        request.session["favorite_review"] = fav_review
        return HttpResponseRedirect("/reviews/"+ review_id)