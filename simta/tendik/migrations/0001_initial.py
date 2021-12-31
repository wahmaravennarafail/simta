# Generated by Django 3.2.8 on 2021-12-31 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MahasiswaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.IntegerField(unique=True)),
                ('nama', models.CharField(max_length=50)),
                ('prodi', models.CharField(max_length=20)),
                ('fakultas', models.CharField(max_length=20)),
                ('kelas', models.CharField(max_length=3)),
                ('semester', models.IntegerField()),
                ('tahun_masuk', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PembimbingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.IntegerField(unique=True)),
                ('nidn', models.IntegerField()),
                ('hp', models.BigIntegerField()),
                ('nama', models.CharField(max_length=50)),
                ('prodi', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
