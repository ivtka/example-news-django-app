from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from users.forms import SignUpForm

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')