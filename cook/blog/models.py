from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField


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
    objects = models.Manager
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(Category, related_name='post', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, default='', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_single', kwargs={'slug': self.category.slug, 'post_slug': self.slug})

    def get_recipes(self):
        return self.recipes.all()


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    serves = models.CharField(max_length=63)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(Post,
                             related_name='recipes',
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)


class Comment(models.Model):
    name = models.CharField(max_length=63)
    email = models.CharField(max_length=127)
    website = models.CharField(max_length=127)
    message = models.TextField(max_length=511)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
