# from django.contrib.auth.views import LoginView
from django.urls import path
from accounts.views import CreateAccount, sign_out, LoginView, user_and_profile_update

urlpatterns = [
    path('create_acount/', CreateAccount.as_view(), name='create account'),
    # path('accounts/login/', LoginView.as_view(template_name='sign_in.html'), name='sign in'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/<int:pk>/', user_and_profile_update, name='my_profile'),
    path('signout/', sign_out, name='sign out'),
]