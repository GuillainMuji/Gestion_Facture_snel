from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Paiement, Facture



from django import forms
from django.contrib.auth.forms import UserCreationForm

class SingForm(UserCreationForm):
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("password1", "password2")

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = ['montant']


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['client', 'montant', 'est_paye', 'date_limite_paiement']
