from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, get_object_or_404
from django.forms import ModelForm
from django import forms
from django.contrib.auth.decorators import login_required
from theme.templatetags.auth_extras import group_required
from django.utils import timezone
from django.db.models import Q
from decimal import Decimal

from .models import Auction, Bid, Batch

class AuctionForm(ModelForm):   
    class Meta:
        model = Auction
        fields = ['start_date', 'end_date', 'batch', 'min_value', 
                    'min_bid_increase_value', 'register_fee_paid', 'buy_fee_paid']

    def clean(self):
        now = timezone.now()
        start_date = self.cleaned_data.get('start_date')
        end_date = self.cleaned_data.get('end_date')
        if start_date >= end_date:
            raise ValidationError(
                'A data de fim deve ser depois da data de início',
            )
        if now > end_date and self.creating:
            raise ValidationError(
                'A data e horário de fim não devem ser antes de agora',
            )
    
        return self.cleaned_data

    def __init__(self, creating, *args, **kwargs):
        self.creating = creating
        super(AuctionForm, self).__init__(*args, **kwargs)
        self.fields["batch"].queryset = Batch.objects.filter(Q(auction__id__isnull=True) | Q(auction__id=self.instance.pk))


def is_bid_valid(bid_value, auction: Auction):
        if auction.end_date < timezone.now():
            return False
        if not auction.winner:
            return bid_value >= auction.min_value + auction.min_bid_increase_value
        else:
            if auction.winner_bid and auction.min_bid_increase_value:
                return bid_value >= auction.winner_bid + auction.min_bid_increase_value
            return True

def calculate_register_fee(batch: Batch):
        if batch.reserve_value <= 1000:
            return batch.reserve_value * Decimal(0.01)
        elif batch.reserve_value > 1000 and batch.reserve_value <= 10000:
            return batch.reserve_value * Decimal(0.02)
        elif batch.reserve_value > 10000 and batch.reserve_value <= 50000:
            return batch.reserve_value * Decimal(0.03)
        else:
            return batch.reserve_value * Decimal(0.04)

def calculate_buy_fee(batch: Batch, bid_value: float):
        if batch.reserve_value <= 1000:
            return bid_value * Decimal(0.03)
        elif batch.reserve_value > 1000 and batch.reserve_value <= 10000:
            return bid_value * Decimal(0.04)
        elif batch.reserve_value > 10000 and batch.reserve_value <= 50000:
            return bid_value * Decimal(0.05)
        else:
            return bid_value * Decimal(0.06)

class BidForm(ModelForm):      
    def clean_value(self):
        data = self.cleaned_data.get('value')
        if not is_bid_valid(data, self.auction):
            raise forms.ValidationError('O valor do lance é inválido.')

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
    for auction in auction_list:
        auction.bids_count = Bid.objects.filter(auction__id__exact=auction.id).count()
    now = timezone.now()
    return render(request, 'auctions/auction_list.html', {'auction_list': auction_list, 'now': now})

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def auction_create(request):
    form = AuctionForm(True, request.POST or None)

    if form.is_valid():
        fs = form.save(commit=False)
        fs.auctioneer = request.user
        fs.winner_bid = fs.min_value        
        fs.register_fee = calculate_register_fee(Batch.objects.get(pk=fs.batch.pk))
        fs.save()
        return redirect('auctions:auction_list')

    return render(request, 'auctions/auction_form.html', {'form': form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def auction_update(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    form = AuctionForm(False, request.POST or None, instance=auction)
    
    if form.is_valid():
        form.save()
        return redirect('auctions:auction_list')
    return render(request, 'auctions/auction_form.html', {'form':form})

@login_required(login_url='/auth/login/')
@group_required('admin', 'auctioneer')
def auction_finish(request, pk):
    auction = get_object_or_404(Auction, pk=pk)
    auction.end_date = timezone.now()
    auction.save()
    return redirect('auctions:auction_list')

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
        fs.datetime = timezone.now()
        fs.save()

        auction.winner = request.user
        auction.winner_bid = fs.value
        auction.winner_bid_id = fs.id
        auction.buy_fee = calculate_buy_fee(Batch.objects.get(pk=auction.batch.id), fs.value)
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