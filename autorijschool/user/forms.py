from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
from .models import Gebruiker, Les, Gebruiker_Lespakket, Auto, Soort
from django.contrib.auth import authenticate


class UserRegister(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=150)
    last_name = forms.CharField(required=True, max_length=150)
    adres = forms.CharField(required=True, max_length=255)
    woonplaats = forms.CharField(required=True, max_length=100)
    postcode = forms.CharField(required=True, max_length=20)
    huisnummer = forms.IntegerField(required=True)


    class Meta:
        model = Gebruiker
        fields = ['username', 'first_name', 'last_name', 'tussenvoegsel', 'adres', 'woonplaats', 'postcode', 'huisnummer', 'email', 'password1', 'password2']

class EditUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=150)
    last_name = forms.CharField(required=True, max_length=150)
    adres = forms.CharField(required=True, max_length=255)
    woonplaats = forms.CharField(required=True, max_length=100)
    postcode = forms.CharField(required=True, max_length=20)
    huisnummer = forms.IntegerField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Gebruiker
        fields = ['first_name', 'last_name', 'tussenvoegsel', 'adres', 'woonplaats', 'postcode', 'huisnummer', 'email', 'password']

class LesEditForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        geannuleerd = cleaned_data.get('geannuleerd')
        lestijd = cleaned_data.get('lestijd')
        
        # Controleer of de lestijd niet in het verleden ligt
        if lestijd and lestijd < timezone.now():
            raise forms.ValidationError({
                'lestijd': "De lestijd mag niet in het verleden liggen."
            })
        
        if geannuleerd and not self.instance.geannuleerd:
            if self.instance.lestijd - timezone.now() < timedelta(hours=24):
                cleaned_data['geannuleerd'] = False
                cleaned_data['reden_annuleren'] = ''
                raise forms.ValidationError({
                    'geannuleerd': "Les kan niet worden geannuleerd binnen 24 uur voor aanvang."
                })
            
            if not cleaned_data.get('reden_annuleren'):
                raise forms.ValidationError({
                    'reden_annuleren': "Een reden voor annulering is verplicht."
                })
        
        return cleaned_data

    class Meta:
        model = Les
        fields = ['lestijd', 'geannuleerd', 'reden_annuleren']
        widgets = {
            'lestijd': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class EigenaarEditUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, max_length=150)
    last_name = forms.CharField(required=True, max_length=150)
    adres = forms.CharField(required=True, max_length=255)
    woonplaats = forms.CharField(required=True, max_length=100)
    postcode = forms.CharField(required=True, max_length=20)
    huisnummer = forms.IntegerField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=False)
    rol = forms.ChoiceField(choices=Gebruiker.ROLE_CHOICES, required=True)

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['password']:
            user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Gebruiker
        fields = ['first_name', 'last_name', 'tussenvoegsel', 'adres', 
                 'woonplaats', 'postcode', 'huisnummer', 'email', 
                 'password', 'rol']

class AutoCreateForm(forms.ModelForm):
    type = forms.CharField(max_length=255)

    def save(self, commit=True):
        auto = super().save(commit=False)
        type_value = self.cleaned_data.get('type')
        soort, created = Soort.objects.get_or_create(type=type_value)
        auto.soort = soort
        if commit:
            auto.save()
        return auto

    class Meta:
        model = Auto
        fields = ['merk', 'model', 'kenteken', 'type']

class AutoEditForm(forms.ModelForm):
    type = forms.CharField(max_length=255)

    def save(self, commit=True):
        auto = super().save(commit=False)
        type_value = self.cleaned_data.get('type')
        soort, created = Soort.objects.get_or_create(type=type_value)
        auto.soort = soort
        if commit:
            auto.save()
        return auto
    
    class Meta:
        model = Auto
        fields = ['merk', 'model', 'kenteken', 'type']

class CustomAuthenticationForm(AuthenticationForm):
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            try:
                user = Gebruiker.objects.get(username=username)
                if not user.is_active:
                    raise forms.ValidationError(
                        "Dit account is niet actief. Neem contact op met de beheerder."
                    )
            except Gebruiker.DoesNotExist:
                raise forms.ValidationError(
                    "Ongeldige gebruikersnaam of wachtwoord."
                )

        return super().clean()

