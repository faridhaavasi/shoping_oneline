from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import User, Otp
from .forms import UserRegisterForm, UserverifyCodeForm, UserLoginForm
from random import randint
from django.contrib.auth import authenticate, login

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
                'full_name': clean_data['full_name'],
                'password': clean_data['password']
            }
            Otp.objects.create(
                phone_number=request.session['user_register_info']['phone_number'],
                code=instace_code
            )
            messages.success(request, 'send sms code fpr you')
            return redirect('accounts:verify_code')
        return render(request, 'accounts/user_register.html', {'form': form})


class UserVerifycodeView(View):
    form_class = UserverifyCodeForm

    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/verifycode.html', {'form': form})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            session_register = request.session['user_register_info']
            print(session_register)
            instance = Otp.objects.get(phone_number=session_register['phone_number'])
            code = instance.code

            if clean_data['code'] == str(code):

                User.objects.create_user(email=session_register['email'],
                                         phone_number=session_register['phone_number'],
                                         full_name=session_register['full_name'],
                                         password=session_register['password'])

                messages.success(request, 'registerd')
                otp = Otp.objects.get(phone_number=session_register['phone_number'])
                otp.delete()
                del session_register
                return redirect('home:home_page')

            messages.success(request, 'code is not match')

        return render(request, 'accounts/verifycode.html', {'form': form})

class UserLoginView(View):
    form_class = UserLoginForm
    def get(self, request):
        form = self.form_class()
        return render(request, 'accounts/login.html',{'form': form})





