from django.urls import path
from authentication import views

app_name= 'authentication'
urlpatterns = [
    path('register/', views.RegisterAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('register-restaurant/', views.RegisterRestaurantView.as_view(), name='register'),
    path('login-restaurant/', views.LoginRestaurantAPIView.as_view(), name='restaurant-login'),
    path('super/', views.CommandCenter.as_view(), name='super')
]
