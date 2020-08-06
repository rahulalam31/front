from django.shortcuts import render

# Create your views here.

def sellerindex(request):
    context ={}
    return render(request, 'seller/index.html', context)

def sellerdashboard(request):
    context ={}
    return render(request, 'seller/dashboard-settings.html', context)