from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .forms import OrderForm
from .filters import OrderFilter
from django.contrib.auth import authenticate


@csrf_exempt
def login(request):
    if request.method == 'POST':

        print("request "+ str(request))
        print("body "+ str(request.body))
        userid = request.POST.get("userid", "")
        userpw = request.POST.get("userpw", "")
        login_result = authenticate(username=userid, password=userpw)

        print("userid = " + userid + " result = " + str(login_result))
        if login_result:
            return redirect('/suhyun/home')
        else:
            return render(request, "accounts/login.html", status = 401)

    return render(request, "accounts/login.html")

def home(request):
	orders = Order.objects.all()
	managers = Manager.objects.all()
	total_managers = managers.count()

	total_orders = orders.count()
	entering = orders.filter(status='Entering').count()
	releasing = orders.filter(status='Releasing').count()

	context = {'orders':orders, 'managers':managers,
	'total_orders':total_orders,'entering':entering,
	'releasing':releasing }

	return render(request, 'accounts/dashboard.html', context)

def products(request):
	products = Product.objects.all()
	return render(request, 'accounts/products.html', {'products':products})



def manager(request, pk_test):
	manager = Manager.objects.get(id=pk_test)

	orders = manager.order_set.all()
	order_count = orders.count()
	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs

	context = {'manager': manager, 'orders': orders, 'order_count': order_count,
			   'myFilter': myFilter}

	return render(request, 'accounts/manager.html',context)

def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Manager, Order, fields=('product', 'status','count'), extra=10)
	manager = Manager.objects.get(id=pk)
	#inventory = Inventory.objects.get(id=pk)
	#current_amount = inventory.current_amount
	#order = Order.objects.get(id=pk)
	#count = order.count


	formset = OrderFormSet(queryset=Order.objects.none(),instance=manager)
	if request.method == 'POST':
		formset = OrderFormSet(request.POST, instance=manager)
		if formset.is_valid():
			formset.save()
			return redirect('/suhyun/home/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)

from django.contrib import messages

def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/suhyun/home')

	context = {'form':form}
	return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/suhyun/home')

	context = {'item':order}
	return render(request, 'accounts/delete.html', context)


