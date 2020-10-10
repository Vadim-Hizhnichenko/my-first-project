from django.urls import path

from .api_views import (
    CategoryListAPIView,
    NonAlcoholCocktailsAPIView,
    AlcoholCocktailsAPIView,
    NonAlcoholCocktailsDetailAPIView,
    AlcoholCocktailsDetailAPIView)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories_list'),
    path('nonalcoholcocktails/', NonAlcoholCocktailsAPIView.as_view(), name='nonalcoholcocktails_list'),
    path('alcoholcocktails/', AlcoholCocktailsAPIView.as_view(), name='alcoholcocktails_list'),
    path('alcoholcocktails/<str:id>/', AlcoholCocktailsDetailAPIView.as_view(), name='alcoholcocktails_detail'),
    path('nonalcoholcocktails/<str:id/', NonAlcoholCocktailsDetailAPIView.as_view(), name='nonalcoholcocktails_detail')
]
