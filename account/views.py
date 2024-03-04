from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import User, Otp
from .forms import UserRegisterForm
from random import randint
# Create your views here.

class UserRegisterView(View):
    form_class = UserRegisterForm
    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/user_register.html', {'form': form})
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            instace_code = randint(1000, 9999)
            request.session['user_register_info'] = {
                'email': clean_data['email'],
                'phone_number': clean_data['phone_number'],
                'fill_name': clean_data['full_name'],
                'password': clean_data['password']
            }
            Otp.objects.create(
                phone_number=request.session['user_register_info']['phone_number'],
                code=instace_code
            )
            messages.success(request, 'sen sms code fpr you')
            return redirect('accounts:verify_code')
        return render(request, 'accounts/user_register.html', {'form': form})







