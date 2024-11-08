# Generated by Django 5.1 on 2024-09-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loft', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='flat',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Квартира №: '),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Дом №:'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Улица'),
        ),
    ]
