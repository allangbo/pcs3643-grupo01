from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Seller

class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = ['name', 'cpf']

def seller_list(request, template_name='sellers/seller_list.html'):
    seller = Seller.objects.all()
    data = {}
    data['object_list'] = seller
    return render(request, template_name, data)

def seller_create(request, template_name='sellers/seller_form.html'):
    form = SellerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sellers:seller_list')
    return render(request, template_name, {'form':form})

def seller_update(request, pk, template_name='sellers/seller_form.html'):
    seller= get_object_or_404(Seller, pk=pk)
    form = SellerForm(request.POST or None, instance=seller)
    if form.is_valid():
        form.save()
        return redirect('sellers:seller_list')
    return render(request, template_name, {'form':form})

def seller_delete(request, pk, template_name='sellers/seller_confirm_delete.html'):
    seller= get_object_or_404(Seller, pk=pk)    
    if request.method=='POST':
        seller.delete()
        return redirect('sellers:seller_list')
    return render(request, template_name, {'object':seller})