from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import OrderForm, CreateUserForm
from .forms import UserUpdateForm, ProfileUpdateForm
from Accounts.models import CustomerProfile
from front.settings import AUTH_USER_MODEL
#from django.contrib.auth import get_user_model
# User = get_user_model()

#from .filters import OrderFilter

# Create your views here.



@login_required(login_url='login')
def index(request):
    #category = Category.objects.all()
    current_user = request.user  # Access User Session information
    profile = CustomerProfile.objects.get(user_id=current_user.id)
    context = {#'category': category,
               'profile': profile,
                }
    
    return render(request, 'user/dashboard-settings.html', context)

@property
def get_photo_url(self):
    if self.profile and hasattr(self.image, 'url'):
        return self.image.url
    else:
        return self.image.url('static/images/user.jpg')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                #user.is_customer = True
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                usera = authenticate(username=username, password=password)
                login(request, usera)
                # Create data in profile table for user
                current_user = request.user
                data=CustomerProfile()
                data.user_id=current_user.id
                data.save()
                messages.success(request, 'Your account has been created!')
                return HttpResponseRedirect('/')
            

        context = {'form':form}
        return render(request, 'user/account-signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Username OR password is incorrect')
    
        context = {}
        return render(request, 'user/account-signin.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')



### user update ####

@login_required(login_url='/login') # Check login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('user/')
    else:
        #category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model -> OneToOneField relatinon with user
        context = {
            #'category': category,
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'user/dashboard-settings.html', context)


@login_required(login_url='/login') # Check login
def user_orders(request):
    context = {}

    return render(request, 'user/dashboard-purchases.html')

@login_required(login_url='/login') # Check login
def user_favorites(request):
    context = {}

    return render(request, 'user/dashboard-favorites.html')



# @login_required(login_url='login')
# def home(request):
#     #orders = Order.objects.all()
#     #customers = Customer.objects.all()

#     #total_customers = customers.count()

#     #total_orders = orders.count()
#     #delivered = orders.filter(status='Delivered').count()
#     #pending = orders.filter(status='Pending').count()

#     #context = {'orders':orders, 'customers':customers,
#     #'total_orders':total_orders,'delivered':delivered,
#     #'pending':pending }

#     return render(request, 'accounts/dashboard.html', context)

# @login_required(login_url='login')
# def products(request):
#     #@products = Product.objects.all()

#     return render(request, 'accounts/products.html', {'products':products})

# @login_required(login_url='login')
# def customer(request, pk_test):
#     #customer = Customer.objects.get(id=pk_test)

#     #orders = customer.order_set.all()
#     #order_count = orders.count()

#     #myFilter = OrderFilter(request.GET, queryset=orders)
#     orders = myFilter.qs 

#     context = {'customer':customer, 'orders':orders, 'order_count':order_count,    'myFilter':myFilter}
#     return render(request, 'accounts/customer.html',context)

# @login_required(login_url='login')
# def createOrder(request, pk):
#     OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
#     #customer = Customer.objects.get(id=pk)
#     #formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
#     #form = OrderForm(initial={'customer':customer})
#     if request.method == 'POST':
#         #print('Printing POST:', request.POST)
#         #form = OrderForm(request.POST)
#         formset = OrderFormSet(request.POST, instance=customer)
#         if formset.is_valid():
#             formset.save()
#             return redirect('/')

#     context = {'form':formset}
#     return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def updateOrder(request, pk):

#     order = Order.objects.get(id=pk)
#     form = OrderForm(instance=order)

#     if request.method == 'POST':
#         form = OrderForm(request.POST, instance=order)
#         if form.is_valid():
#             form.save()
#             return redirect('/')

#     context = {'form':form}
#     return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def deleteOrder(request, pk):
#     order = Order.objects.get(id=pk)
#     if request.method == "POST":
#         order.delete()
#         return redirect('/')

#     context = {'item':order}
#     return render(request, 'accounts/delete.html', context)

