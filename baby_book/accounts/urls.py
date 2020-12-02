#from django.contrib.auth.views import LoginView
from django.urls import path
from accounts.views import CreateAccount, sign_out, LoginView1

urlpatterns = [
    path('create_acount/', CreateAccount.as_view(), name='create account'),
#    path('sign_in/', LoginView.as_view(template_name='sign_in.html'), name='sign in'),
    path('sign_in/', LoginView1.as_view(), name='sign in'),
    path('signout/', sign_out, name='sign out'),

]