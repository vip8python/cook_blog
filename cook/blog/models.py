from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    serves = models.CharField(max_length=63)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(Post,
                             related_name='recipe',
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=63)
    email = models.CharField(max_length=127)
    website = models.CharField(max_length=127)
    message = models.TextField(max_length=511)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)






