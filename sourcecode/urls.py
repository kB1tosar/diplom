from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name="sourcecode"
urlpatterns = [
    path('', views.index, name='index'),
    path('add_article/', views.create_article, name='add_article'),
    path(
        'full_description/<int:pk>',
        views.full_description,
        name='full_description'
    ),
    path(
        'article_delete/<int:pk>',
        views.article_remove,
        name='article_delete'
    ),
    path('article_edit/<int:pk>', views.article_edit, name='article_edit'),
    path('add_map/', views.create_map, name='add_map'),
    path('add/', views.feature, name='add'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
