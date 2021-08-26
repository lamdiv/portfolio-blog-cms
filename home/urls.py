from django.urls import path
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin

from .views import IndexView,AboutView,PortfolioView,PortfolioDetailView,BlogView,BlogDetailView,SearchView,ContactView
from .models import Blog

info_dict = {
    'queryset': Blog.published.all(),
    'date_field': 'created',
}

app_name="home"

admin.site.site_title = 'Portfolio'
admin.site.site_header = 'My portfolio Websit'    
admin.site.index_title = 'Features Area'

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('portfolio/',PortfolioView.as_view(),name='project'),
    path('portfolio/<slug:slug>/',PortfolioDetailView.as_view(),name='project_detail'),
    path('blogs/',BlogView.as_view(),name='blogs'),
    path('tags/<slug:tag_slug>/',BlogView.as_view(),name='tags'),
    path('categories/<slug:categories>/',BlogView.as_view(),name='categories'),
    path('blogs/<slug:slug>/',BlogDetailView.as_view(),name='blog_detail'),
    path('search/',SearchView.as_view(),name='search'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('sitemap.xml', sitemap,
         {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
         name='django.contrib.sitemaps.views.sitemap'),
]