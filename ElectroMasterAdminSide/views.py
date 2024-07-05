from django.shortcuts import render,redirect
from ElectroMasterAdminSide.models import CategoryDB,ProductDB
from ElectroMasterUserSide.models import ContactDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages


# Create your views here.

def index_page(req):
    return render(req,"index.html")

# --------------

def category_page(req):
    return render(req,"AddCategory.html")

def save_category(req):
    if req.method =="POST":
        cn = req.POST.get('c_name')
        des = req.POST.get('desc')
        cimg = req.FILES['c_image']
        obj = CategoryDB(Category_Name=cn, Description=des, Category_Image=cimg)
        obj.save()
        messages.success(req,"category details saved successfully")
        return redirect(category_page)

def category_display(req):
    Category = CategoryDB.objects.all()
    return render(req,"DisplayCategory.html",{'Category':Category})

def category_edit(req,dataid):
    Category = CategoryDB.objects.get(id=dataid)
    return render(req,"EditCategory.html",{'Category':Category})

def category_update(req,dataid):
    if req.method =="POST":
        cn = req.POST.get('c_name')
        des = req.POST.get('desc')
        try:
            cimg = req.FILES['c_image']
            fs = FileSystemStorage()
            file = fs.save(cimg.name,cimg)
        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=dataid).Category_Image
    CategoryDB.objects.filter(id=dataid).update(Category_Name=cn, Description=des, Category_Image=file)
    messages.success(req,"category details updated successfully")
    return redirect(category_display)

def category_delete(req,dataid):
    Category = CategoryDB.objects.filter(id=dataid)
    Category.delete()
    messages.success(req,"category details deleted successfully")
    return redirect(category_display)


# ----------------

def product_page(req):
    Category = CategoryDB.objects.all()
    return render(req,"AddProduct.html",{'Category':Category})

def product_save(req):
    if req.method =="POST":
        ct_n = req.POST.get('ct_name')
        pn = req.POST.get('p_name')
        de = req.POST.get('descr')
        pr = req.POST.get('price')
        pimg = req.FILES['p_image']
        obj = ProductDB(Category_name=ct_n, Product_Name=pn, Descriptio_n=de, Price=pr, Product_Image=pimg)
        obj.save()
        messages.success(req,"product details saved successfully")
        return redirect(product_page)

def product_display(req):
    Product = ProductDB.objects.all()
    return render(req,"DisplayProduct.html",{'Product':Product})

def product_edit(req,dataid):
    Product = ProductDB.objects.get(id=dataid)
    Category = CategoryDB.objects.all()
    return render(req,"EditProduct.html",{'Product':Product, 'Category':Category})

def product_update(req,dataid):
    if req.method == "POST":
        ct_n = req.POST.get('ct_name')
        pn = req.POST.get('p_name')
        de = req.POST.get('descr')
        pr = req.POST.get('price')
        try:
            pimg = req.FILES['p_image']
            fs = FileSystemStorage()
            file = fs.save(pimg.name,pimg)
        except MultiValueDictKeyError:
            file = ProductDB.objects.get(id=dataid).Product_Image
    ProductDB.objects.filter(id=dataid).update(Category_name=ct_n, Product_Name=pn, Descriptio_n=de, Price=pr, Product_Image=file)
    messages.success(req,"product details updated successfully")
    return redirect(product_display)

def product_delete(req,dataid):
    Product = ProductDB.objects.filter(id=dataid)
    Product.delete()
    messages.success(req,"product details deleted successfully")
    return redirect(product_display)


# -----------------

def admin_login(req):
    return render(req,"AdminLogin.html")

def adminlogin(request):
    if request.method =="POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')

        if User.objects.filter(username__contains=un).exists():
            user = authenticate(username=un, password=pwd)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pwd
                return redirect(index_page)
            else:
                return redirect(admin_login)
        else:
            return redirect(admin_login)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(admin_login)

# -----
def display_contact(request):
    Contact = ContactDB.objects.all()
    return render(request,"ViewContact.html",{'Contact':Contact})