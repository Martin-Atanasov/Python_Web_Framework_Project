from django.contrib.auth import logout, REDIRECT_FIELD_NAME
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from accounts.forms import CreateAccountForm, LoginForm


class CreateAccount(CreateView):
    form_class = CreateAccountForm
    success_url = reverse_lazy('home')
    template_name = 'create_account.html'


class LoginView1(LoginView):
    success_url = reverse_lazy('home')
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'sign_in.html'


def sign_out(request):
    logout(request)
    return redirect('home')
