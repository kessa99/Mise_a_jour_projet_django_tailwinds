from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate

# definission des pages principale.

def home(request):
    return render(request, "dossier_principale/home.html", {})

def aide(request):
    return render(request, "dossier_principale/aide.html", {})

def dashboard(request):
    return render(request, "dossier_principale/dashboard.html", {})

def information(request):
    return render(request, "dossier_principale/informations.html", {})

def service(request):
    return render(request, "dossier_principale/services.html", {})


#definitions des pages pour le dashboard

def impot(request):
    return render(request, "dossier_dashbord/impot.html", {})

#definition pour les page de connexion

def login(request):
    return render(request, "dossier_connexion/login.html", {})

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm(request.POST)

    return render(request, "dossier_connexion/signup.html", {"form": form})



# def home(request):
#     return render(request, "dossier_principale/home.html", {})

# def home(request):
#     return render(request, "dossier_principale/home.html", {})