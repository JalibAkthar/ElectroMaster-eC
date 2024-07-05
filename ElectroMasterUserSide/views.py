from django.shortcuts import render,redirect
from ElectroMasterAdminSide.models import CategoryDB,ProductDB
from ElectroMasterUserSide.models import ContactDB,LoginDB,CartDB

# Create your views here.

def home_page(request):
    Category = CategoryDB.objects.all()
    return render(request,"Home.html",{'Category':Category})


def products_page(request):
    Product = ProductDB.objects.all()
    Category = CategoryDB.objects.all()
    return render(request,"products.html",{'Product':Product,'Category':Category})

def single_product(request,proid):
    Category = CategoryDB.objects.all()
    single = ProductDB.objects.get(id=proid)
    return render(request,"single_product.html",{'Category':Category,'single':single})

def product_filtered(request,cat_name):
    pro = ProductDB.objects.filter(Category_name=cat_name)
    Category = CategoryDB.objects.all()
    return render(request,"product_filtered.html",{'pro':pro,'Category':Category})

def about_us(request):
    return render(request,"About_Us.html")

def services(request):
    return render(request,"Services.html")

def contact_us(request):
    return render(request,"Contact_Us.html")

def save_contact(request):
    if request.method =="POST":
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        em = request.POST.get('email')
        add = request.POST.get('address')
        ct = request.POST.get('city')
        cnt = request.POST.get('country')
        pin = request.POST.get('pin_code')
        mob = request.POST.get('mobile')
        obj = ContactDB(First_Name=fn, Last_Name=ln, Email=em, Address=add, City=ct, Country=cnt, Pin_Code=pin, Mobile_Number=mob)
        obj.save()
        return redirect(contact_us)

def login(request):
    return render(request,"Login.html")

def signup_save(request):
    if request.method =="POST":
        us = request.POST.get('u_sername')
        ps = request.POST.get('p_assword')
        em = request.POST.get('e_mail')
        ad = request.POST.get('text_area')
        obj = LoginDB(User_Name=us, Pass_Word=ps, Email=em, Address=ad)
        obj.save()
        return redirect(login)


def User_Login(request):
    if request.method =="POST":
        un = request.POST.get('user_name')
        pwd = request.POST.get('pass_word')
        if LoginDB.objects.filter(User_Name=un, Pass_Word=pwd).exists():
            request.session['User_Name'] = un
            request.session['Pass_Word'] = pwd
            return redirect(home_page)
        else:
            return redirect(login)
    return redirect(login)


def User_Logout(request):
    del request.session['User_Name']
    del request.session['Pass_Word']
    return redirect(login)

# -----------
def cart_page(request):
    cart = CartDB.objects.filter(USer_NAme=request.session['User_Name'])
    total_price = 0
    for i in cart:
        total_price = total_price+i.TOtal_PRice
    return render(request,"cart.html",{'cart':cart,'total_price':total_price})

def save_cart(request):
    if request.method =="POST":
        usn = request.POST.get('use_rname')
        prn = request.POST.get('pro_name')
        desr = request.POST.get('descri_ption')
        quan = request.POST.get('quan_tity')
        topr = request.POST.get('total_pr')
        obj = CartDB(USer_NAme=usn,PRoduct_NAme=prn,DEscription=desr,QUantity=quan,TOtal_PRice=topr)
        obj.save()
        return redirect(cart_page)


def delete_cart(request,dataid):
    cart = CartDB.objects.filter(id=dataid)
    cart.delete()
    return redirect(cart_page)

def check_out(request):
    cart = CartDB.objects.filter(USer_NAme=request.session['User_Name'])
    total_price = 0
    for i in cart:
        total_price = total_price+i.TOtal_PRice
    return render(request,"check_out.html",{'cart':cart,'total_price':total_price})