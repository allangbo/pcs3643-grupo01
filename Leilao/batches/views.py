from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Batch

class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields = ['reserve_value','value','fee','register_fee','payed','sequential_number','min_value','min_bid_increase_value','seller_id']

def batch_list(request, template_name='batches/batch_list.html'):
    batch = Batch.objects.all()
    data = {}
    data['object_list'] = batch
    return render(request, template_name, data)

def batch_create(request, template_name='batches/batch_form.html'):
    form = BatchForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('batches:batch_list')
    return render(request, template_name, {'form':form})

def batch_update(request, pk, template_name='batches/batch_form.html'):
    batch= get_object_or_404(Batch, pk=pk)
    form = BatchForm(request.POST or None, instance=batch)
    if form.is_valid():
        form.save()
        return redirect('batches:batch_list')
    return render(request, template_name, {'form':form})

def batch_delete(request, pk, template_name='batches/batch_confirm_delete.html'):
    batch= get_object_or_404(Batch, pk=pk)    
    if request.method=='POST':
        batch.delete()
        return redirect('batches:batch_list')
    return render(request, template_name, {'object':batch})