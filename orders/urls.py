from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('create_order', views.CreateOrderView.as_view(), name='create_order'),
    path('detail_order/<int:order_id>', views.OrderDetailView.as_view(), name='order_detail'),
    path('pay/<int:order_id>/', views.OrderPayView.as_view(), name='order_pay'),
	path('verify/', views.OrderVerifyView.as_view(), name='order_verify'),
    path('cart', views.CartView.as_view(), name='cart'),
    path('cart/add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('cart/remove/<str:product_name>/', views.CartRemoveView.as_view(), name='cart_remove'),

]
