# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,redirect

from blog.models import Post




def index(request):
    posts = Post.objects.order_by('-id')[:3]
    return render(request, 'index.html' , {'posts':posts})

def tour(request):
    return render(request, 'pages/tour.html')

def about(request):
    return render(request, 'pages/about.html')

#region samples
def basic_grid(request):
    return render(request, 'example_pages/basic_grid.html')

def full_width(request):
    return render(request, 'example_pages/full_width.html')

def gallery(request):
    return render(request, 'example_pages/gallery.html')

def sidebar_left(request):
    return render(request, 'example_pages/sidebar_left.html')

def sidebar_right(request):
    return render(request, 'example_pages/sidebar_right.html')
#endregion
