from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
 
class Wilaya(models.TextChoices):
    ADRAR = "01", "Adrar"
    CHLEF = "02", "Chlef"
    LAGHOUAT = "03", "Laghouat"
    OUM_EL_BOUAGHI = "04", "Oum El Bouaghi"
    BATNA = "05", "Batna"
    BEJAIA = "06", "Bejaia"
    BISKRA = "07", "Biskra"
    BECHAR = "08", "Bechar"
    BLIDA = "09", "Blida"
    BOUIRA = "10", "Bouira"
    TAMANRASSET = "11", "Tamanrasset"
    TEBESSA = "12", "Tebessa"
    TLEMCEN = "13", "Tlemcen"
    TIARET = "14", "Tiaret"
    TIZI_OUZOU = "15", "Tizi Ouzou"
    ALGIERS = "16", "Algiers"
    DJELFA = "17", "Djelfa"
    JIJEL = "18", "Jijel"
    SETIF = "19", "Setif"
    SAIDA = "20", "Saida"
    SKIKDA = "21", "Skikda"
    SIDI_BEL_ABBES = "22", "Sidi Bel Abbes"
    ANNABA = "23", "Annaba"
    GUELMA = "24", "Guelma"
    CONSTANTINE = "25", "Constantine"
    MEDEA = "26", "Medea"
    MOSTAGANEM = "27", "Mostaganem"
    MSILA = "28", "Msila"
    MASCARA = "29", "Mascara"
    OUARGLA = "30", "Ouargla"
    ORAN = "31", "Oran"
    EL_BAYADH = "32", "El Bayadh"
    ILLIZI = "33", "Illizi"
    BORDJ_BOU_ARRERIDJ = "34", "Bordj Bou Arreridj"
    BOUMERDES = "35", "Boumerdes"
    EL_TARF = "36", "El Tarf"
    TINDOUF = "37", "Tindouf"
    TISSEMSILT = "38", "Tissemsilt"
    EL_OUED = "39", "El Oued"
    KHENCHELA = "40", "Khenchela"
    SOUK_AHRAS = "41", "Souk Ahras"
    TIPAZA = "42", "Tipaza"
    MILA = "43", "Mila"
    AIN_DEFLA = "44", "Ain Defla"
    NAAMA = "45", "Naama"
    AIN_TEMOUCHENT = "46", "Ain Temouchent"
    GHARDAIA = "47", "Ghardaia"
    RELIZANE = "48", "Relizane"

class Band(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=10, blank=False, null=False)
    wilaya = models.CharField(
        max_length=2,
        choices=Wilaya.choices,
        default=Wilaya.ALGIERS,
    )

    def __str__(self):
        return self.name

class MusicianManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)  # Use set_password to hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, first_name, last_name, password, **extra_fields)


class Musician(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=200, blank=False, null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    birth_date = models.DateField(blank=False, null=True)
    instrument = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=10, blank=False, null=False)
    band = models.ForeignKey(Band, on_delete=models.SET_DEFAULT, default=None, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = MusicianManager()  

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def full_name(self):
        return self.first_name + " " + self.last_name
