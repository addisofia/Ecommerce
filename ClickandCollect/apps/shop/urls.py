from django.urls import path
from .views import home, menu,redirect_buttons
app_name = "shop"
urlpatterns = [
    path('redirect_buttons/',redirect_buttons, name='redirect_buttons'),
    path("",home, name="home"),
    path("menu/",menu,name="menu"),
]