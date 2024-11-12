# Generated by Django 5.1.1 on 2024-10-02 18:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendas', '0002_alter_reserva_data_da_reserva'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='data_da_compra',
        ),
        migrations.AddField(
            model_name='venda',
            name='data_da_e_hora_da_compra',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
