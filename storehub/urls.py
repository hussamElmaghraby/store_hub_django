from django.urls import path, include
from rest_framework.routers import DefaultRouter

from storehub.views import ProductViewSet, CategoryViewSet, UserRegistrationView, ProfileView, OrderViewSet, \
    OrderItemViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

router.register(r'orders' , OrderViewSet)
router.register(r'order-item' , OrderItemViewSet, basename='order-item')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/profile/', ProfileView.as_view(), name='auth_profile'),
    path('auth/register/', UserRegistrationView.as_view(), name='auth_registration'),

]