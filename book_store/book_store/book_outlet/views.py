from django.shortcuts import render, get_object_or_404
from .models import book
from django.db.models import Avg

# Create your views here.
def mainpage(request):
    books = book.objects.all().order_by('rating')
    no_of_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request, 'book_outlet/index.html', {'books':books,
        'avg_rating':avg_rating,
        'no_of_books':no_of_books})

def book_detail(request, slug):
    # print("reaching here?")
    # is_book= book.objects.get(pk = id) #this will get the book which has primary key, ie an id 

    is_book = get_object_or_404(book, sluged_url = slug)
    return render(request, 'book_outlet/book_detail.html', {
        'title': is_book.title,
        'rating': is_book.rating,
        'author': is_book.author,
        'is_bestselling': is_book.best_selling 
    })