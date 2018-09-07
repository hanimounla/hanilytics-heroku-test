from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
import core.views as views



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tour/$', views.tour, name='tour'),
    url(r'^about/$',views.about, name = 'about'),
    
    # url(r'^pages/basic-grid', views.basic_grid, name = 'basic_view'),
    # url(r'^pages/full-width', views.full_width, name = 'full_width'),
    # url(r'^pages/gallery', views.gallery, name = 'gallery'),
    # url(r'^pages/sidebar-left', views.sidebar_left, name = 'sidebar_left'),
    # url(r'^pages/sidebar-right', views.sidebar_right, name = 'sidebar_right'),
]