# jwt_auth/urls.py

from django.contrib import admin
from django.urls import path
from authority.views import CustomTokenObtainPairView, CustomTokenRefreshView, RegisterView
from authority import views
from authority.views import test_id_generation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/upload/', views.upload_files, name='upload_files'),
    path('test-id/', test_id_generation, name='test_id_generation'),

]