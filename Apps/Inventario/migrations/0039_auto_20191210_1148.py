# Generated by Django 2.0 on 2019-12-10 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0038_auto_20191210_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
    ]
