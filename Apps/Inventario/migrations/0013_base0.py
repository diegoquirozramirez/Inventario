# Generated by Django 2.0 on 2019-12-06 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0012_ambiente_usuario_ambiente'),
    ]

    operations = [
        migrations.CreateModel(
            name='base0',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_sbn', models.CharField(max_length=12)),
                ('codigo_interno', models.CharField(max_length=5)),
                ('piso_base0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.piso')),
                ('sede_base0', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.sede')),
            ],
        ),
    ]
