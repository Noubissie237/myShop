from django.shortcuts import render

# Create your views here.
def shop(request, *args, **kwargs):
    """Vue des produits"""
    context = {}
    return render(request, 'shop/index.html', context)


def panier(request, *args, **kwargs):

    context = {}

    return render(request, 'shop/panier.html', context)


def commande(request, *args, **kwargs):

    context = {}

    return render(request, 'shop/commande.html', context)