from django.shortcuts import render, redirect
from .models import Fashion

def index(request):
    return render(request, 'index.html')

def electronic(request):
    return render(request, 'electronic.html')

def fashion(request):
    return render(request, 'fashion.html')

def jewellery(request):
    return render(request, 'jewellery.html')
    
def contact(request):
     if request.method == "POST":
        phonenumber = request.POST.get('phonenumber')
        delivery = request.POST.get('delivery')
        category = request.POST.get('category')
       
        query = Fashion(phonenumber=phonenumber, delivery=delivery, category=category)
        query.save()
        return redirect("/")
     return render(request, 'contact.html')

    
