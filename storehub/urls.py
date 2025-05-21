from django.urls import path, include
from rest_framework.routers import DefaultRouter

from storehub.views import ProductViewSet, CategoryViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('auth/register/', UserRegistrationView.as_view(), name='auth_registration'),
]

