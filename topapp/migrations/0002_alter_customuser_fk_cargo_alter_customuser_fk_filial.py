# Generated by Django 5.0.1 on 2024-10-05 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('topapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='fk_cargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='fk_filial',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='topapp.filial'),
        ),
    ]