from .models import Category, Blog


def categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def random_blog(request):
    blogs = Blog.objects.order_by('?').all()
    random_blogs = []
    
    if blogs:
        random_blogs = blogs[:2]
        
    return dict(random_blogs=random_blogs)


def popular_blogs(request):
    blogs = Blog.objects.all().order_by("-views")
    
    popular_blogs = []
    first_popular_blog = []
    second_popular_blogs = []
    
    if blogs:
        popular_blogs = blogs[0:3]
        first_popular_blog = popular_blogs[0]
        second_popular_blogs = popular_blogs[1:]

    return dict(popular_blogs=popular_blogs, first_popular_blog=first_popular_blog,  second_popular_blogs=second_popular_blogs)

def recent_blogs(request):
    blogs = Blog.objects.all().order_by("-created_at")
    recent_blogs = []
    first_recent_blog = []
    second_recent_blog = []
    
    if blogs:
        recent_blogs = blogs[0:3]
        first_recent_blog = recent_blogs[0]
        second_recent_blog = recent_blogs[1:]

    return dict(recent_blogs=recent_blogs, first_recent_blog=first_recent_blog, second_recent_blog=second_recent_blog)


# def tech_blogs(request):
#     tech_category = Category.objects.get(slug="tech")
#     blogs = tech_category.blog_set.all()
#     first_tech_blog = blogs[0]
#     tech_blogs = blogs[1:]
#     return dict(first_tech_blog=first_tech_blog, tech_blogs=tech_blogs)


# # def business_blogs(request):
# #     business_category = Category.objects.get(slug="business")
# #     blogs = business_category.blog_set.all()
# #     first_business_blog = blogs[0]
# #     business_blogs = blogs[1:]
# #     return dict(first_business_blog=first_business_blog, business_blogs=business_blogs)


# # def game_blogs(request):
# #     game_category = Category.objects.get(slug="game")
# #     blogs = game_category.blog_set.all()
# #     first_game_blog = blogs[0]
# #     game_blogs = blogs[1:]
# #     return dict(first_game_blog=first_game_blog, game_blogs=game_blogs)


# # def social_blogs(request):
# #     social_category = Category.objects.get(slug="social")
# #     blogs = social_category.blog_set.all()
# #     first_social_blog = blogs[0]
# #     social_blogs = blogs[1:]
# #     return dict(first_social_blog=first_social_blog, social_blogs=social_blogs)


# # def movie_blogs(request):
# #     movie_category = Category.objects.get(slug="movie")
# #     blogs = movie_category.blog_set.all()
# #     first_movie_blog = blogs[0]
# #     movie_blogs = blogs[1:]
# #     return dict(first_movie_blog=first_movie_blog, movie_blogs=movie_blogs)
