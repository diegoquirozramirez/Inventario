# Generated by Django 2.0 on 2019-12-06 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0009_auto_20191206_0216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ambiente',
            old_name='mon_ambiente',
            new_name='nom_ambiente',
        ),
    ]
