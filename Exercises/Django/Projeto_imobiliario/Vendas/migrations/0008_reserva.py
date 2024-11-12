# Generated by Django 5.1.1 on 2024-10-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendas', '0007_delete_reserva'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_casa_a_ser_reservada', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField()),
                ('endereço', models.CharField(max_length=30)),
                ('disponibilidade', models.BooleanField()),
                ('data_da_reserva', models.DateField()),
                ('foto_da_casa', models.ImageField(blank=True, null=True, upload_to='Reserva')),
            ],
        ),
    ]
