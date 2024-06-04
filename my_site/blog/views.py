from django.shortcuts import render

# Create your views here.

def starting_page(request):
    print("This will be printed")
    return render(request, 'blog/starting_page.html')

def post(request):
    return render(request, 'blog/all-posts.html')

def selected_post(request, slug):
    return render(request, 'blog/post-detail.html')