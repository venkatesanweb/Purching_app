from http.client import HTTPResponse
import json
from venv import logger
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail


from Shop_Fusion.forms import ContactForms, CustomerForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


def index(request):
    products=Product.objects.filter(trending=1)
    return render(request,"index.html",{"products":products})
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            name = request.POST.get("username")  # Ensure this matches the form field name
            key = request.POST.get("password")

            user = authenticate(request, username=name, password=key)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in Successfully")  # Fixed spelling mistake
                return redirect('/')
            else:
                messages.error(request, "Invalid Username And Password")
                return redirect('/login/')

        return render(request, "login.html")

def register(request):
    form=CustomerForm()
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=="POST":
            form=CustomerForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"User Created Successfully You can Login Now !..")
                return redirect("/login/")
        


        return render(request,"register.html",{'forms':form})

def Collections(request):
    catagory=Catagory.objects.filter(status=0)
    return render(request,"collections.html",{"catagory":catagory})

def Collectionsview(request,name):
    if(Catagory.objects.filter(status=0,name=name)):
        products=Product.objects.filter(catagory__name=name)
        return render(request,"products/index.html",{"products":products,"cate_name":name})
    else:
        messages.warning(request,"No Such Catagory Founnd")
        return redirect("/collections/")
    

def Productdetailview(request,cname,pname):
    if(Catagory.objects.filter(status=0,name=cname)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"products/productdetails.html",{"products":products})
        else:
            messages.error(request,"No such Product Found")
            return render("/collections/")
    else:
        messages.error(request,"No Such Catagory Found")
        return redirect("/collections/")
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Loged Out Successfully")
        return redirect("/")
    return redirect("login/")

def addtocart(request):
    if request.headers.get("x-requested-with")=="XMLHttpRequest":
        if request.user.is_authenticated:
            data=json.load(request)
            
            product_qty=(data['product_qty'])
            product_id=int(data['pid'])
            #print(request.user.id)
            products_stutes=Product.objects.get(id=product_id)
            if products_stutes:
                if Cart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already In Cart'},status=200)
                else:
                    if products_stutes.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,quantity_qut=product_qty)
                        return JsonResponse({'status':'Prodect Added To Cart'},status=200)
                    else:
                        return JsonResponse({'status':'Product Out Of Stock'},status=200)

        else:
            return JsonResponse({'status':'Login To AddCart'},status=200)
        
    else:
        return JsonResponse({'status':'invalid Access'},status=200)
    



def cart(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request,"cart.html",{"cart":cart})
    else:
        return redirect("/")
    

def delete(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/Cart/")
def contact(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if form.is_valid():
            # Sending the email
            subject = f"Message from {name} - {email}"
            email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(
                subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,  # Sender email
                ['your_email@example.com'],  # Recipient email (change this to your email)
                fail_silently=False
            )

            # Log the successful sending of the email
            logger.debug(f"Sent email from {email} with message: {message}")
            messages.success(request, "Your email has been sent successfully!")

            # After sending the email, you may want to reset the form fields
            return render(request, "contact.html", {'form': form})

        else:
            logger.debug("Form validation failed")

        return render(request, "contact.html", {'form': form, 'name': name, 'email': email, 'message': message})

    return render(request, "contact.html",)



def about(request):
    return render(request,"about.html")
    
    

