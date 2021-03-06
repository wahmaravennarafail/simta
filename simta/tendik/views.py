from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from .forms import MahasiswaForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
# from mahasiswa import models as models_mhs
# from mahasiswa.models import Judul, pembimbing

# @login_required(login_url=settings.LOGIN_URL)
def dashboardView(request):
    return render(request, 'tendik/index.html')

# ----------------------Untuk Halaman Pembimbing-------------------------------------------------

# Menampilkan data inputan

def pembimbingView(request):
    if request.POST:
        nama = request.POST['nama']
        nip = request.POST['nip']
        nidn = request.POST['nidn']
        hp = request.POST['hp']
        prodi = request.POST['prodi']
        models.DosenPemb.objects.create(nama=nama, nip=nip, nidn=nidn, hp=hp, prodi=prodi)
        messages.success(request, f'Data pembimbing berhasil ditambahkan')
    pembibmbing_table = models.DosenPemb.objects.all()
    return render(request, 'tendik/pembimbing.html', {
        'pemb_table': pembibmbing_table
    })

# Hapus

def pembimbingHapus(request, id):
    models.DosenPemb.objects.filter(pk =id).delete()
    return redirect('/tendik/pembimbing')

# ------------------------------------------------------------------------------

# ----------------------Untuk Halaman Mahasiswa---------------------------------

# Tampilkan Data
def mahasiswaView(request):
    if request.POST:
        nama = request.POST['nama']
        nim = request.POST['nim']
        prodi = request.POST['prodi']
        fakultas = request.POST['fakultas']
        semester = request.POST['semester']
        tahun_masuk = request.POST['tahun_masuk']
        models.Mahasiswa.objects.create(nama=nama, nim=nim, prodi=prodi, fakultas=fakultas, semester=semester, tahun_masuk=tahun_masuk)
        messages.success(request, f'Data Mahasiswa telah ditambahkan')
        print(nim)
        
    mhs_table = models.Mahasiswa.objects.all()
    return render(request, 'tendik/mahasiswa.html', {
        'tabel_mhs': mhs_table
    })

    # Hapus Data
def mahasiswaHapus(request, id):
    models.Mahasiswa.objects.filter(pk=id).delete()
    return redirect('/tendik/mahasiswa')

    # edit mahasiswa
def editmahasiswa(request, id):
    if request.POST:
        models.Mahasiswa.objects.filter(pk=id).update(
            nama = request.POST['nama'],
            nim = request.POST['nim'],
            prodi = request.POST['prodi'],
            fakultas = request.POST['fakultas'],
            # kelas = request.POST['kelas'],
            semester = request.POST['semester'],
            tahun_masuk = request.POST['tahun_masuk'],
        )
        return redirect ('/tendik/mahasiswa')
    mhs_update = models.Mahasiswa.objects.filter(pk=id).first()
    print(mhs_update)
    return render(request, 'tendik/editmahasiswa.html', {
        'tabel_mhs': mhs_update
    })


    # edit pembimbing
def editpembimbing(request, id):
    if request.POST:
        models.DosenPemb.objects.filter(pk=id).update(
            nama = request.POST['nama'],
            nip = request.POST['nip'],
            nidn = request.POST['nidn'],
            hp = request.POST['hp'],
            prodi = request.POST['prodi'],
        )
        return redirect ('/tendik/pembimbing')
    pembimbing_update = models.DosenPemb.objects.filter(pk=id).first()
    print(pembimbing_update)
    return render(request, 'tendik/editpembimbing.html', {
        'tabel_mhs': pembimbing_update
    })

    #  return render(request, 'tendik/editmahasiswa.html')

# ------------------------------------------------------------

def pengajuanJudulView(request):
    # data_judul = models.Judul.objects.all()
    # data_pem = models_mhs.pembimbing.objects.all()
    # print(data_pem)
    # konteks = {'data_judul' : data_judul}
    # konteks2 = {'datapem' : data_pem}
    return render(request, 'tendik/pengajuanjudul.html')

def proposalView(request):
    # data_pembimbing = models.pembimbing.objects.all()
    # konteks2 = {'data_pembimbing' : data_pembimbing}
    return render(request, 'tendik/proposal.html')

def tugasAkhirView(request):
    return render(request, 'tendik/tugas-akhir.html')

def jadwalBimbingan(request):
    return render(request, 'tendik/jadwal-bimbingan.html')

def jadwalSeminarProposal(request):
    return render(request, 'tendik/jadwal-sempro.html')

def jadwalSidang(request):
    return render(request, 'tendik/jadwal-sidang.html')