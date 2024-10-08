from django.shortcuts import render, redirect
from .models import Supplier, Product, Customer, Car
from django.contrib.auth import authenticate, login, logout

# #LANDING AFTER LOGIN
# def landingview(request):
#      return render (request, "landingpage.html")

#LOGIN AND LOGOUT
def loginview(request):
     return render (request, "loginpage.html")

# Login action
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')


# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')


#Product views
def productlistview(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        productlist = Product.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'products': productlist, 'suppliers': supplierlist}
        return render (request,"productlist.html",context)

def addproduct(request):
        a = request.POST['productname']
        b = request.POST['packagesize']
        c = request.POST['unitprice']
        d = request.POST['unitsinstock']
        e = request.POST['supplier']
        Product(productname = a, packagesize = b, unitprice = c, unitsinstock = d, supplier = Supplier.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])


def confirmdeleteproduct(request, id):
    product = Product.objects.get(id = id)
    context = {'product': product}
    return render (request,"confirmdelprod.html",context)


def deleteproduct(request, id):
    Product.objects.get(id = id).delete()
    return redirect(productlistview)


def edit_product_get(request, id):
        product = Product.objects.get(id = id)
        context = {'product': product}
        return render (request,"edit_prod.html",context)


def edit_product_post(request, id):
        item = Product.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(productlistview)

def products_filtered(request, id):
    productlist = Product.objects.all()
    filteredproducts = productlist.filter(supplier = id)
    context = {'products': filteredproducts}
    return render (request,"productlist.html",context)


# Supplier views
def supplierlistview(request):
    if not request.user.is_authenticated:
        return render (request, "loginpage.html")
    else:
        supplierlist = Supplier.objects.all()
        context = {'suppliers': supplierlist}
        return render (request,"supplierlist.html",context)

def addsupplier(request):
        a = request.POST['companyname']
        b = request.POST['contactname']
        c = request.POST['address']
        d = request.POST['phone']
        e = request.POST['email']
        f = request.POST['country']
        Supplier(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
        return redirect(request.META['HTTP_REFERER'])

def confirmdeletesupplier(request, id):
    supplier = Supplier.objects.get(id = id)
    context = {'supplier': supplier}
    return render (request,"confirmdelsupp.html",context)


def deletesupplier(request, id):
    Supplier.objects.get(id = id).delete()
    return redirect(supplierlistview)

def edit_supplier_get(request, id):
        supplier = Supplier.objects.get(id = id)
        context = {'supplier': supplier}
        return render (request,"edit_supp.html",context)

def edit_supplier_post(request, id):
        supplier = Supplier.objects.get(id = id)
        supplier.contactname = request.POST['contactname']
        supplier.address = request.POST['address']
        supplier.phone = request.POST['phone']
        supplier.email = request.POST['email']
        supplier.save()
        return redirect(supplierlistview)

def searchsuppliers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(companyname__icontains=search)
    context = {'suppliers': filtered}
    return render (request,"supplierlist.html",context)

#Customer views
def customerlistview(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        customerlist = Customer.objects.all()
        context = {'customers': customerlist }
        return render (request,"customerlist.html",context)

def addcustomer(request):
        a = request.POST['customername']
        b = request.POST['address']
        c = request.POST['phone']
        d = request.POST['email']
        e = request.POST['country']
        Customer(customername = a, address = b, phone = c, email = d, country = e).save()
        return redirect(request.META['HTTP_REFERER'])


def confirmdeletecustomer(request, id):
    customer = Customer.objects.get(id = id)
    context = {'customer': customer}
    return render (request,"confirmdelcust.html",context)


def deletecustomer(request, id):
    Customer.objects.get(id = id).delete()
    return redirect(productlistview)


def edit_customer_get(request, id):
        customer = Customer.objects.get(id = id)
        context = {'customer': customer}
        return render (request,"edit_cust.html",context)


def edit_customer_post(request, id):
        client = Customer.objects.get(id = id)
        client.address = request.POST['address']
        client.phone = request.POST['phone']
        client.email = request.POST['email']
        client.country = request.POST['country']
        client.save()
        return redirect(customerlistview)

def searchcustomers(request):
    search = request.POST['search']
    filtered = Supplier.objects.filter(customername__icontains=search)
    context = {'customers': filtered}
    return render (request,"customerlist.html",context)

# Car views
def carlistview(request):
    if not request.user.is_authenticated:
         return render(request, 'loginpage.html')
    else:
        carlist = Car.objects.all()
        supplierlist = Supplier.objects.all()
        context = {'cars': carlist, 'suppliers': supplierlist}
        return render (request,"carlist.html",context)

def addcar(request):
        a = request.POST['brand']
        b = request.POST['model']
        c = request.POST['licenseplate']
        e = request.POST['owner']
        Car(brand = a, model = b, licenseplate = c, owner = Supplier.objects.get(id = e)).save()
        return redirect(request.META['HTTP_REFERER'])


def confirmdeletecar(request, id):
    car = Car.objects.get(id = id)
    context = {'car': car}
    return render (request,"confirmdelcar.html",context)


def deletecar(request, id):
    Product.objects.get(id = id).delete()
    return redirect(carlistview)

def cars_filtered(request, id):
    carlist = Car.objects.all()
    filteredcars = carlist.filter(owner = id)
    context = {'cars': filteredcars}
    return render (request,"carlist.html",context)

