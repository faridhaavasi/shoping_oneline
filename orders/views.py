from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from home.models import Product
from .forms import CartAddForm
# Create your views here.

class CartView(View):
    template_name = 'orders/cart.html'
    def get(self, request):
        return render(request, self.template_name, {})

class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(data=request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])
            return redirect('orders:cart')
