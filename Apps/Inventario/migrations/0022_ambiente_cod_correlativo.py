# Generated by Django 2.0 on 2019-12-08 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0021_auto_20191208_1626'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambiente',
            name='cod_correlativo',
            field=models.CharField(default='', max_length=4),
        ),
    ]
