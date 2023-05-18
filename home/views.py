from django.shortcuts import render, redirect
from .models import Fashion
import os
from django.conf import settings
from .models import Images,Product

     

#image upload
def img(request):
    images = Images.objects.all()
    context = {"images": images}
    return render(request, "electronic.html", "fashion.html", "jewellery.html", context)       
        



def home(request):
    e_prod= Product.objects.filter(category_id=1,sold=False) 
    f_prod= Product.objects.filter(category_id=6,sold=False)
    j_prod= Product.objects.filter(category_id=2,sold=False)
    
    print(f_prod[0:3])
    
    context = {"e_prod":e_prod ,"f_prod":f_prod,"j_prod":j_prod,}
    
    
    return render(request, 'index.html', context)
    

def electronic(request):
    e_prod= Product.objects.filter(category_id=1,sold=False)
    context = {"e_prod":e_prod }
 
    return render(request, 'electronic.html', context)

def fashion(request):
    f_prod= Product.objects.filter(category_id=6,sold=False)
    context = {"f_prod":f_prod }
    return render(request, 'fashion.html', context)
    
def buy(request):
    return render(request, 'buy.html')

def more(request):
    return render(request, 'more.html')

def jewellery(request):
    j_prod= Product.objects.filter(category_id=2,sold=False)
    context = {"j_prod":j_prod }
    return render(request, 'fashion.html', context)
    return render(request, 'jewellery.html')
    #contact page
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

   #payment 
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
