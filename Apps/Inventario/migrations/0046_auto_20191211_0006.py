# Generated by Django 2.0 on 2019-12-11 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0045_auto_20191210_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='num_ficha',
            field=models.CharField(max_length=7),
        ),
    ]
