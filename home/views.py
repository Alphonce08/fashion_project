from django.shortcuts import render, redirect
from .models import Fashion
import os
from django.conf import settings
from .models import Images

     


def img(request):
    images = Images.objects.all()
    context = {"images": images}
    return render(request, "electronic.html", "fashion.html", "jewellery.html", context)       
        



def home(request):
    return render(request, 'index.html')

def electronic(request):
    return render(request, 'electronic.html')

def fashion(request):
    return render(request, 'fashion.html')
def buy(request):
    return render(request, 'buy.html')

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

    
def oauth_success(request):
    r = cl.access_token()
    return JsonResponse(r, safe=False)


def lipamimi(request):
    if request.method == "POST":
        phone_number = request.POST.get('phone')
        amount = request.POST.get('amount')
        amount = int(amount)
        account_reference = 'WANYAMA'
        transaction_desc = 'STK Push Description'
        callback_url = stk_push_callback_url
        r = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
        return JsonResponse(r.response_description, safe=False)
    return render(request, 'buy.html')