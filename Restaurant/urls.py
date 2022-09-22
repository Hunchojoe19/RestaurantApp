from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('users/', views.UserList.as_view(), name="user-list"),
    path('users/<int:pk>/', views.UserDetails.as_view(), name="user-details")
]
