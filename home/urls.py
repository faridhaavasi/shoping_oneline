from django.urls import path, include
from . import views
app_name = 'home'

bucket_urls = [
	path('bucket', views.BucketHome.as_view(), name='bucket'),
	path('delete_obj/<str:key>/', views.DeleteBucketObject.as_view(), name='delete_obj_bucket'),
	path('download_obj/<str:key>/', views.DownloadBucketObject.as_view(), name='download_obj_bucket'),
]

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('bucket', views.BucketHome.as_view(), name='bucket'),

    path('products/', views.ListOfProductsView.as_view(), name='list_of_products'),
    path('category/<slug:category_slug>', views.ListOfProductsView.as_view(), name='category_filter'),
    path('detal/product/<slug:slug>', views.DetailProductView.as_view(), name='detail_product'),
]

