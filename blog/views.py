from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.utils import dateformat

from .models import Post, Tag



# def blog_home(request):
#     posts = Post.objects.order_by('-id')
#     return render(request, 'blog/blog_home.html',{'posts':posts})

class PostListView(ListView):
    queryset = Post.objects.published()
    context_object_name = 'posts'
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'tags': Tag.objects.all(),
        })
        return context

    def get_queryset(self):
        return Post.objects.order_by('-published_date')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


class PostListByTagView(ListView):
    context_object_name = 'posts'
    allow_empty = False
    template_name_suffix = '_list_by_tag'

    def get_queryset(self):
        return Post.objects.active().filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(PostListByTagView, self).get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context

