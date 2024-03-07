from django.shortcuts import render
from django.views.generic import View
from .models import Product
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

