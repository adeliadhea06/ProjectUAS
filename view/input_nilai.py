# import module daftar nilai dari modul
from model import daftar_nilai as daftar

def input_data(no):
    # input seluruh data
    while True:
        try:
            nim = int(input("Masukkan NIM : "))
            if nim == '':
                print('Masukkan NIM, Tidak boleh kosong !')
        except ValueError:
            print('Masukkan NIM dengan angka !')
        else:
            break

    while True:
            nama = input("Masukkan Nama : ")
            if nama == '':
                print("Nama tidak boleh kosong !")
            else:
                break

    while True:
            try:
                tugas = int(input("Masukkan Nilai Tugas : "))
                if tugas == '':
                    print('Nilai tugas tidak boleh kosong !')
            except ValueError:
                print('Nilai tugas harus angka !')
            else:
                break

    while True:
        try:
            uts = int(input("Masukkan Nilai UTS : "))
            if uts == '':
                print('Nilai UTS tidak boleh kosong !')
        except ValueError:
            print('Nilai UTS harus angka !')
        else:
            break

    while True:
        try:
            uas = int(input("Masukkan Nilai UAS : "))
            if uas == '':
                print('Nilai UAS tidak boleh kosong !')
        except ValueError:
            print('Nilai UAS harus angka !')
        else:
            break

    daftar.tambah_data(no, nim, nama, tugas, uts, uas)
