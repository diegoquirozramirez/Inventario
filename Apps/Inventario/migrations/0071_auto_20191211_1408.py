# Generated by Django 2.0 on 2019-12-11 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0070_auto_20191211_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base0',
            name='est',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventario.estado'),
        ),
        migrations.AlterField(
            model_name='base0',
            name='mar',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventario.marca'),
        ),
        migrations.AlterField(
            model_name='base0',
            name='op',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Inventario.operatividad'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='idusuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Usuario'),
        ),
    ]
