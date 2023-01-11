from tabulate import tabulate
from model import daftar_nilai


def cetak_daftar_nilai():
    dataMahasiswa = daftar_nilai.index()
    print(tabulate(dataMahasiswa,headers=[
        'No', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))


def cetak_hasil_pencarian(hasilPencarian):
    print(tabulate(hasilPencarian, headers=[
        'No', 'NIM', 'Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))
    print("Data berhasil ditemukan")
