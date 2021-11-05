from django.shortcuts import redirect, render, get_object_or_404
from django.forms import ModelForm
from .models import Product
from theme.templatetags.auth_extras import group_required
from django.contrib.auth.decorators import login_required

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer', 'seller-buyer')
def product_list(request):
    if request.user.groups.filter(name__in=['admin', 'auctioneer']) or request.user.is_superuser:
        product_list = Product.objects.all().order_by('id')
    else:
        product_list = Product.objects.filter(seller=request.user).order_by('id')

    return render(request, 'products/product_list.html', {'product_list': product_list})

@login_required(login_url='/auth/login/')
@group_required('admin', 'seller-buyer')
def product_create(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        fs = form.save(commit=False)
        fs.seller = request.user
        fs.save()
        return redirect('products:product_list')
    return render(request, 'products/product_form.html', {'form': form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'seller-buyer')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('products:product_list')
    return render(request, 'products/product_form.html', {'form':form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'seller-buyer')
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)  
    product.delete()        
    return redirect("products:product_list")