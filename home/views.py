from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class HomePage(View):
    template_name = 'home/index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)


