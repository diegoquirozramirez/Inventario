# Generated by Django 2.0 on 2019-12-10 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0035_auto_20191210_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
            preserve_default=False,
        ),
    ]
