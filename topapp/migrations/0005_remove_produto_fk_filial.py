# Generated by Django 5.0.1 on 2024-11-06 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topapp', '0004_cliente_remove_customuser_fk_cargo_produto_medida_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='fk_filial',
        ),
    ]
