from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product, Category, Order, OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(write_only=True,
                                           source='category',
                                           queryset=Category.objects.all()
                                           )
    class Meta:
        model = Product
        fields = ['id', 'name', 'description' , 'image'
                    , 'price', 'stock', 'created_at',
                    'updated_at', 'category', 'category_id']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        # execute save mehtod + hashing the password text
    def create(self, validated_data):
        iems_data = validated_data.pop('items')
        return User.objects.create_user(**validated_data)



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'product', 'user', 'quantity', 'total_price', 'ordered_at']
        read_only_fields = ['user' , 'total_price', 'ordered_at']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [ 'quantity' , 'price', 'product']





