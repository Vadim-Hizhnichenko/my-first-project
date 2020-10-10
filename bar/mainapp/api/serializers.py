from rest_framework import serializers
from ..models import Category, AlcoholCocktails, NonAlcoholCocktails


class CategorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    slug = serializers.SlugField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class BaseProductSerializer:
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    image = serializers.ImageField(required=True)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)


class NonalcoholcocktailsSerializer(BaseProductSerializer, serializers.ModelSerializer):
    volume = serializers.CharField(required=True)
    temperature = serializers.CharField(required=True)
    taste = serializers.CharField(required=True)

    class Meta:
        model = NonAlcoholCocktails
        fields = '__all__'


class AlcoholcocktailsSerializer(BaseProductSerializer, serializers.ModelSerializer):
    alcohol_content = serializers.CharField(required=True)
    volume = serializers.CharField(required=True)
    temperature = serializers.CharField(required=True)
    in_time = serializers.CharField(required=True)

    class Meta:
        model = AlcoholCocktails
        fields = '__all__'
