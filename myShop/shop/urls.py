from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="shop page"),
    path('panier/', views.panier, name="panier page"),
    path('commande/', views.commande, name="commande page"),
]
