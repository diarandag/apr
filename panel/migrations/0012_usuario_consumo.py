# Generated by Django 4.2.6 on 2023-10-27 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_usuario_numero_medidor'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='consumo',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Consumo'),
        ),
    ]
