from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import task_loader, sign_in
from django.urls import reverse, reverse_lazy
from .forms import Input_form, Sign_up
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.views.generic.edit import FormView, DeleteView
# Create your views here.


def saved_tasks(request):
    try:
        if (task_loader.objects.all()):
            all_tasks = task_loader.objects.filter(user=request.user)
            return render(request, 'task/homepage.html', {'all_tasks': all_tasks})
        else:
            redirected_path = reverse('add_task')
            return HttpResponseRedirect(redirected_path)
    except:
        redirected_path = reverse('add_task')
        return HttpResponseRedirect(redirected_path)

# this will redirect to add_task page to give user prompt


class add_taskView(FormView):
    template_name = "task/task_adder.html"
    form_class = Input_form
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = self.request.user
        task = form.save(commit=False)
        task.user = user
        task.save()
        return super(add_taskView, self).form_valid(form)


# def add_task(request):
#     if request.method == 'POST':
#         form = Input_form(request.POST)
#         if form.is_valid():
#             who_is_online = request.user
#             task_title = form.cleaned_data['task_title']
#             task_priority = form.cleaned_data['task_priority']
#             task_due_date = form.cleaned_data['task_due_date']
#             task_detail = form.cleaned_data['task_detail']
#             print(task_title)
#             task_loader.objects.create(user = who_is_online, task_title = task_title, task_priority = task_priority,task_due_date = task_due_date ,task_detail = task_detail)
#             redirected_path = reverse('homepage')
#             return HttpResponseRedirect(redirected_path)
#     else:
#         form = Input_form()
#     return render(request, 'task/task_adder.html', {'form':form})


# def remove_task(request, id):
#     task_loader.objects.filter(pk=id).delete()
#     return redirect('homepage')

class remove_taskView(DeleteView):
    model = task_loader
    success_url = reverse_lazy("homepage")

# def remove_task(request, id):
#     task_loader.objects.filter(pk=id).delete()
#     return redirect('homepage')


class sign_upView(View):
    def get(self, request):
        form = Sign_up()
        return render(request, 'task/sign_up.html', {'form': form})

    def post(self, request):
        form = Sign_up(request.POST)
        if form.is_valid():
            user1 = form.save()
            print(user1)
            print("i was here")
            print(user1.id)
            print(user1.first_name)
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            sign_in.objects.create(
                Username=user1, phone=phone, address=address)
            print(phone)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('homepage')

# def sign_up(request):
#     if request.method == 'POST':
#         form = Sign_up(request.POST)
#         if form.is_valid():
#             user1 = form.save()
#             print(user1)
#             print("i was here")
#             print(user1.id)
#             print(user1.first_name)
#             phone = form.cleaned_data['phone']
#             address = form.cleaned_data['address']
#             sign_in.objects.create(Username = user1, phone = phone, address = address )
#             print(phone)

#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('homepage')
#     else:
#         form = Sign_up()
#     return render(request, 'task/sign_up.html', {'form':form})


# def login_user(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('homepage')
#         else:
#             messages.success(request, ("there is no such user! please check your details again!"))
#             return redirect('frontpage')
#     else:
#         return render(request, 'task/front_page.html')

class login_userView(View):
    def get(self, request):
        return render(request, 'task/front_page.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.success(
                request, ("there is no such user! please check your details again!"))
            return redirect('frontpage')


def logout_user(request):
    logout(request)
    messages.success(request, ("You have logged out of your account!"))
    return redirect('frontpage')
