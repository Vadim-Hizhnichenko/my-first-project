from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from .serializers import CategorySerializer, NonalcoholcocktailsSerializer, AlcoholcocktailsSerializer
from ..models import Category, NonAlcoholCocktails, AlcoholCocktails


class CategoryPagination(PageNumberPagination):

    page_size = 10
    page_query_param = 'page_size'
    max_page_size = 10


class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()


class NonAlcoholCocktailsAPIView(ListAPIView):

    serializer_class = NonalcoholcocktailsSerializer
    queryset = NonAlcoholCocktails.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']


class AlcoholCocktailsAPIView(ListAPIView):

    serializer_class = AlcoholcocktailsSerializer
    queryset = AlcoholCocktails.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']


class NonAlcoholCocktailsDetailAPIView(RetrieveAPIView):

    serializer_class = NonalcoholcocktailsSerializer
    queryset = NonAlcoholCocktails.objects.all()
    lookup_field = 'id'


class AlcoholCocktailsDetailAPIView(RetrieveAPIView):

    serializer_class = AlcoholcocktailsSerializer
    queryset = AlcoholCocktails.objects.all()
    lookup_field = 'id'
