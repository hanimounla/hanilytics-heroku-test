from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
import home.views as views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tour/', views.tour, name='tour'),
    url(r'^about/',views.about, name = 'about'),
    
    #blog
    url(r'^blog/$', views.blog, name = 'blog'),
    url(r'^blog/new-article$', views.new_article, name = 'new_article'),
    url(r'^blog/new-category$', views.new_article_category, name = 'new_article_category'),
    url(r'^blog/article/(?P<urltitle>)', views.view_article, name = 'view_article'),

    #case studies
    url(r'^case-studies/$', views.case_studies, name = 'case_studies'),

    
    url(r'^pages/basic-grid', views.basic_grid, name = 'basic_view'),
    url(r'^pages/full-width', views.full_width, name = 'full_width'),
    url(r'^pages/gallery', views.gallery, name = 'gallery'),
    url(r'^pages/sidebar-left', views.sidebar_left, name = 'sidebar_left'),
    url(r'^pages/sidebar-right', views.sidebar_right, name = 'sidebar_right'),
]