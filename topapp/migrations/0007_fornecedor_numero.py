# Generated by Django 5.0.1 on 2024-11-07 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topapp', '0006_rename_quantidade_reservada_estoque_tipomovimentacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedor',
            name='numero',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
