from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Product
from . import tasks
from django.contrib import messages
# Create your views here.

class HomePage(View):
    template_name = 'home/index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)


class ListOfProductsView(View):
    template_name = 'home/list_of_products.html'
    def get(self, request):
        products = Product.objects.available_True_manager()
        return render(request, self.template_name, {'products': products})


class DetailProductView(View):
    template_name = 'home/product_detail.html'
    def get(self, request, slug):
        product = Product.objects.get(slug=slug)
        return render(request, self.template_name, {'product': product})




class BucketHome(View):
	template_name = 'home/bucket.html'
	def get(self, request):
		objects = tasks.all_bucket_objects_task()
		return render(request, self.template_name, {'objects':objects})




class DeleteBucketObject(View):
	def get(self, request, key):
		tasks.delete_object_task.delay(key)
		messages.success(request, 'your object will be delete soon.', 'info')
		return redirect('home:bucket')


class DownloadBucketObject(View):
	def get(self, request, key):
		tasks.download_object_task.delay(key)
		messages.success(request, 'your download will start soon.', 'info')
		return redirect('home:bucket')



