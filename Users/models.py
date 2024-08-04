from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)



class Client(models.Model):
    """
    nom: modele de definition client 
    """
    TYPE_CLIENT_CHOICES = [
        ('R', 'Residentiel'), 
        ('C', 'Commercial'), 
        ('I', 'Industriel'), 
    ]
    
    # defiition du choix de sexe 

    TYPES_SEXE = (
        ('M', 'Masculin'), 
        ('F', 'Feminin'),
    )

    nom = models.CharField(max_length=255)
    post_nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    sexe = models.CharField(max_length=1, choices=TYPES_SEXE)
    adresse = models.TextField()
    type_client = models.CharField(max_length=20, choices=TYPE_CLIENT_CHOICES)
    
    def __str__(self) :
        return f"{self.nom}_{self.post_nom}_{self.prenom}"


class Consommation (models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    consommation_kwh = models.FloatField()

    def __str__(self) :
        return f"{self.client}_{self.date}"


class Facture(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_creation = models.DateField(default=timezone.now)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    est_paye = models.BooleanField(default=False)
    date_limite_paiement = models.DateField()

    def __str__(self) :
        return f" facture {self.id}_{self.client.nom}"

class Paiement(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    date_paiement = models.DateField(default=timezone.now)
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) :
        return f"paiement{self.id}_{self.facture.id}"


class Coupure(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_coupure = models.DateField()
    frais = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) :
        return f"Coupure{self.client.nom}_{self.date_coupure}"