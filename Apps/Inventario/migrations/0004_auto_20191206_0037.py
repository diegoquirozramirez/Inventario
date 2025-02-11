# Generated by Django 2.0 on 2019-12-06 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0003_auto_20191206_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cabecera',
            name='ambi',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='depa',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='dire_gere',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='distri',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='moda',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='ofi',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='pis',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='provi',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='sed',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='subofi',
        ),
        migrations.RemoveField(
            model_name='cabecera',
            name='usu',
        ),
        migrations.AddField(
            model_name='usuario',
            name='ambi',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.ambiente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='depa',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='dire_gere',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.direccionGerencia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='distri',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.distrito'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='ofi',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.oficina'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='pis',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.piso'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='provi',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.provincia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='sed',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.sede'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='subofi',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Inventario.suboficina'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='cabecera',
        ),
    ]
