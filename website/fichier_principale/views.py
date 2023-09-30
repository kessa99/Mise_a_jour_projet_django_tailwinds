from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import  User, auth

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
    if request.method =='POST':
        email = request.POST['username']
        password = request.POST['pawd']
        user = auth.authenticate(username=username, password=pwd)

        if user is not None:
            auth.login(request.user)
            return render('dossier_principale/home.html')
        else:
            return render(request, "dossier_connexion/login.html", {})

def signup1(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        pwd = request.POST['password1']
        pwd2 = request.POST['password2']

        # Vérifiez si un utilisateur avec le même nom d'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            # Gérez le cas où le nom d'utilisateur est déjà pris
            return render(request, 'dossier_principale/home.html')
        # Vérifiez si les mots de passe correspondent
        if pwd == pwd2:
            # Créez un nouvel utilisateur avec l'adresse e-mail comme nom d'utilisateur
            user = User.objects.create_user(username=username, email=email, password=pwd)
            # Mettez à jour le nom d'utilisateur avec la valeur capturée dans le formulaire
            user.username = username
            user.save()

            # Redirigez l'utilisateur vers une page de confirmation ou toute autre page souhaitée
            return render(request, 'dossier_principale/home.html')
        else:
            # Gérez le cas où les mots de passe ne correspondent pas
            return render(request, 'dossier_connexion/signup1.html')
    else:
        # Gérez le cas où la méthode de la requête n'est pas POST
        return render(request, 'dossier_connexion/signup1.html')



# def home(request):
#     return render(request, "dossier_principale/home.html", {})

# def home(request):
#     return render(request, "dossier_principale/home.html", {})