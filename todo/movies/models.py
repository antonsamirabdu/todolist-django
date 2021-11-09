from django.db import models
from django.conf import settings


# Create your models here.

class Actor(models.Model):
    first_name = models.CharField(max_length=255, unique=True)
    last_name = models.CharField(max_length=255, null=True)
    profile_image = models.ImageField(upload_to='actor/images')
    id_name = models.OneToOneField("IdentityNamber", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ('first_name',)
        verbose_name = "cast"


class IdentityNamber(models.Model):
    number = models.CharField(max_length=50)

    def __str__(self):
        return self.number


class Review(models.Model):
    comment = models.TextField()
    attachment = models.FileField(upload_to='movie/attachment/review', null=True, blank=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE())
    movie = models.ForeignKey("Movies", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{} - Review'.format(self.movie)


class Movies(models.Model):
    active = models.BooleanField(default=True)

    name = models.CharField("Movie Name", max_length=255, unique=True)  # my first column in the table

    description = models.TextField(verbose_name="Movie Description")

    likes = models.IntegerField(default=0, null=True)

    watch_count = models.IntegerField(default=0, null=True)

    rate = models.PositiveIntegerField(default=0, null=True)

    production_date = models.DateField(null=True, blank=True)

    creation_date = models.DateTimeField(auto_now_add=True)

    modification_date = models.DateTimeField(auto_now=True)

    poster = models.ImageField(upload_to='movie/images', null=True)

    video = models.FileField(upload_to='movie/videos' ,null=True)

    actors = models.ManyToManyField("Actor")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = "movies"
        verbose_name_plural= "movies"


class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering = ('category_name',)
        verbose_name = "Category"
        verbose_name_plural= "Categories"

