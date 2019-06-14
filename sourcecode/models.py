from django.db import models
from django.contrib.auth.models import User
from leaflet.forms.fields import MultiPointField


class Article(models.Model):
    article_name = models.CharField(max_length=21, blank=True)
    construction_object_name = models.CharField(max_length=50, blank=True)
    construction_objects = models.FileField(
        upload_to='BuildObjects',
        blank=True
    )
    construction_image = models.ImageField(
        upload_to='Image/Objects image',
        blank=True
    )
    descriptions = models.TextField("Текстовое описание")


class Map(models.Model):
    map_name = models.CharField(max_length=20, blank=True)
    map_image = models.ImageField(
        upload_to='Image/Maps',
        blank = True
    )

class ArticleObjectsSpot(models.Model):
    name = models.OneToOneField(Article, on_delete=models.CASCADE)
    geom = MultiPointField()

    def __unicode__(self):
        return self.name