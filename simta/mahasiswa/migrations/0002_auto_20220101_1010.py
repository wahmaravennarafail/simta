# Generated by Django 3.2.8 on 2022-01-01 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tendik', '0002_auto_20220101_1010'),
        ('mahasiswa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pembimbing',
            name='id_pemb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Dosen', to='tendik.dosen'),
        ),
        migrations.AlterField(
            model_name='pembimbing',
            name='pembimbing_1',
            field=models.TextField(default='', max_length=180),
        ),
        migrations.AlterField(
            model_name='pembimbing',
            name='pembimbing_2',
            field=models.TextField(default='', max_length=180),
        ),
    ]