from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('reegister', views.UserRegisterView.as_view(), name='user_register'),
    path('verifycode',views.UserVerifycodeView.as_view(), name='verify_code'),
]