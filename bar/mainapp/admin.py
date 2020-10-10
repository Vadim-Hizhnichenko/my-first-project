from django import forms
from django.contrib import admin
from .models import *
from django.forms import ModelForm




admin.site.register(Category)
admin.site.register(AlcoholCocktails)
admin.site.register(NonAlcoholCocktails)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)



