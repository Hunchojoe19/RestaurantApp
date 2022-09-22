from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse
from rest_framework import generics

from Restaurant.models import User
from Restaurant.serializer import UserSerializer


def home(request):
    return HttpResponse("Welcome to the Home Page")


def redirect(request):
    return HttpResponseRedirect(reverse('restaurant:home'))


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
