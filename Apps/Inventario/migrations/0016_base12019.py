# Generated by Django 2.0 on 2019-12-07 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0015_auto_20191206_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='base12019',
            fields=[
                ('id', models.AutoField(max_length=12, primary_key=True, serialize=False)),
                ('base0_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.base0')),
            ],
        ),
    ]
