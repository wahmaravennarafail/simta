# Generated by Django 3.2.8 on 2022-01-01 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0002_auto_20220101_1010'),
        ('tendik', '0002_auto_20220101_1010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Dosen',
            new_name='DosenPemb',
        ),
    ]