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
     success_massage=""

     if request.method == "POST":
        phonenumber = request.POST.get('phonenumber')
        delivery = request.POST.get('delivery')
        category = request.POST.get('category')
       
        query = Fashion(phonenumber=phonenumber, delivery=delivery, category=category)
        query.save()
        success_massage = "You have sucessfuly send your infomation, You will get within 3 days of your request. Thanks for ordering"
        return render(request, 'contact.html',{"mmg1":success_massage,"mmg2":777})
     return render(request, 'contact.html',{"mmg1":success_massage,"mmg2":777})

    
#     dic1= {"firstname": "Gilbert","secondName":"Korir"} 