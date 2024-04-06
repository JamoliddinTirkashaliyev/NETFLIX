# Generated by Django 5.0.4 on 2024-04-06 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aktyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=100)),
                ('t_sana', models.DateField(blank=True, null=True)),
                ('davlat', models.CharField(max_length=50)),
                ('jins', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('janr', models.CharField(max_length=50)),
                ('yil', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('davomiylik', models.CharField(max_length=20)),
                ('narx', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='KinoAktior',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aktior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmApp.aktyor')),
                ('kino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filmApp.kino')),
            ],
        ),
    ]
