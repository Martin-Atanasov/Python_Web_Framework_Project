# from django.contrib.auth.views import LoginView
from django.urls import path
from accounts.views import CreateAccount, sign_out, LoginView, user_and_profile_update

urlpatterns = [
    path('accounts/create_acount/', CreateAccount.as_view(), name='create account'),
    # path('accounts/login/', LoginView.as_view(template_name='sign_in.html'), name='sign in'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/profile/<int:pk>/', user_and_profile_update, name='my_profile'),
    path('accounts/signout/', sign_out, name='sign out'),
]