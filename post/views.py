from http.client import HTTPResponse
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from post.models import Post, Category


def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts':posts,
        'categories':categories
    }
    return render(request, 'index.html', context = context)