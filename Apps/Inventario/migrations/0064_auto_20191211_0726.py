# Generated by Django 2.0 on 2019-12-11 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0063_auto_20191211_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base0',
            name='tipo',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
    ]
