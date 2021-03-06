# Generated by Django 3.2.8 on 2022-01-01 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mahasiswa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JadwalBimbingan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('waktu', models.TimeField()),
                ('lokasi', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PenyetujuanJudul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keterangan', models.TextField(max_length=500)),
                ('judul', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.judul')),
            ],
        ),
    ]
