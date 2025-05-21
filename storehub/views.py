from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, UserRegistrationSerializer


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
    #  for products only
    permission_classes = [IsAuthenticatedOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes =  [AllowAny]
    serializer_class = UserRegistrationSerializer