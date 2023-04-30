from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path('', views.home, name='home'),
    path('fashion', views.fashion, name='fashion'),
    path('electronic', views.electronic, name='electronic'),
    path('jewellery', views.jewellery, name='jewellery'),
    path('contact', views.contact, name='contact')
    ]
