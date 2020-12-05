from django.contrib.auth import logout, REDIRECT_FIELD_NAME, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView
import os

from accounts.forms import CreateAccountForm, LoginForm, ProfileForm, UserForm
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


@login_required
def user_and_profile_update(request, pk):
    profile = UserProfile.objects.get(pk=pk)
    current_user = User.objects.get(pk=profile.user_id)
    if request.method == 'GET':
        user_form = UserForm(instance=current_user)
        profile_form = ProfileForm(instance=profile)
        context = {
            'profile_form': profile_form,
            'user_form': user_form,
            'profile': profile,
        }
        return render(request, 'profile.html', context)

    default_pic = 'media/users/profile_pic_default.png'
    old_picture = 'media/'
    old_picture += str(profile.profile_picture)
    user_form = UserForm(request.POST, instance=current_user)
    profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

    if profile_form.is_valid() and user_form.is_valid():
        profile_form.save()
        user_form.save()
        if os.path.exists(old_picture) and old_picture != default_pic:
            os.remove(old_picture)
        return redirect('my_profile', profile.pk)

    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'profile': profile,
    }
    return render(request, 'profile.html', context)
