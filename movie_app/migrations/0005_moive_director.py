# Generated by Django 4.0.6 on 2022-08-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0004_alter_moive_budget_alter_moive_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='moive',
            name='director',
            field=models.CharField(default='Квентин Тарантино', max_length=100),
        ),
    ]
