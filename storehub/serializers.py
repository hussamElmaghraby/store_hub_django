from rest_framework import serializers
from .models import Product, Category


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
