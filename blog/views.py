from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    # we will pass the data in the dictionary
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
