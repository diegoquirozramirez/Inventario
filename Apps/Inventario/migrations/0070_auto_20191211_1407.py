# Generated by Django 2.0 on 2019-12-11 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0069_auto_20191211_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base0',
            name='col',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventario.color'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
    ]
