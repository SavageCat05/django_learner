from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from .forms import profile_form
from .models import UserProfile

# Create your views here.


class CreateProfileView(CreateView):
    template = "profiles/create_profile.html"
    model = UserProfile
    fields = '__all__'
    success_url = '/profiles'


# class CreateProfileView(View):
#     def get(self, request):
#         form = profile_form()
#         return render(request, "profiles/create_profile.html", {
#             'form':form
#         })

#     def post(self, request):
#         submitted_form = profile_form(request.POST, request.FILES['image'])
        
#         if submitted_form.is_valid():
#             profile = UserProfile(image = request.FILES)
#             profile.save()
#             # store_file(request.FILES["image"])
#             return HttpResponseRedirect("profiles")
        
#         return render(request, "profiles/create_profile.html", {
#             'form':submitted_form
#         })
    