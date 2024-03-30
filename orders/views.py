from django.shortcuts import render
from django.views import View
# Create your views here.

class CartView(View):
    template_name = 'orders/cart.html'
    def get(self, request):
        return render(request, self.template_name, {})

class CartAddView(View):
    def post(self, request, product_id):
        pass