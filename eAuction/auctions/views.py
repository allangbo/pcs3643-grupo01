from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import login_required
from theme.templatetags.auth_extras import group_required
from datetime import datetime
from django.utils import timezone

from .models import Auction, Bid

class AuctionForm(ModelForm):   
    class Meta:
        model = Auction
        fields = ['start_date', 'end_date', 'batch', 'min_value', 
                    'min_bid_increase_value', 'register_fee', 'register_fee_paid']

    def clean(self):
        now = timezone.now()
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date > end_date:
            raise ValidationError(
                'A data de fim deve ser depois da data de início',
            )
        if now > end_date:
            raise ValidationError(
                'A data e horário de fim não devem ser antes de agora',
            )
        return self.cleaned_data

def is_bid_valid(bid_value, auction: Auction):
        if auction.end_date < datetime.today().date():
            return False
        if not auction.winner:
            return bid_value >= auction.min_value
        else:
            if auction.winner_bid and auction.min_bid_increase_value:
                return bid_value >= auction.winner_bid + auction.min_bid_increase_value
            return True

class BidForm(ModelForm):      
    def clean_value(self):
        data = self.cleaned_data.get('value')
        if not is_bid_valid(data, self.auction):
            raise forms.ValidationError('Bid value is not valid.')

        return data

    def __init__(self, auction, *args, **kwargs):
        self.auction = auction
        super(BidForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Bid
        fields = ['value']
        
@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def auction_list(request):
    auction_list = Auction.objects.order_by('id')
    return render(request, 'auctions/auction_list.html', {'auction_list': auction_list})

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def auction_create(request):
    form = AuctionForm(request.POST or None)

    if form.is_valid():
        fs = form.save(commit=False)
        fs.auctioneer = request.user
        fs.save()
        return redirect('auctions:auction_list')

    return render(request, 'auctions/auction_form.html', {'form': form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def auction_update(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    form = AuctionForm(request.POST or None, instance=auction)
    
    if form.is_valid():
        form.save()
        return redirect('auctions:auction_list')
    return render(request, 'auctions/auction_form.html', {'form':form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def auction_delete(request, pk):
    auction = get_object_or_404(Auction, pk=pk)  
    auction.delete()        
    return redirect("auctions:auction_list")

@login_required(login_url='/auth/login/')
@group_required('admin', 'seller-buyer')
def bid_create(request, auction_id):    
    auction = get_object_or_404(Auction, pk=auction_id)
    form = BidForm(auction, request.POST or None)

    if form.is_valid():        
        fs = form.save(commit=False)
        fs.buyer = request.user
        fs.auction = auction
        fs.datetime = datetime.now()
        fs.save()

        auction.winner = request.user
        auction.winner_bid = fs.value
        auction.winner_bid_id = fs.id
        auction.save()
        return redirect('theme:home')
    return render(request, 'auctions/bid_form.html', {'form': form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer', 'seller-buyer')
def bid_list(request):
    if request.user.groups.filter(name__in=['admin', 'auctioneer']) or request.user.is_superuser:
        bid_list = Bid.objects.all().order_by('id')
    else:
        bid_list = Bid.objects.filter(buyer=request.user).order_by('id')
    
    return render(request, 'auctions/bid_list.html', {'bid_list': bid_list})