from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend , filters.SearchFilter, filters.OrderingFilter]
    # / products /?search = phone
    search_fields = ['name', 'description']
    # / products /?ordering = price or / products /?ordering = -name
    ordering_fields = ['price', 'created_at' , 'updated_at']
    # /products/?category=electronics
    filterset_fields = ['category']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer