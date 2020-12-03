from django.contrib.auth import logout, REDIRECT_FIELD_NAME, authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from accounts.forms import CreateAccountForm, LoginForm
from accounts.models import UserProfile


class CreateAccount(CreateView):
    template_name = 'create_account.html'
    form_class = CreateAccountForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save(commit=False)
        profile = UserProfile(
            user=user,
        )
        user.save()
        profile.save()

        valid = super(CreateAccount, self).form_valid(form)

        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        if new_user.is_authenticated:
            print('yes')
        login(self.request, new_user)
        return valid


class LoginView(LoginView):
    success_url = reverse_lazy('home')
    form_class = LoginForm
    redirect_field_name = REDIRECT_FIELD_NAME
    template_name = 'sign_in.html'


def sign_out(request):
    logout(request)
    return redirect('home')
