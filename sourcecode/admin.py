from django.contrib import admin
from .models import Article, Map
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import ArticleObjectsSpot

# Register your models here.
admin.site.register(Article)
admin.site.register(Map)


admin.site.register(ArticleObjectsSpot, LeafletGeoAdmin)