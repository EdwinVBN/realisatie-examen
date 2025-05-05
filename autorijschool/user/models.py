from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class Gebruiker(AbstractUser):
    adres = models.CharField(max_length=255)
    woonplaats = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    huisnummer = models.PositiveIntegerField()
    ROLE_CHOICES = [
    ('eigenaar', 'Eigenaar'),
    ('instructeur', 'Instructeur'),
    ('klant', 'Klant'),
    ]
    rol = models.CharField(max_length=50, choices=ROLE_CHOICES, default='klant')

    tussenvoegsel = models.CharField(max_length=50, null=True, blank=True)
    exameninformatie = models.TextField(null=True, blank=True)
    geslaagd = models.BooleanField(default=False, null=True, blank=True)

    first_name = models.CharField("Voornaam", max_length=150)
    last_name = models.CharField("Achternaam", max_length=150)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'adres', 'woonplaats', 'postcode', 'huisnummer', 'rol']


class Ziekmelding(models.Model):
    toelichting = models.TextField(null=True, blank=True)
    van = models.DateTimeField(null=True, blank=True)
    tot = models.DateTimeField(null=True, blank=True)
    gebruiker = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ziekmeldingen'
        )

class Lespakket(models.Model):
    naam = models.CharField(max_length=255)
    omschrijving = models.TextField(null=True, blank=True)
    aantal = models.PositiveIntegerField()
    prijs = models.PositiveIntegerField()
    soortles = models.CharField(max_length=255)    


class Gebruiker_Lespakket(models.Model):
    gebruiker = models.ForeignKey(
            settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lespakketten'
        )
    lespakket = models.ForeignKey(Lespakket, on_delete=models.CASCADE, related_name='gebruiker_lespakketten')

class Soort(models.Model):
    type = models.CharField(max_length=255)
    instructeur = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='soort_instructeur',
        limit_choices_to={'rol': 'instructeur'}
    )

class Auto(models.Model):
    merk = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    kenteken = models.CharField(max_length=10)
    soort = models.ForeignKey(Soort, on_delete=models.CASCADE, related_name='soort_auto')

class OphaalLocatie(models.Model):
    adres = models.CharField(max_length=255)
    postcode = models.CharField(max_length=7)
    plaats = models.CharField(max_length=255)

class Les(models.Model):
    lestijd = models.DateTimeField(null=True, blank=True)
    doel = models.CharField(max_length=255)
    geannuleerd = models.BooleanField()
    reden_annuleren = models.TextField(null=True, blank=True)
    lespakket = models.ForeignKey(Lespakket, on_delete=models.CASCADE, related_name='lessen')
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='les_auto')
    ophaal_locatie = models.ForeignKey(OphaalLocatie, on_delete=models.CASCADE, related_name='ophaal_locatie_les')
    gebruiker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='gebruiker_lessen')

class Onderwerp(models.Model):
    onderwerp = models.CharField(max_length=255)
    omschrijving = models.TextField(null=True, blank=True)

class Les_Onderwerp(models.Model):
    les = models.ForeignKey(Les, on_delete=models.CASCADE, related_name='onderwerp')
    onderwerp = models.ForeignKey(Onderwerp, on_delete=models.CASCADE, related_name='les')