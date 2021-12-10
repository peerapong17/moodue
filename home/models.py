from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        ordering = ['id']

    def blog_length(self):
        length = self.blog_set.all().count()
        return length
        
    def get_blog_by_category(self):
        return reverse('get_blog_by_category', args=[self.slug])

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tag"
        ordering = ['id']
        
    def get_blog_by_tag(self):
        return reverse('get_blog_by_tag', args=[self.slug])


class Blog(models.Model):
    title = models.CharField(max_length=250)
    short_desc = models.TextField()
    content = RichTextField(blank=True, null=True)
    categories = models.ManyToManyField(Category)
    thumbnail = models.ImageField(upload_to='thumbnail/', default="thumbnail/default.jpg")
    tags = models.ManyToManyField(Tag)
    views = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"
        ordering = ['-created_at']
        
    def get_blog_detail(self):
        return reverse('get_blog_detail', args=[self.id])




