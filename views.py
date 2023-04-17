from django.shortcuts import render, redirect
from .models import Products
from django.db.models import F
from .forms import ProductsForm
from django.contrib.auth.decorators import login_required


def main(request):
    return render(request, 'main.html',)


@login_required
def my_pantry(request):
    user = request.user.id
    products = Products.objects.filter(user_id=user).order_by('name')

    context={
        'products':products,
    }
    return render(request, 'my_pantry.html' ,context)


@login_required
def to_kitchen(request, pk):
    user = request.user.id
    pk_product = Products.objects.get(id=pk)
    quty = int(request.POST['quty'])
    pk_product.quty -= quty
    pk_product.save()

    products = Products.objects.filter(user_id=user).order_by('name')
   
    context={
            'products':products,
            }
    
    return render(request, 'my_pantry.html', context)


@login_required
def go_shopping(request):
    user = request.user.id
    for_safety = Products.objects.filter(user_id=user, quty__lte=F("sefty"))
    listbuy=dict()
    varisempty=1

    if len(for_safety) == 0:
        tobuy = 1
        varisempty=0

    else:
        for i in for_safety:
            tobuy = i.sefty - i.quty
            name = i.name
            if tobuy > 0:
                listbuy[name]=tobuy
    
    context={
        'varisempty': varisempty,
        'for_safety':for_safety,
        'tobuy':tobuy,
        'listbuy':listbuy,
    }
    return render(request, 'go_shopping.html', context)


@login_required
def with_shopping(request):
    user = request.user.id
    for_safety = Products.objects.filter(user_id=user, quty__lte=F("sefty"))
    contents_basket=[]
    varisempty=1

    for i in for_safety:
        if i.sefty-i.quty > 0:
            contents_basket.append(i)
    print(f" to jest nowy koszyk: {contents_basket}")
        

    if len(contents_basket) == 0:
        varisempty=0
    
    context={
        'varisempty':varisempty,
        'contents_basket':contents_basket,
    }
    print(varisempty)
    return render(request, 'with_shopping.html', context)


@login_required
def action_shopping(request, pk):
    user = request.user.id
    pk_product = Products.objects.get(id=pk)
    quty = int(request.POST['quty'])

    pk_product.quty += quty
    pk_product.save()

    for_safety = Products.objects.filter(user_id=user, quty__lte=F("sefty"))

    context={
        'for_safety':for_safety
    }

    return render(request, 'with_shopping.html', context)


@login_required
def adding(request):

    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/my_pantry') 
    else:
        form = ProductsForm()

    return render(request, 'add.html', {'form':form})


@login_required
def update(request, pk):
    pk_product = Products.objects.get(id=pk)
    form = ProductsForm(instance=pk_product)

    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=pk_product)
        if form.is_valid():
            form.save()
            return redirect('/my_pantry')
        
    context={
        'pk_product':pk_product,
        'form':form
        }
    return render(request, 'update.html', context)


@login_required
def delete(request, pk):
    pk_product = Products.objects.get(id=pk)

    if request.method == 'POST':
        pk_product.delete()
        return redirect('/my_pantry')

    context={
        'pk_product':pk_product
    }
    return render(request, 'delete.html', context)
