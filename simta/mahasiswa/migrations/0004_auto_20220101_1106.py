# Generated by Django 3.2.8 on 2022-01-01 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tendik', '0003_rename_dosen_dosenpemb'),
        ('mahasiswa', '0003_auto_20220101_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='judul',
            name='id_mhs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tendik.mahasiswa'),
        ),
        migrations.AlterField(
            model_name='judul',
            name='id_pembimbing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mahasiswa.pembimbing'),
        ),
    ]