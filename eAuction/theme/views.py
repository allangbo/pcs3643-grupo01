from django.shortcuts import render

from auctions.models import Auction



def home(request):
    auction_list = Auction.objects.order_by('id')
    
    return render(request, 'theme/home.html', {'auction_list': auction_list})
