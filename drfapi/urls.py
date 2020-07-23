from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('authen/',views.obtain_auth_token),
    path('api/user/',include('api_user.urls')),
    path('api/',include('api_zaikodata.urls')),
    
    path('api/rest_auth/',include('rest_auth.urls')),
     path('api/rest_auth/registration/',include('rest_auth.registration.urls')),
     
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)