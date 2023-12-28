from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def shop(request, *args, **kwargs):
    """Vue des produits"""

    produit = Produit.objects.all()

    if request.user.is_authenticated:

        client = request.user.client

        commande, created = Commande.objects.get_or_create(client=client, complete=False)

        nombre_article = commande.get_panier_article

    else:

        articles = []

        commande = {
            'get_panier_total':0,
            'get_panier_article':0
        }

        nombre_article = commande('get_panier_article')

    context = {
        'produits' : produit,
        'nombre_article': nombre_article
    }

    return render(request, 'shop/index.html', context)


def panier(request, *args, **kwargs):

    if request.user.is_authenticated:

        client = request.user.client

        commande, created = Commande.objects.get_or_create(client=client, complete=False)

        articles = commande.commandearticle_set.all()

        nombre_article = commande.get_panier_article

    else:

        articles = []

        commande = {
            'get_panier_total':0,
            'get_panier_article':0
        }

        nombre_article = commande('get_panier_article')

    context = {
        'articles' : articles, 
        'commande': commande,
        'nombre_article': nombre_article
    }

    return render(request, 'shop/panier.html', context)


def commande(request, *args, **kwargs):

    if request.user.is_authenticated:

        client = request.user.client

        commande, created = Commande.objects.get_or_create(client=client, complete=False)

        articles = commande.commandearticle_set.all()

        nombre_article = commande.get_panier_article

    else:

        articles = []

        commande = {
            'get_panier_total':0,
            'get_panier_article':0
        }

        nombre_article = commande('get_panier_article')

    context = {
        'articles' : articles, 
        'commande': commande,
        'nombre_article': nombre_article
    }

    return render(request, 'shop/commande.html', context)

@login_required()
def update_article(request, *args, **kwargs):

    data = json.loads(request.body)
    produit_id = data['produit_id']
    action = data['action']
    
    produit = Produit.objects.get(id=produit_id)

    client = request.user.client

    commande, created = Commande.objects.get_or_create(client=client, complete=False)

    commande_article, created = CommandeArticle.objects.get_or_create(commande=commande, produit=produit)

    if action == "add":
        commande_article.quantite += 1
    
    if action == "remove":
        commande_article.quantite -=1

    commande_article.save()

    if commande_article.quantite <= 0:
        commande_article.delete()
    
    return JsonResponse("panier modifié", safe=False)