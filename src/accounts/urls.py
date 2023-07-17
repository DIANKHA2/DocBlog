from django.urls import path, include
from accounts.views import accountsHome, signup, profile

app_name = "accounts"

urlpatterns =[
    #list
    path('', accountsHome.as_view(), name='home'),
    path('Compte/', include('django.contrib.auth.urls')),
    path('profile/', profile),
    path('Sinscrire/', signup, name='signup'),

]