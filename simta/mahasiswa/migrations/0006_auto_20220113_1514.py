# Generated by Django 3.2.8 on 2022-01-13 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0005_auto_20220101_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='judul',
            name='keterangan',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='judul',
            name='tolak',
            field=models.CharField(default='', max_length=6),
        ),
    ]