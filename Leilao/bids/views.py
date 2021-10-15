from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from .models import Bid

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['value', 'auction_id']

def bid_list(request, template_name='bids/bid_list.html'):
    bid = Bid.objects.all()
    data = {}
    data['object_list'] = bid
    return render(request, template_name, data)

def bid_create(request, template_name='bids/bid_form.html'):
    form = BidForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('bids:bid_list')
    return render(request, template_name, {'form':form})

def bid_update(request, pk, template_name='bids/bid_form.html'):
    bid= get_object_or_404(Bid, pk=pk)
    form = BidForm(request.POST or None, instance=bid)
    if form.is_valid():
        form.save()
        return redirect('bids:bid_list')
    return render(request, template_name, {'form':form})

def bid_delete(request, pk, template_name='bids/bid_confirm_delete.html'):
    bid= get_object_or_404(Bid, pk=pk)    
    if request.method=='POST':
        bid.delete()
        return redirect('bids:bid_list')
    return render(request, template_name, {'object':bid})