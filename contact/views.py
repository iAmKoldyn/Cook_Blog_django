from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from django.contrib import messages
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from .models import *
from .forms import ContactForm
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import CreateUserForm
from .serializers import *
from rest_framework import permissions




class RecipeView(View):
    def get(self, request):
        return render(request, 'contact/recipe.html')




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

# rest

class AboutList(ListAPIView):
    model = About
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutCreate(CreateAPIView):
    model = About
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AboutDetail(RetrieveAPIView):
    model = About
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class AboutUpdate(UpdateAPIView):
    model = About
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    # permission_classes = [permissions.IsAuthenticated]


class AboutDelete(DestroyAPIView):
    model = About
    queryset = About.objects.all()
    serializer_class = AboutSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ContactLinkList(ListAPIView):
    model = ContactLink
    queryset = ContactLink.objects.all()
    serializer_class = ContactLinkSerializer


class ContactLinkCreate(CreateAPIView):
    model = ContactLink
    queryset = ContactLink.objects.all()
    serializer_class = ContactLinkSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ContactLinkDetail(RetrieveAPIView):
    model = ContactLink
    queryset = ContactLink.objects.all()
    serializer_class = ContactLinkSerializer


class ContactLinkUpdate(UpdateAPIView):
    model = ContactLink
    queryset = ContactLink.objects.all()
    serializer_class = ContactLinkSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ContactLinkDelete(DestroyAPIView):
    model = ContactLink
    queryset = ContactLink.objects.all()
    serializer_class = ContactLinkSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ContactModelList(ListAPIView):
    model = ContactModel
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer


class ContactModelCreate(CreateAPIView):
    model = ContactModel
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ContactModelDetail(RetrieveAPIView):
    model = ContactModel
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer


class ContactModelUpdate(UpdateAPIView):
    model = ContactModel
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ContactModelDelete(DestroyAPIView):
    model = ContactModel
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SocialList(ListAPIView):
    model = Social
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class SocialCreate(CreateAPIView):
    model = Social
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SocialDetail(RetrieveAPIView):
    model = Social
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class SocialUpdate(UpdateAPIView):
    model = Social
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SocialDelete(DestroyAPIView):
    model = Social
    queryset = Social.objects.all()
    serializer_class = SocialSerializer
    # permission_classes = [permissions.IsAuthenticated]
