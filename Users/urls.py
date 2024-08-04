from django.urls import path
from .import views



   
urlpatterns = [
    path('connexion', views.connexion, name='connexion'),
    path('inscription/', views.inscription, name='inscription'),
    path('acceuil/', views.acceuil, name='acceuil'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('facture_liste', views.facture_liste, name='facture_liste'),
    path('message', views.message, name='message'), 
    #path('paiement_facture', views.paiement_facture, name='paiement_facture'), 

]
