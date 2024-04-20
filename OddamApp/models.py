from django.db import models
from django.conf import settings


class Category(models.Model):
    """
    Model kategorii, który przechowuje różne kategorie darów, które mogą być przekazywane.
    """
    name = models.CharField(max_length=255)  # Nazwa kategorii darów

    def __str__(self):
        return self.name


class Institution(models.Model):
    """
    Model instytucji, który przechowuje informacje o różnych typach instytucji, które mogą otrzymywać dary.
    """
    FUNDACJA = 'fundacja'
    ORGANIZACJA_POZARZADOWA = 'organizacja_pozarzadowa'
    ZBIORKA_LOKALNA = 'zbiorka_lokalna'

    INSTITUTION_TYPE_CHOICES = [
        (FUNDACJA, 'Fundacja'),
        (ORGANIZACJA_POZARZADOWA, 'Organizacja pozarządowa'),
        (ZBIORKA_LOKALNA, 'Zbiórka lokalna'),
    ]

    name = models.CharField(max_length=255)  # Nazwa instytucji
    description = models.TextField()  # Opis instytucji
    type = models.CharField(
        max_length=50,
        choices=INSTITUTION_TYPE_CHOICES,
        default=FUNDACJA
    )  # Typ instytucji, z wartością domyślną jako 'fundacja'
    categories = models.ManyToManyField(Category)  # Kat    egorie darów, które instytucja może przyjmować

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    class Meta:
        verbose_name = "instytucja"
        verbose_name_plural = "instytucje"


class Donation(models.Model):
    """
    Model daru, reprezentujący szczegóły dotyczące darów przekazywanych przez użytkowników.
    """
    quantity = models.IntegerField()  # Ilość worków z darowiznami
    categories = models.ManyToManyField(Category)  # Kategorie darowanych przedmiotów
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)  # Instytucja, która otrzyma dar
    address = models.CharField(max_length=255)  # Adres odbioru daru
    phone_number = models.CharField(max_length=15)  # Numer telefonu dla kontaktu przy odbiorze
    city = models.CharField(max_length=150)  # Miasto, w którym odbędzie się odbiór
    zip_code = models.CharField(max_length=10)  # Kod pocztowy miejsca odbioru
    pick_up_date = models.DateField()  # Data odbioru daru
    pick_up_time = models.TimeField()  # Godzina odbioru daru
    pick_up_comment = models.TextField(blank=True)  # Dodatkowe uwagi dla kuriera
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )  # Użytkownik przekazujący dar; może być anonimowy

    def __str__(self):
        return f"Donation by {self.user} to {self.institution}"
