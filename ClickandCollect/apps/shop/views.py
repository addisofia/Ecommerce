from django.shortcuts import render, redirect

# Create your views here.
#def index(request):
#    message = "Hello Django"
#    return render(request, "shop/index.html", {"message": message})

def home(request):
    return render(request, "shop/home.html")

def menu(request):
    return render(request, "shop/menu.html")


def redirect_buttons(request):
    if request.method == "POST":
        action = request.POST.get("action")

        if action == "panier":
            return redirect("shop:menu")
        elif action == "compte":
            return redirect("users:login")
        
    return redirect("shop:home")    