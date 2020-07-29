from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from .views import *


def inventory(request):
    return render(request, 'inventory/index.html')


def display_accessory(request):
    items = Product.objects.filter(category=1)
    context = {
        'items': items,
        'header': 'Accessory',
    }
    return render(request, 'inventory/index.html', context)


def display_oil(request):
    items = Product.objects.filter(category=2)
    context = {
        'items': items,
        'header': 'OIL',
    }
    return render(request, 'inventory/index.html', context)


def display_3m(request):
    items = Product.objects.all()
    context = {
        'items': items,
        'header': '3M',
    }
    return render(request, 'inventory/index.html', context)


def display_others(request):
    items = Product.objects.all()
    context = {
        'items': items,
        'header': 'Others',
    }
    return render(request, 'inventory/index.html', context)


def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inventory')

    else:
        form = cls()
        return render(request, 'inventory/add_new.html', {'form': form})


def add_accessory(request):
    return add_item(request, AccessoryForm)


def add_oil(request):
    return add_item(request, OilForm)


def add_3m(request):
    return add_item(request, M3Form)


def add_others(request):
    return add_item(request, OthersForm)


def edit_device(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)
    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory')
    else:
        form = cls(instance=item)
        return render(request, 'inventory/edit_item.html', {'form': form})


def edit_accessory(request, pk):
    return edit_device(request, pk, Product, AccessoryForm)


def edit_oil(request, pk):
    return edit_device(request, pk, Product, OilForm)


def edit_3m(request, pk):
    return edit_device(request, pk, Product, M3Form)


def edit_others(request, pk):
    return edit_device(request, pk, Product, OthersForm)


def delete_accessory(request, pk):
    template = 'inventory/index.html'
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_oil(request, pk):
    template = 'inventory/index.html'
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_3m(request, pk):

    template = 'inventory/index.html'
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_others(request, pk):

    template = 'inventory/index.html'
    Product.objects.filter(id=pk).delete()
    items = Product.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
