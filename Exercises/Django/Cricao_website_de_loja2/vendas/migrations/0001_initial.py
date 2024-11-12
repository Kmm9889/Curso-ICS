# Generated by Django 5.1.1 on 2024-09-15 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cobranca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(max_length=10)),
                ('data_vencimento', models.DateField(max_length=10)),
                ('data_pagamento', models.DateField(max_length=10)),
                ('metodo', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco_entrega', models.CharField(max_length=50)),
                ('data_envio', models.DateField(max_length=10)),
                ('data_entrega', models.DateField(max_length=10)),
                ('status', models.CharField(max_length=20)),
                ('codigo_rastreamento', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(max_length=15)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('forma_pagamento', models.CharField(max_length=40)),
                ('observacao', models.TextField(max_length=500)),
            ],
        ),
    ]
