from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Tag(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    ##image = models.FilePathField(path="/img")
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(Category,on_delete= models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True)
    publish_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
