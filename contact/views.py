from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib import messages
# import django_filters import OrderFilter


from .models import ContactLink, About
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter    


class ContactView(View):
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {"contacts": contacts, "form": form})


class CreateContact(CreateView):
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {"about": about})


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
		context = {'form':form}
		return render(request, 'register.html', context)


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


# @login_required(login_url='login')
# def home(request):
# 	orders = Order.objects.all()
# 	customers = Customer.objects.all()

# 	total_customers = customers.count()

# 	total_orders = orders.count()
# 	delivered = orders.filter(status='Delivered').count()
# 	pending = orders.filter(status='Pending').count()

# 	context = {'orders':orders, 'customers':customers,
# 	'total_orders':total_orders,'delivered':delivered,
# 	'pending':pending }

# 	return render(request, 'accounts/dashboard.html', context)

# @login_required(login_url='login')
# def products(request):
# 	products = Product.objects.all()

# 	return render(request, 'accounts/products.html', {'products':products})

# @login_required(login_url='login')
# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
# 	order_count = orders.count()

# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs 

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)

# @login_required(login_url='login')
# def createOrder(request, pk):
# 	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
# 	customer = Customer.objects.get(id=pk)
# 	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = OrderForm(request.POST)
# 		formset = OrderFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def updateOrder(request, pk):

# 	order = Order.objects.get(id=pk)
# 	form = OrderForm(instance=order)

# 	if request.method == 'POST':
# 		form = OrderForm(request.POST, instance=order)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == "POST":
# 		order.delete()
# 		return redirect('/')

# 	context = {'item':order}
# 	return render(request, 'accounts/delete.html', context)


# {% load static %}
  # <style>
  #   .hello-msg{
  #     font-size: 18px;
  #     color: #fff;
  #     margin-right: 20px;
  #   }
  # </style>

#   <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
#     </button>
#     <div class="collapse navbar-collapse" id="navbarNav">
#     </div>
#     <span class="hello-msg">Hello, {{request.user}}</span>
#     <span ><a  class="hello-msg" href="{% url 'logout' %}">Logout</a></span>
#   </nav>