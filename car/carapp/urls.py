
from django.urls import path
from carapp import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('about',views.about),
    path('contact',views.contact),
    path('car',views.car),
    path('detail',views.detail),
    path('booking',views.booking),
    path('service',views.service),
]