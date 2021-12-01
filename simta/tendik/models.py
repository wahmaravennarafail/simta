from django.db import models
from django.db.models.base import Model
from django.db.models.fields import IntegerField


class MahasiswaModel(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.IntegerField()
    prodi = models.CharField(max_length=20)
    fakultas = models.CharField(max_length=20)
    kelas = models.CharField(max_length=3)
    semester = IntegerField()
    tahun_masuk = models.IntegerField(null=True)
    

