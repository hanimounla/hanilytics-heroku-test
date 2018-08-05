# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render ,redirect
import home.forms as my_forms 
import home.sqlite_connection as db
from home.models import Article

#region pages
def index(request):
    return render(request, 'index.html')

def tour(request):
    return render(request, 'pages/tour.html')

def blog(request):
    # articles = db.get_latest_articles(6)
    articles = Article.objects.order_by('-id')
    return render(request, 'blog/blog_home.html',{'articles':articles})

def about(request):
    return render(request, 'pages/about.html')

def case_studies(request):
    return render(request, 'case_studies/case_studies_home.html')

def view_article(request,urltitle = 'none'):
    article = Article.objects.get(url_title = request.path[14:])
    return render(request, 'blog/article_view.html',{'article':article})

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
#endregion

#region forms
#blog
def new_article(request):
    if request.method == 'POST':
        form = my_forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("blog")
    else:
        return render(request, 'blog/new_article.html', {
            'new_article_form': my_forms.ArticleForm()
})

def new_article_category(request):
    if request.method == 'POST':
        form = my_forms.ArticleCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog")
    return render(request, 'blog/new_category.html', {
            'new_category_form': my_forms.ArticleCategoryForm()
})

#case studies
def new_case_study(request):
    if request.method == 'POST':
        form = my_forms.CaseStudyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("case_studies")
    else:
        return render(request, 'blog/new_article.html', {
            'new_case_study_form': my_forms.CaseStudyForm()
})

#endregion
