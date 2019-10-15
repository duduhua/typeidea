from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import views as sitemap_views

from .views import (
    IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
)
from .rss import LatestPostFeed
from .sitemap import PostSitemap

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category-list'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='tag-list'),
    path('post/<int:post_id>.html/', PostDetailView.as_view(), name='post-detail'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:owner_id>/', AuthorView.as_view(), name='author'),
    path('rss/', LatestPostFeed(), name='rss'),
    path('sitemap.xml', sitemap_views.sitemap, {'sitemaps': {'post': PostSitemap}}),
]