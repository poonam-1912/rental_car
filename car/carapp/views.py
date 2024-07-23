from django.shortcuts import render
from carapp import urls


# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def car(request):
    return render(request, 'car.html')

def detail(request):
    return render(request, 'detail.html')

def booking(request):
    return render(request, 'booking.html')
# def contact(request):
#     return render(request, 'about.html')