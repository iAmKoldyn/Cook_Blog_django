from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import *
from rest_framework import generics, permissions
from .serializers import *


class GalleryList(ListAPIView):
    model = Gallery
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class GalleryCreate(CreateAPIView):
    model = Gallery
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    # permission_classes = [permissions.IsAuthenticated]


class GalleryDetail(RetrieveAPIView):
    model = Gallery
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer



class GalleryUpdate(UpdateAPIView):
    model = Gallery
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    # permission_classes = [permissions.IsAuthenticated]


class GalleryDelete(DestroyAPIView):
    model = Gallery
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    # permission_classes = [permissions.IsAuthenticated]


class PhotoList(ListAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoCreate(CreateAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PhotoDetail(RetrieveAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer


class PhotoUpdate(UpdateAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = [permissions.IsAuthenticated]


class PhotoDelete(DestroyAPIView):
    model = Photo
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = [permissions.IsAuthenticated]
