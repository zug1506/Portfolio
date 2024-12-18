from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render, redirect
from .models import Client,Produit
from .forms import ClientForm, ProduitForm
from django.db import IntegrityError




def index(request):
    return render(request, 'clients/index.html')





def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/liste_clients.html', {'clients': clients})

def creer_client(request):
    error_message = None
    if request.method == "POST":
        try:
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            adresse = request.POST['adresse']
            code_postal = request.POST['code_postal']
            ville = request.POST['ville']
            email = request.POST['email']
            telephone = request.POST['telephone']
            telephone2 = request.POST.get('telephone2', '')


            client = Client(nom=nom, prenom=prenom, adresse=adresse, code_postal=code_postal,
                            ville=ville, email=email, telephone=telephone, telephone2=telephone2)
            client.save()
            return redirect('liste_clients')

        except IntegrityError:
            error_message = "Cet email est déjà utilisé. Veuillez en utiliser un autre."

    return render(request, 'clients/creer_client.html', {'error_message': error_message})


def modifier_client(request, client_id):

    client = get_object_or_404(Client, id=client_id)

    if request.method == "POST":

        client.civilite = request.POST.get('civilite', '')
        client.nom = request.POST['nom']
        client.prenom = request.POST['prenom']
        client.adresse = request.POST['adresse']
        client.code_postal = request.POST['code_postal']
        client.ville = request.POST['ville']
        client.email = request.POST['email']
        client.telephone = request.POST['telephone']
        client.telephone2 = request.POST.get('telephone2', '')



        client.save()

        return redirect('liste_clients')


    return render(request, 'clients/modifier_client.html', {'client': client})


def supprimer_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('liste_clients')





def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'clients/liste_produits.html', {'produits': produits})

def creer_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'clients/creer_produit.html', {'form': form})



# Create your views here.

def generer_facture(request):

    return render(request, 'clients/generer_facture.html')
