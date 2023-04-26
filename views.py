from django.shortcuts import render, redirect
from .models import Products, Kategoria
from django.db.models import F
from .forms import ProductsForm, KategoriaForm
from django.contrib.auth.decorators import login_required



def main(request):
    return render(request, 'main.html',)


@login_required
def my_pantry(request):
    user = request.user.id
    products = Products.objects.filter(user_id=user).order_by('name')
    m_category = Kategoria.objects.filter(user_id=user).order_by('cate')

    context={
        'products':products,
        'm_category':m_category,
    }
    return render(request, 'my_pantry.html' ,context)

@login_required
def select_category(request):
    id_cate_f=0
    user=request.user.id
    m_category = Kategoria.objects.filter(user_id=user).order_by('cate')

    if request.method == "POST":
        print("udało się kórka wodna")
        id_cate_f = int(request.POST.get('Cate_ID', 0))
            
    else:
        id_cate_f = 0

    if id_cate_f == 0:
        products = Products.objects.filter(user_id=user).order_by('name')
    else:
        products = Products.objects.filter(user_id=user, category_id=id_cate_f).order_by('name')

    context = {
        'products':products,
        'm_category':m_category,
    }

    return render(request, 'my_pantry.html', context)

@login_required
def to_kitchen(request, pk):
    user = request.user.id
    pk_product = Products.objects.get(id=pk)
    quty = int(request.POST['quty'])
    print(f" test prosty bo głupieje =======================================> {quty}")
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
    for_safety = Products.objects.filter(user_id=user).order_by('name')
    
    context={
        'for_safety':for_safety
    }
    
    return render(request, 'with_shopping.html', context)


@login_required
def action_shopping(request, pk):
    user = request.user.id
    pk_product = Products.objects.get(id=pk)

    quty = int(request.POST['quty'])

    pk_product.quty += quty
    pk_product.save()

    for_safety = Products.objects.filter(user_id=user).order_by('name')

    context={
        'for_safety':for_safety
    }

    return render(request, 'with_shopping.html', context)


@login_required
def adding(request):
    
    if request.method == "POST":
        form = ProductsForm(request.user, request.POST)
        if form.is_valid():
            formularzwypelniony = form.save(commit=False)
            formularzwypelniony.user = request.user
            formularzwypelniony.save()
            return redirect('/with') 
    else:
        form = ProductsForm(request.user)

    return render(request, 'add.html', {'form':form})


@login_required
def update(request, pk):
    user = request.user.id
    pk_product = Products.objects.get(id=pk)
    form = ProductsForm(request.user, instance=pk_product)

    if request.method == 'POST':
        form = ProductsForm(request.user, request.POST, instance=pk_product)
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

@login_required
def my_category(request):
    user = request.user.id
    category = Kategoria.objects.filter(user_id=user).order_by('cate')

    context={
        'category': category,
    }
    return render(request, 'category.html' ,context)

@login_required
def add_category(request):

    if request.method == "POST":
        form = KategoriaForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/category') 
    else:
        form = KategoriaForm()

    return render(request, 'add_cate.html', {'form':form})

@login_required
def delete_cate(request, pk):
    pk_cate = Kategoria.objects.get(id=pk)

    if request.method == 'POST':
        pk_cate.delete()
        return redirect('/category')

    context={
        'pk_cate':pk_cate
    }
    return render(request, 'delete_cate.html', context)

@login_required
def update_cate(request, pk):
    pk_cate = Kategoria.objects.get(id=pk)
    form = KategoriaForm(instance=pk_cate)

    if request.method == 'POST':
        form = KategoriaForm(request.POST, instance=pk_cate)
        if form.is_valid():
            form.save()
            return redirect('/category')
        
    context={
        'pk_cate':pk_cate,
        'form':form
        }
    return render(request, 'update.html', context)