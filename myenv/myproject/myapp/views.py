from django.shortcuts import render
from .models import *

# Create your views here.

#<<<<<<<<<<<<<<< HOME >>>>>>>>>>>>>>>>>>>>>>

def home(request):
    # --------------------- FATCH ALL PRODUCT ---------------------------
    products = Product_mst.objects.all()
    return render(request,'home.html',{'products': products})

#<<<<<<<<<<<<<<< ADD PRODUCT >>>>>>>>>>>>>>>>>>>>>>

def add_product(request):
    if request.POST:
        # --------------------- CREATE PRODUCT ---------------------------
        a = request.POST['name']   # store the value in variable
        name = a.upper()           # str are uper case and store name variable
        p = Product_mst.objects.create(
            product_name = name
        )
        # --------------------- CREATE PRODUCT DETAILS ---------------------------
        Product_sub_cat.objects.create(
            pid = p,
            p_price = request.POST['price'],
            p_image = request.FILES['image'],
            p_model = request.POST['model'],
            p_ram = request.POST['ram']
        )
        msg = "Product successfully added"
        return render(request,'add_product.html',{'msg':msg})        
    else:
        return render(request,'add_product.html')
    
#<<<<<<<<<<<<<<< PRODUCT DETAIL >>>>>>>>>>>>>>>>>>>>>>

def p_details(request,pk):
        # --------------------- FATCH PRODUCT DETAIL ---------------------------
        product = Product_mst.objects.get(pk=pk)
        p_detail = Product_sub_cat.objects.filter(id = product.pk) 
        return render(request,'p_details.html',{'p_detail': p_detail})
    
#<<<<<<<<<<<<<<< EDIT PRODUCT  >>>>>>>>>>>>>>>>>>>>>>

def edit_product(request,pk):
    if request.POST:
        # --------------------- FATCH  PRODUCT AND EDIT PRODUCT ---------------------------
        product = Product_mst.objects.get(pk=pk)
        a = request.POST['name']
        name = a.upper()
        product.product_name = name
        product.save()
        p_detail = Product_sub_cat.objects.get(id = product.pk) 
    
        p_detail.p_price = request.POST['price']
        if request.FILES:
            p_detail.p_image = request.FILES['image']
        p_detail.p_model = request.POST['model']
        p_detail.p_ram = request.POST['ram']
        
        p_detail.save()
        p_detail = Product_sub_cat.objects.filter(id = product.pk) 
        return render(request,'p_details.html',{'p_detail': p_detail})
    else:
        product = Product_mst.objects.get(pk=pk)
        p_detail = Product_sub_cat.objects.get(id = product.pk) 
        print("===============",p_detail.p_price)
        return render(request,'edit_product.html',{'p_detail': p_detail})

#<<<<<<<<<<<<<<< DELETE PRODUCT >>>>>>>>>>>>>>>>>>>>>>

def delete_product(request,pk):
        # --------------------- FATCH  PRODUCT AND DELETE PRODUCT ---------------------------
        product = Product_mst.objects.get(pk=pk)
        product.delete()
        msg = "Product successfully delete" 
        products = Product_mst.objects.all()
        return render(request,'home.html',{'products': products,'msg':msg})

#<<<<<<<<<<<<<<< SEARCH PRODUCT >>>>>>>>>>>>>>>>>>>>>>

def search_item(request):
    # --------------------- FATCH  PRODUCT  ---------------------------
    if request.POST['search']:
        
            a = request.POST['search']  # Store the value in a variable
            name = a.upper()            #convert value in uppercase and store the value in variable
            print("name",name)          # print variable
            
            try:
                product = Product_mst.objects.get(product_name = name)
                print("==============>",product)

                products = Product_sub_cat.objects.filter(pk = product.pk)
                print(products)
                return render(request,'search_item.html',{'products': products})
            except:
                msg1="Item not Found !!"
                products = Product_mst.objects.all()
                return render(request,'home.html',{'products': products,'msg1':msg1})
   
    else:
        products = Product_mst.objects.all()
        return render(request,'home.html',{'products': products})

    

    
