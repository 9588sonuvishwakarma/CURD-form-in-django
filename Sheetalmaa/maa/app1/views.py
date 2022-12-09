from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import Product
from .models import Order
from .models import  Customer
from .models import OrderForm
from .models import Name
from .models import Fast
from .models import oom

def home(request):
    order = Order.objects.all()
    customers = Customer.objects.all()
    names = Name.objects.all()
    fasts = Fast.objects.all()
    om = oom.objects.all()

    total_customers = customers.count()
    total_order = order.count()
    total_name = names.count()
    delivered = order.filter(status='Delivered').count()
    pending = order.filter(status='pending').count()
    outdeliver = order.filter(status='out for delivery').count()
    context = {'order': order, 'customers': customers,'total_customers':total_customers, 'total_order':total_order,'delivered':delivered,'pending':pending,'outdeliver':outdeliver,'names':names,
               'fasts':fasts,'total_name':total_name}

    return render(request,'dash.html',context)

def product(request):
    products = Product.objects.all()
    return render(request,'pro.html',{'products':products})

def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    # myFilter = OrderFilter()
    context = {'customer':customer,'orders':orders,'order_count':order_count}
    return render(request,'cus.html',context)

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #('printing post:',requset.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'order_form.html',context)

def updateOrder(request,pk):
    # form = OrderForm()
    order =Order.objects.get(id=pk) # to fetch the data from the order
    form = OrderForm(instance=order)
    if request.method == 'POST': # when you press submit then it work

        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect(('/'))
    context = {'form':form}
    return render(request, 'order_form.html',context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":


        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request,'delete.html',context)
# def pros(request):
#      om = oom.objects.all()
#     # om = oom.objects.get(pk)
#     # context={'om':om}
#     return render(request,'proo.html')