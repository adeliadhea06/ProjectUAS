from view import view_nilai
from tabulate import tabulate

dataMahasiswa = {
    'No': [],
    'NIM': [],
    'Nama': [],
    'Tugas': [],
    'UTS': [],
    'UAS':[],
    'Nilai Akhir':[]
}

# fungsi mengembalikan dataMahasiswa

def index():
    return dataMahasiswa

# fungsi tambah data

def tambah_data(no, nim, nama, tugas, uts, uas):
    nilai_akhir = tugas*30/100 + uts*35/100 + uas*35/100
    # menambahkan data
    dataMahasiswa['No'].append(no)
    dataMahasiswa['NIM'].append(nim)
    dataMahasiswa['Nama'].append(nama)
    dataMahasiswa['Tugas'].append(tugas)
    dataMahasiswa['UTS'].append(uts)
    dataMahasiswa['UAS'].append(uas)
    dataMahasiswa['Nilai Akhir'].append(nilai_akhir)
    print('Data berhasil ditambahkan')

# fungsi untuk mengedit data

def ubah_data():
    #print data untuk referensi nim data data yang mau dihapus
    print(tabulate(dataMahasiswa, headers=[
        'No', 'NIM','Nama', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))

    # cek jika ada nama tersebut di dataMahasiswa
    nim = int(input('Masukkan NIM yang mau diedit : '))

    if nim in dataMahasiswa['NIM']:
        # cari posisi indexnya lalu disimpan di nimIndex
        nimIndex = dataMahasiswa['NIM'].index(nim)
        print("Pilih data yang akan diedit")
        # perulangan mengedit data dalam bentuk pilihan
        while True:
            editApa = int(input(
                "(1) NIM, | (2) Nama, | (3) Nilai Tugas, | (4) Nilai UTS, | (5) Nilai UAS, | (0) Save Perubahan & Exit : \n"))
            print("")

            if editApa == 1:
                # jika memilih opsi 1 merubah nim
                newNim = int(input("Masukkan NIM : "))
                dataMahasiswa['NIM'][nimIndex] = newNim
            elif editApa == 2:
                # jika memilih opsi 2 merubah nama
                newNama = input("Masukkan Nama : ")
                dataMahasiswa['Nama'][nimIndex] = newNama
            elif editApa == 3:
                # jika memilih opsi 3 merubah nilai tugas & nilai akhir
                newTugas = int(input("Masukkan Nilai Tugas : "))
                #memperbarui nilai akhir
                nilai_akhir = (newTugas*30/100)+(dataMahasiswa['UTS'][nimIndex]*35/100)+(dataMahasiswa['UAS'][nimIndex]*35/100)
                dataMahasiswa['Tugas'][nimIndex] = newTugas
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 4:
                # jika memilih opsi 4 merubah nilai uts & nilai akhir
                newUts = int(input("Masukkan Nilai UTS : "))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex]*30/100)+(newUts*35/100)+(dataMahasiswa['UAS'][nimIndex] * 35 / 100)
                dataMahasiswa['UTS'][nimIndex] = newUts
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 5:
                # jika memilih opsi 5 merubah nilai uas & nilai akhir
                newUAS = int(input("Masukkan Nilai UAS : "))
                # memperbarui nilai akhir
                nilai_akhir = (dataMahasiswa['Tugas'][nimIndex] * 30 / 100)+(dataMahasiswa['UTS'][nimIndex] * 35 / 100) + (newUAS * 35 / 100)
                dataMahasiswa['UTS'][nimIndex] = newUts
                dataMahasiswa['Nilai Akhir'][nimIndex] = nilai_akhir
            elif editApa == 0:
                # jika memilih opsi 0 menyimpan perubahan dan keluar dari edit data
                print('Perubahan data berhasil disimpan,')
                break
        else:
            print("Data tidak ditemukan")

def cari_data():

    nama = input('Masukkan nama yang mau dicari : ')
    # cek jika nama ada di dataMahasiswa cari lokasi indexnya
    if nama in dataMahasiswa['Nama']:
        namaIndex = dataMahasiswa['Nama'].index(nama)
        # simpan data di variable hasilPencarian pada position index yang telah ditemukan
        hasilPencarian = {
            'No': [dataMahasiswa['No'][namaIndex]],
            'NIM': [dataMahasiswa['NIM'][namaIndex]],
            'Nama': [dataMahasiswa['Nama'][namaIndex]],
            'Tugas': [dataMahasiswa['Tugas'][namaIndex]],
            'UTS': [dataMahasiswa['UTS'][namaIndex]],
            'UAS': [dataMahasiswa['UAS'][namaIndex]],
            'Nilai Akhir': [dataMahasiswa['Nilai Akhir'][namaIndex]],
        }
        # memparsing parameter hasil pencarian ke modul cetak hasil pencarian
        view_nilai.cetak_hasil_pencarian(hasilPencarian)
    else:
        print("Data tidak ditemukan")

#fungsi untuk menghapus data

def hapus_data():
    # print data untuk referensi nim pada data yang mau dihapus
    print(tabulate(dataMahasiswa, headers=[
        'No', 'NIM', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir'], tablefmt="fancy_grid"))
    nim = int(input('Masukkan NIM yang mau dihapus : '))
    # cek jika nim ada di dataMahasiswa cari lokasi indexnya
    if nim in dataMahasiswa['NIM']:
        nimIndex = dataMahasiswa['NIM'].index(nim)
        # menghapus data berdasarkan position index yang telah ditemukan
        del dataMahasiswa['No'][nimIndex]
        del dataMahasiswa['NIM'][nimIndex]
        del dataMahasiswa['Nama'][nimIndex]
        del dataMahasiswa['Tugas'][nimIndex]
        del dataMahasiswa['UTS'][nimIndex]
        del dataMahasiswa['UAS'][nimIndex]
        del dataMahasiswa['Nilai Akhir'][nimIndex]
        print("Data berhasil dihapus.")
    else:
        print("Data tidak ditemukan")
