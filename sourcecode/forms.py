from django import forms
from .models import Article, Map, ArticleObjectsSpot
from ckeditor.widgets import CKEditorWidget
from django.views.generic import UpdateView
from leaflet.forms.widgets import LeafletWidget
from leaflet.forms.fields import MultiPointField


class ArticleForm(forms.ModelForm):
    article_name = forms.CharField(
        label='Название статьи',
        max_length=20,
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    construction_object_name = forms.CharField(
        label='Название здания',
        max_length=50,
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    construction_objects = forms.FileField(
        label='Объект',
        widget=forms.ClearableFileInput(),
        required=False,
    )
    construction_image = forms.ImageField(
        label='Изображение',
        widget=forms.ClearableFileInput(),
        required=False,
    )

    class Meta:
        model = Article
        fields = [
            'article_name',
            'construction_object_name',
            'construction_objects',
            'construction_image',
            'descriptions',
        ]
        widgets = {
            'descriptions': forms.Textarea(
                attrs={'class': 'form-control', 'rows': '5', 'cols': '5'}
            )
        }


class MapForm(forms.ModelForm):
    map_name = forms.CharField(
        label='Название карты',
        max_length=20,
        min_length=2,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    map_image = forms.ImageField(
        label='Карта',
        widget=forms.ClearableFileInput(),
        required=False,
    )

    class Meta:
        model = Map
        fields = [
            'map_name',
            'map_image',
        ]


class ArticleObjectsSpotForm(forms.ModelForm):
    geom = MultiPointField()

    class Meta:
        model = ArticleObjectsSpot
        fields = ('name', 'geom',)



