from django.urls import path
from .views import IndexView,AboutView,PortfolioView,PortfolioDetailView,BlogView,BlogDetailView,SearchView,ContactView

app_name="home"

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
]