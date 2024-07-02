from django.urls import path, include
from . import views

urlpatterns = [
    path('homepage', views.saved_tasks, name="homepage"),
    path('add_task', views.add_taskView.as_view(), name="add_task"),
    path('remove_task/<int:pk>', views.remove_taskView.as_view(), name = "remove_task"),
    path('sign_up', views.sign_upView.as_view(), name = "sign_up"),
    path('', views.login_userView.as_view(), name = "frontpage"),
    path('logout_user', views.logout_user, name = "logout"),
]

# urlpatterns = [
#     path('homepage', views.saved_tasks, name="homepage"),
#     path('add_task', views.add_task, name="add_task"),
#     path('remove_task/<int:id>', views.remove_task, name = "remove_task"),
#     path('sign_up', views.sign_up, name = "sign_up"),
#     path('', views.login_user, name = "frontpage"),
#     path('logout_user', views.logout_user, name = "logout"),
# ]
