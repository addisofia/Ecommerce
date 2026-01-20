from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages


def login(request):
    return render(request, "users/login.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # récupère le champ username
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Vérifier si l'utilisateur existe déjà
        if User.objects.filter(username=username).exists():
            messages.error(request, "Ce nom d'utilisateur est déjà pris.")
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return redirect('signup')

        # Créer l'utilisateur
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Compte créé avec succès ! Vous pouvez maintenant vous connecter.")
        return redirect('login')  # rediriger vers la page login

    return render(request, 'accounts/signup.html')  # ton template existant



