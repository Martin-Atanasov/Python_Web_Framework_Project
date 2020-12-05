from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic.base import View

from accounts.models import UserProfile


class HomeView(View):
    def get(self, request):
        context = {}
        if not request.user.is_anonymous:
            current_user = User.objects.get(id=request.user.id)
            current_profile = UserProfile.objects.get(user=request.user.id)
            context = {
                   'user': current_user,
                   'profile': current_profile,
            }
        return render(request, 'home.html', context)
