# Generated by Django 3.2.10 on 2021-12-29 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0003_auto_20211229_1319'),
    ]

    operations = [
        migrations.CreateModel(
            name='bimbingan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField()),
                ('fakultas', models.CharField(max_length=30)),
                ('prodi', models.CharField(max_length=30)),
                ('pembimbing_1', models.CharField(max_length=20)),
                ('pembimbing_2', models.CharField(max_length=20)),
                ('judul', models.CharField(max_length=500)),
                ('abstrak', models.CharField(max_length=5000)),
            ],
        ),
    ]