from django.shortcuts import render
from django.shortcuts import redirect
from .models import Category, Blog, Tag
from django.core.paginator import Paginator

# Create your views here.


def index(request):
    return render(request, "pages/index.html")
    
def ordered_blog(request, type=None):
    blogs = None
    type_name = ""
    
    if(type is not None and type == "recent_blogs"):
        type_name = "บทความล่าสุด"
        blogs = Blog.objects.all().order_by("-created_at")
    else:
        type_name = "บทความยอดนิยม"
        blogs = Blog.objects.all().order_by("-views")
    
    paginator = Paginator(blogs, 5)
    
    try:
        page = int(request.GET.get("page"))
    except:
        page = 1
        
    try:
        blogs_per_page = paginator.get_page(page)
    except:
        blogs_per_page = paginator.get_page(1)
    
    return render(request, "pages/category.html", {"category_slug_name": type_name, "blogs": blogs_per_page})
    


def blog_category(request, category_slug):
    related_category = Category.objects.filter(slug=category_slug).first()
    blogs = related_category.blog_set.all()
    
    paginator = Paginator(blogs, 5)
    
    try:
        page = int(request.GET.get("page"))
    except:
        page = 1
        
    try:
        blogs_per_page = paginator.get_page(page)
    except:
        blogs_per_page = paginator.get_page(1)
    
    return render(request, "pages/category.html", {"category_slug_name": related_category.name, "blogs": blogs_per_page})


def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    found_blogs = Blog.objects.filter(tags=blog.tags.all()[0].id).all()[:2]
    related_blogs = [found_blog for found_blog in found_blogs if found_blog.id != blog.id]
    blog.views += 1
    blog.save()
    return render(request, "pages/detail.html", {"blog": blog, "related_blogs": related_blogs})


def blog_tag(request, tag_slug):
    relatedTag = Tag.objects.get(slug=tag_slug)
    blogs = relatedTag.blog_set.all()
    return render(request, "pages/category.html", {"category_slug_name": relatedTag.name, "blogs": blogs})
