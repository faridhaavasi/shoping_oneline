from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('reegister', views.UserRegisterView.as_view(), name='user_register'),
    path('verifycode',views.UserVerifycodeView.as_view(), name='verify_code'),
    path('login', views.UserLoginView.as_view(), name='user_login'),
    path('logout/<int:pk>', views.UserLogoutView.as_view(), name='user_logout'),
]