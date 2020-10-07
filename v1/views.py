from django.shortcuts import render
from Accounts.models import CustomerProfile
# Create your views here.

def index(request):

    if request.user.is_authenticated:
        current_user = request.user # Access User Session information
        profile = CustomerProfile.objects.get(user_id=current_user.id)
        context = {#'category': category,
               'profile': profile}
        return render(request, 'v1/index.html', context)
    else:
        context = {}
        return render(request, 'v1/index.html', context)

def cart(request):
    context = {}
    return render(request, 'v1/cart.html', context)

def checkoutdetails(request):
    context = {}
    return render(request, 'v1/checkout_details.html', context)

def checkoutshipping(request):
    context = {}
    return render(request, 'v1/checkout_shipping.html', context)


def checkoutreview(request):
    context = {}
    return render(request, 'v1/checkout_review.html', context)


def checkoutpayments(request):
    context = {}
    return render(request, 'v1/checkout_payments.html', context)

def ordertracking(request):
    context = {}
    return render(request, 'v1/ordertracking.html', context)

def single(request):
    context = {}
    return render(request, 'v1/single.html', context)

def checkoutcomplete(request):
    context = {}
    return render(request, 'v1/checkout_complete.html')