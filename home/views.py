from django.shortcuts import render, redirect
from .models import Fashion
import os
from django.conf import settings




def updateimage(request, id):  #this function is called when update data
    old_image = ImageModel.objects.get(id=id)
    form = ImageForm(request.POST, request.FILES, instance=old_image)

    if form.is_valid():

        # deleting old uploaded image.
        image_path = old_image.image_document.path
        if os.path.exists(image_path):
            os.remove(image_path)

        # the `form.save` will also update your newest image & path.
        form.save()
        return redirect("/fashion_project")
    else:
        context = {'singleimagedata': old_image, 'form': form}
        return render(request, 'demo/editproduct.html', context)



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

    
