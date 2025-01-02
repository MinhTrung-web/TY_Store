from django.urls import path, include
from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.Register.as_view(), name='register'),
    path('profile', views.profile, name='profile'),
    path('logged_out/', views.logged_out, name='logged_out'),
    # Sử dụng logout_view của bạn
    path('logout/', views.logout_view, name='logout'),
]
