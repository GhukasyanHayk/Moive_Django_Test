from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=100, default='Квентин Тарантино')
    last_name = models.CharField(max_length=100, default='Квентин Тарантино')
    director_emanil = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class DressingRoom(models.Model):
    floor = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.floor} {self.number}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женшина'),
    ]

    first_name = models.CharField(max_length=100, default='Квентин Тарантино')
    last_name = models.CharField(max_length=100, default='Квентин Тарантино')
    dressing = models.OneToOneField(DressingRoom, on_delete=models.SET_NULL, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default=MALE)

    def __str__(self):
        if self.gender == self.MALE:
            return f'Актер {self.first_name} {self.last_name}'
        return f'Актриса {self.first_name} {self.last_name}'


class Moive(models.Model):
    EUR = 'EUR'
    USD = 'USD'
    RUB = 'RUB'

    CORRENCY_CHOICES = [

        (EUR, 'Euro'),
        (USD, 'Dollars'),
        (RUB, 'Rubles'),

    ]

    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=1000000, blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CORRENCY_CHOICES, default='R')
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actors = models.ManyToManyField(Actor)

    def get_url(self):
        return reverse('movie_detail', args=[self.id])

    def __str__(self):
        return f'{self.name} - {self.rating}%'
