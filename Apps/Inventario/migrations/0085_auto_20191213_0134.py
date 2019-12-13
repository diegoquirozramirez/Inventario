# Generated by Django 2.0 on 2019-12-13 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0084_auto_20191213_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='ambiente',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='dependencia',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='sede',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
    ]
