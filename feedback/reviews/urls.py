from django.urls import path
from . import views 

urlpatterns = [
    # path("", views.write_review),
    path("", views.reviewView.as_view()),
    path("thankyou", views.thankyouView.as_view(), name = "alpha"),
    # path('thankyou', views.thankyou, name = "alpha"),
    # path('checks', views.get_review_items),
    path('reviews/favorite', views.AddFavoriteView.as_view()),
    path('checks', views.list_of_items.as_view()),
    path('detail/<int:pk>', views.single_pageView.as_view(), name = "more_detail"),
]