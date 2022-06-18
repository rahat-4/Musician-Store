from xml.dom.minidom import Document
from django.urls import path
from login_app import views

from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


app_name = 'login_app'

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('user_login/', views.login_func, name='login_func'),
    path('register/', views.user_registration, name='user_registration'),
    path('logout/', views.user_logout, name='user_logout'),
    path('profile/<int:user_id>', views.user_profile, name='user_profile'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
