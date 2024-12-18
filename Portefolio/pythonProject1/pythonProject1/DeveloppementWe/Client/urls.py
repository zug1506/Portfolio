from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.liste_clients, name='liste_clients'),
    path('clients/creer/', views.creer_client, name='creer_client'),
    path('clients/modifier/<int:client_id>/', views.modifier_client, name='modifier_client'),
    path('clients/supprimer/<int:client_id>/', views.supprimer_client, name='supprimer_client'),
    path('produits/', views.liste_produits, name='liste_produits'),
    path('produits/creer/', views.creer_produit, name='creer_produit'),
    path('generer-facture/', views.generer_facture, name='generer_facture')
]
