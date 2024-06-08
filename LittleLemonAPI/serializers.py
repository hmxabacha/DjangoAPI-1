from .models import Cart,Category,MenuItem,Order
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    model=Cart
    fields=['user','menuitem','qunatity','unit_price','price']
    
class OrderSerializer(serializers.ModelSerializer):
    model=Order
    fields=['user','menuitem','qunatity','unit_price','price']
    
class MenuItemSerializer(serializers.ModelSerializer):
    model=MenuItem
    fields=['title','price','featured','category']
    
class CategorySerailizer(serializers.ModelSerializer):
    model=Category
    fields=['slug','title']
    