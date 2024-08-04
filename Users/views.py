from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
from .form import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Client, Facture, Paiement
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = UserCreationForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'connexion.html')

@login_required
def acceuil(request):
    return render(request, 'acceuil.html')

def deconnexion(request):
    logout(request)
    return redirect('connexion')



def facture_liste(request):
    factures = Facture.objects.all()
    return render(request, 'facture_liste.html', {'factures':factures})


def message(request):
    return render(request, 'message.html')


"""@login_required
def paiement_facture(request, facture_id):
    facture = get_object_or_404(Facture, id=facture.client_id)
    if request.method == 'POST':
        paiement = Paiement.objects.create(facture=facture, facture_paye=facture.montant)
        facture.est_paye = True
        facture.save()
        return redirect('thank_you')
    return render(request, 'paiement_facture.html', {'facture': facture})"""
