from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:type>", views.ordered_blog, name='get_blog_by_ordering'),
    path("category/<slug:category_slug>", views.blog_category, name='get_blog_by_category'),
    path("detail/<int:blog_id>", views.blog_detail, name='get_blog_detail'),
    path("tags/<slug:tag_slug>", views.blog_tag, name='get_blog_by_tag')
]
