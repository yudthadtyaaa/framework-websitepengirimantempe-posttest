from django.shortcuts import render
from .models import Tempe

def home(request):
    tempe_list = Tempe.objects.all()
    return render(request, 'core/index.html', {'tempe_list': tempe_list})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')
