from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import viewsets, filters, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.views import APIView

from .models import Product, Category, Order, OrderItem
from .permissions import IsStaffReadOnly
from .serializers import ProductSerializer, CategorySerializer, UserRegistrationSerializer, OrderSerializer, \
    OrderItemSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # / products /?search = phone
    search_fields = ['name', 'description']
    # / products /?ordering = price or / products ordering = -name
    ordering_fields = ['price', 'created_at', 'updated_at']
    # /products/?category=electronics
    filterset_fields = ['category']
    #  for products only
    permission_classes = [IsStaffReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer


class ProfileView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_staff': user.is_staff,
        })


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        # Only return orders of the logged-in user
        return Order.objects.filter(user=self.request.user)


    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']
        total_price = product.price * quantity
        serializer.save(user=self.request.user, total_price=total_price)



class OrderItemViewSet(viewsets.ModelViewSet):
    querySet  = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
