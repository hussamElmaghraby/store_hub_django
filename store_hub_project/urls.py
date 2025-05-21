from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import  static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
       # path('admin/', admin.site.urls),
       path('api/', include('storehub.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
       path('api/auth/login/', TokenObtainPairView.as_view() , name = 'token_obtain_pair'),
       path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]