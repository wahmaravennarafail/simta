# Generated by Django 3.2.8 on 2021-12-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tendik', '0003_remove_pembimbingmodel_id_pembimbing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pembimbingmodel',
            name='hp',
            field=models.IntegerField(),
        ),
    ]
