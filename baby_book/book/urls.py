from django.urls import path

from book.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
