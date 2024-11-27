from django.contrib import admin
from django.urls import path, include  # Include is for app-specific routing
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('tasks/', include('tasks.urls')),  # Include app-level URLs (keep this or similar routes)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT token route
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh token route
]
