# Generated by Django 2.0 on 2019-12-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0008_auto_20191206_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sector',
            name='obs_sector',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
