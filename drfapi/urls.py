from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token #追加
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('api_user.urls')),
    path('api/',include('api_zaikodata.urls')),
    path('sets/',include('api_usersite.urls')),
    
    # ログイン認証
    path('api-auth/', include('rest_framework.urls')),
    # ログインAPI(ログイン・ログアウト、リセット、リセット機能)
    path('api/v1/rest-auth/', include('rest_auth.urls')), 
    # redister機能
    path('api/v1/rest-auth/registration/',include('rest_auth.registration.urls')),
    
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),  #追加
    

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)