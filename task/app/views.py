from django.shortcuts import  render, redirect
from .forms import *
from .models import *
from django.contrib.auth import login
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login,logout

# Create your views here.
def dashboard(request):
    product=Product.objects.all()
    context={
        "product":product
    }
    return render(request,'dashboard.html',context)

# def show(request):
#     return render(request,'dashboard.html')

class Registration(View):
    def get(self,request):
        myforms=UsersForm()
        return render(request,'register.html',{"userform":myforms})    
    def post(self,request):
        myforms=UsersForm(request.POST)
        if myforms.is_valid():
                myforms.save()
                return render(request,'login.html')


class Logins(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        usnm=request.POST['usnm']
        pswd=request.POST['pswd']
        user_cnfrm=Users.objects.filter(username=usnm).filter(password=pswd)
        if user_cnfrm:
            return redirect('dashboard')
        else:
           return render(request,'login.html')


def logouts(request):
    logout(request)
    return redirect('login')

def delete(request):
    pro_id=request.GET.get('pro_id')
    Product.objects.get(id=pro_id).delete()
    return redirect('dashboard')


def update(request):
    if request.method=="GET":
        pro_id=request.GET.get('pro_id')
        product=Product.objects.filter(id=pro_id)
        return render(request,'update.html',{'product':product})
    else:
        
        pro_id=request.POST.get('pro_id')
        product=Product.objects.get(id=pro_id)
        product.name=request.POST.get('name')
        product.description=request.POST.get('description')
        product.price=request.POST.get('price')
        product.save()
        return redirect('dashboard')


def add_product(request):
    if request.method=="POST":
        product=Product()
        product.name=request.POST.get('name')
        product.description=request.POST.get('description')
        product.price=request.POST.get('price')
        product.save()
        return redirect('dashboard')
    return render(request, 'add.html')