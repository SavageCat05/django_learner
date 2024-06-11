from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[0:3]
    return render(request, 'blog/starting_page.html', {'latest_posts':latest_posts})


def post(request):
    latest_posts = Post.objects.all().order_by("-date")
    return render(request, 'blog/all-posts.html', {'latest_posts':latest_posts})

def selected_post(request, slug):
    identified_post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/post-detail.html', {
        'post':identified_post
    })



    # {
    #     "slug": "hike-in-the-mountains",
    #     "image": "mountains.jpg",
    #     "author": "Anshuman",
    #     "date": date(2021, 7, 21),
    #     "title": "Mountain Hiking",
    #     "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # },
    # {
    #     "slug": "programming-is-fun",
    #     "image": "coding.jpg",
    #     "author": "Anshuman",
    #     "date": date(2022, 3, 10),
    #     "title": "Programming Is Great!",
    #     "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # },
    # {
    #     "slug": "into-the-woods",
    #     "image": "woods.jpg",
    #     "author": "Anshuman",
    #     "date": date(2020, 8, 5),
    #     "title": "Nature At Its Best",
    #     "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
    #     "content": """
    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

    #       Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
    #       aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
    #       velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
    #     """
    # }