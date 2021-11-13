from django.shortcuts import redirect, render, get_object_or_404
from django.forms import ModelForm
from theme.templatetags.auth_extras import group_required
from django.contrib.auth.decorators import login_required

from .models import Batch

class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ['description', 'value', 'reserve_value', 'products']
        
@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer', 'seller-buyer')
def batch_list(request):
    if request.user.groups.filter(name__in=['admin', 'auctioneer']) or request.user.is_superuser:
        batch_list = Batch.objects.all().order_by('id')
    else:
        batch_list = Batch.objects.filter(seller=request.user).order_by('id')
    return render(request, 'batches/batch_list.html', {'batch_list': batch_list})

@login_required(login_url='/auth/login/')
@group_required('admin', 'seller-buyer')
def batch_create(request):
    form = BatchForm(request.POST or None)

    if form.is_valid():
        fs = form.save(commit=False)
        fs.seller = request.user
        fs.save()
        form.save_m2m()
        return redirect('batches:batch_list')

    return render(request, 'batches/batch_form.html', {'form': form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'seller-buyer')
def batch_update(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    form = BatchForm(request.POST or None, instance=batch)
    
    if form.is_valid():
        form.save()
        return redirect('batches:batch_list')
    return render(request, 'batches/batch_form.html', {'form':form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'seller-buyer')
def batch_delete(request, pk):
    batch = get_object_or_404(Batch, pk=pk)  
    batch.delete()        
    return redirect("batches:batch_list")
