
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        valid = super(SignUpView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return valid
class CustomLoginView(LoginView):
    template_name = 'login.html'       
    def get_success_url(self):
        return reverse_lazy('homepage')

class MusicianCreateView(LoginRequiredMixin, CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('homepage')

class MusicianUpdateView(LoginRequiredMixin, UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'musician_form.html'
    success_url = reverse_lazy('homepage')

class MusicianDeleteView(LoginRequiredMixin, DeleteView):
    model = Musician
    template_name = 'musician_confirm_delete.html'
    success_url = reverse_lazy('homepage')

class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('homepage')

class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_form.html'
    success_url = reverse_lazy('homepage')

class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'album_confirm_delete.html'
    success_url = reverse_lazy('homepage')

