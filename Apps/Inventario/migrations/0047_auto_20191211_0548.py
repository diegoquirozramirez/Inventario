# Generated by Django 2.0 on 2019-12-11 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0046_auto_20191211_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cod_usuario',
        ),
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
    ]
