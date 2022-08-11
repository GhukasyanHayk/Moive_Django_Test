from django.contrib import admin, messages
from django.contrib.auth.models import User
from .models import *
from django.db.models import QuerySet

admin.site.register(Director)
admin.site.register(Actor)
# admin.site.register(DressingRoom)


@admin.register(DressingRoom)
class DressingRoom(admin.ModelAdmin):
    list_display = ['floor', 'number', 'actor']


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79', 'Высокий'),
            ('>=80', 'Топ'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '40':
            return queryset.filter(rating__ls=40)
        return queryset


@admin.register(Moive)
class MoiveAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'director', 'year', 'budget', 'rating_status']
    list_editable = ['rating', 'director', 'year', 'budget']
    ordering = ['-rating']
    actions = ['set_dollars']
    search_fields = ['name__startswith', 'rating']
    list_filter = ['name', 'currency', RatingFilter]
    filter_horizontal = ['actors']

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, mov: Moive):
        if mov.rating < 50:
            return 'Зачем это смотреть'
        if mov.rating < 50:
            return 'Разочек можно это посмотреть'
        if mov.rating <= 85:
            return 'Зачет'
        return 'Топчик'

    @admin.action(description='Устонавить валюту доллар')
    def set_dollars(self, request, qs: QuerySet):
        qs.update(currency=Moive.USD)
