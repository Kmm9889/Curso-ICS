# Generated by Django 5.1.1 on 2024-10-02 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alugueis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='foto_do_contrato',
            field=models.ImageField(blank=True, null=True, upload_to='Contrato'),
        ),
    ]