# Generated by Django 2.0 on 2019-12-16 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0095_auto_20191216_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
    ]
