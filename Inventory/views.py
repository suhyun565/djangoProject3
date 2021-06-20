from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from Inventory.filters import productFilter
from Inventory.forms import itemForm
from speedracer.models import Product, Order


def list_item(request):
    items = Inventory.objects.all()
    order = Order.objects.all()
    total_items = items.count()
    prods = Product.objects.all()
    context = {
        'items': items, 'prods': prods, 'total_items':total_items
    }
    return render(request, 'accounts/list_items.html',context )


def create_item(request):
    prod = Product.objects.all()
    order = Order.objects.all()
    form = itemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/suhyun/inventory')
    return render(request,'accounts/create_item.html', {'prod':prod,'order':order,'form': form})



def update_item(request, id):
    item = Inventory.objects.get(id=id)
    form = itemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('/suhyun/inventory')

    return render(request, 'accounts/item_form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Inventory.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('/suhyun/inventory/')

    return render(request, 'accounts/item_delete_confirm.html', {'item': item})


def search_basic(request):
    if 'q' in request.GET:
        q = request.GET['q']
        message = 'You searched for: %r' % request.GET['q']
        items = Inventory.objects.filter(product_location__icontains=q)

    else:
        message = 'You submitted an empty form.'
    return render(request, 'accounts/list_items.html', {'message': message, 'items': items})



def search(request):
    item_list = Product.objects.all()
    items = productFilter(request.GET, queryset=item_list)
    return render(request, 'accounts/test_item.html', {'filter': items})

def viewbar(request):
    items = Inventory.objects.all()
    return render(request, 'chart/viewbar.html', {'items': items})
