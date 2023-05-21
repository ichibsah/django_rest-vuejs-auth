from django.shortcuts import render

# Create your views here.

# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic 
#from django.views.generic import TemplateView


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("accounts:login")
    #password_reset_done = reverse_lazy("accounts:password_reset_done")
    template_name = "registration/signup.html"
    
class PasswordResetDoneView():
    success_url = reverse_lazy("password_reset_done")
    template_name = "registration/password_reset_done.html"