# Generated by Django 2.0 on 2019-12-16 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0094_auto_20191215_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='dni_ficha',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
    ]
