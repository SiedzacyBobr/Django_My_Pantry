from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Products
from django.db.models import F
from .forms import ProductsForm, QuantityForm, LiczbaForm


def main(request):
    return render(request, 'main.html')

def my_pantry(request):
    products = Products.objects.all().order_by('name')
   
    context={
        'products':products,
    }
    return render(request, 'my_pantry.html' ,context)

def with_shopping(request):
    for_safety = Products.objects.filter(quty__lte=F("sefty"))
    

    context={
        'for_safety':for_safety,
        
    }

    return render(request, 'with_shopping.html', context)

def adding(request):
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/my_pantry') 
            except:
                pass
    else:
        form = ProductsForm()
    return render(request, 'add.html', {'form':form})

def update(request, pk):
    pk_product = Products.objects.get(id=pk)
    form = ProductsForm(instance=pk_product)

    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=pk_product)
        if form.is_valid():
            form.save()
            return redirect('/my_pantry')
        
    context = {'pk_product':pk_product,
               'form':form}
    
    return render(request, 'update.html', context)

def delete(request, pk):
    pk_product = Products.objects.get(id=pk)

    if request.method == 'POST':
        pk_product.delete()
        return redirect('/my_pantry')
    
    context = {
        'pk_product':pk_product
    }
    return render(request, 'delete.html', context)

def go_shopping(request):
    for_safety = Products.objects.filter(quty__lte=F("sefty"))
    print(for_safety)

    listbuy=dict()
    print(listbuy)

    for i in for_safety:
        tobuy = i.sefty - i.quty
        name = i.name
        listbuy[name]=tobuy
        
    print(listbuy)
    
    context={
        'for_safety':for_safety,
        'tobuy':tobuy,
        'listbuy':listbuy,
    }

    return render(request, 'go_shopping.html', context)

#===================================================================

def to_kitchen(request, pk):
    pk_product = Products.objects.get(id=pk)
    max_value = pk_product.quty
    print(f"udało się max_vaule = {max_value}")
    
    if request.method=="POST":
        print("0 udało się ")
        form = QuantityForm(request.POST, max_value=pk_product.quty, instance=pk_product)
        print("1 udało się ")
        if form.is_valid():
            enter_varible = form.cleaned_data['quty']
            pk_product.quty -= enter_varible
            pk_product.save()
            print("udało się koniec")
            return redirect('/my_pantry')
            
    else:
        form = QuantityForm(max_value=max_value, instance=pk_product)

    context={
        'form':form,
        'pk_product':pk_product,
        }
    
    return render(request, 'to_kitchen.html', context)

#===============================================================