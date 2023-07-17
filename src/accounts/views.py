from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from accounts.forms import UserRegistrationForm
from accounts.models import CustomUser


class accountsHome(ListView):
    model = CustomUser
    context_object_name = "accounts"

def signup(request):

     if request.method == "POST":
         form = UserRegistrationForm(request.POST)
         if form.is_valid():
             form.save()
             return redirect("home")
     else:
         form = UserRegistrationForm()
     return render(request, "accounts/signup.html", context={"form": form})

     #   email = request.POST.get("email")
      #  password1 = request.POST.get("password1")
       # password2 = request.POST.get("password2")
       # if password1 !=password2:
       #     return render(request, "accounts/signup.html", {"error": "Les mots de pass  ne correspondent pas "})
       # CustomUser.objects.create_user(email=email, password=password1)
        #return HttpResponse(f"Bienvenue {email} !")
    #form = UserCreationForm()
    #return render(request, "accounts/signup.html", context={"form": form})

def profile(request):
    return HttpResponse(f"Bienvenue {request.user.email}")