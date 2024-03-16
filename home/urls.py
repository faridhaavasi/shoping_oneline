from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('', views.BucketHome.as_view(), name='bucket'),

    path('products/', views.ListOfProductsView.as_view(), name='list_of_products'),
    path('detal/product/<slug:slug>', views.DetailProductView.as_view(), name='detail_product'),
]