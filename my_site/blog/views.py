from django.shortcuts import render

# Create your views here.

def starting_page(request):
    print("This will be printed")
    return render(request, 'blog/starting_page.html')

def post(request):
    pass

def selected_post(request):
    pass