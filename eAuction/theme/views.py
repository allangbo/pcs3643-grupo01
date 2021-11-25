from django.shortcuts import render
from django.utils import timezone

from auctions.models import Auction, Bid



def home(request):
    auction_list = Auction.objects.order_by('id')
    for auction in auction_list:
        auction.bids_count = Bid.objects.filter(auction__id__exact=auction.id).count()
    now = timezone.now()
    return render(request, 'theme/home.html', {'auction_list': auction_list, 'now': now})
