# Generated by Django 2.0 on 2019-12-11 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0060_auto_20191211_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etiquetado',
            name='cod_eti',
        ),
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
    ]
