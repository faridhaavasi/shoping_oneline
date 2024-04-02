from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .cart import Cart
from home.models import Product
from .forms import CartAddForm
# Create your views here.

class CartView(View):
    template_name = 'orders/cart.html'
    def get(self, request):
        cart = Cart(request)
        return render(request, self.template_name, {'cart': cart})

class CartAddView(View):
	def post(self, request, product_id):
		cart = Cart(request)
		product = get_object_or_404(Product, id=product_id)
		form = CartAddForm(data=request.POST)
		if form.is_valid():
			cart.add(product, quantity=form.cleaned_data['quantity'])

			return redirect('orders:cart')
		return redirect('home:detail_product')

class CartRemoveView(View):
	def get(self, request, product_name):
		cart = Cart(request)
		product = get_object_or_404(Product, name=product_name)
		cart.remove(product=product)
		return redirect('orders:cart')


