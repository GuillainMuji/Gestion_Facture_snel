from django.contrib import admin
from .models import  Client, Consommation, Facture, Paiement, Coupure




class AdminClient(admin.ModelAdmin):
    list_display = ('nom', 'post_nom', 'prenom', 'sexe', 'adresse', 'type_client')

    

class AdminConsommation(admin.ModelAdmin):
    list_display = ('client', 'date', 'consommation_kwh')
    
class AdminFacture(admin.ModelAdmin):
    list_display = ('client', 'date_creation', 'montant', 'est_paye', 'date_limite_paiement')



class AdmiPaiement(admin.ModelAdmin):
    list_display = ('facture', 'date_paiement', 'montant')
 


class AdminCoupure(admin.ModelAdmin):
    list_display = ('client', 'date_coupure', 'frais')


admin.site.register(Client, AdminClient)
admin.site.register(Consommation, AdminConsommation)
admin.site.register(Facture, AdminFacture)
admin.site.register(Paiement, AdmiPaiement)
admin.site.register(Coupure, AdminCoupure)
