# Generated by Django 3.2.10 on 2021-12-29 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mahasiswa', '0002_auto_20211229_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ta',
            name='pembimbing_1',
            field=models.TextField(max_length=180),
        ),
        migrations.AlterField(
            model_name='ta',
            name='pembimbing_2',
            field=models.TextField(max_length=180),
        ),
    ]