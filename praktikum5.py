print("Program Input Nilai")
print("=================")
print("= Data Nilai Mahasiswa =====")

daftar = {}

while True:
    perintah = input("(L) Lihat, (T) Tambah, (U) Ubah, \n"
                     "(H) Hapus, (C) Cari, (K) Keluar: ")


    # Keluar
    if perintah.lower() == 'k':
        break
    
    # Lihat
    elif perintah.lower() == 'l':
        print("Daftar Nilai:")
        print("===================================================================")
        print("| No |      Nama      |    NIM    | Tugas |  UTS  |  UAS  | Akhir |")
        print("===================================================================")
        no = 1
        for tabel in daftar.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                  (no, tabel[0],
                   tabel[1], tabel[2],
                   tabel[3], tabel[4], tabel[5]))
            no += 1
        print("===================================================================")

    # Tambah
    elif perintah.lower() == 't':
        print("Masukan data mahasiswa")
        print("...")
        nama = input("Masukan nama: ")
        nim = input("Masukan NIM: ")
        n_tugas = int(input("Masukan nilai tugas: "))
        n_UTS = int(input("Masukan nilai UTS: "))
        n_UAS = int(input("Masukan nilai UAS: "))
        akhir = (n_tugas * 30/100 + n_UTS * 35/100 + n_UAS * 35/100)
        daftar[nama] = [nama, nim, n_tugas, n_UTS, n_UAS, akhir]

    # Ubah
    elif perintah.lower() == 'u':
        print("Ubah Data")
        nama = input("Masukan nama: ")
        if nama in daftar.keys():
            nim = input("Masukan NIM: ")
            n_tugas = int(input("Masukan nilai tugas: "))
            n_UTS = int(input("Masukan nilai UTS: "))
            n_UAS = int(input("Masukan nilai UAS: "))
            akhir = (n_tugas * 30/100 + n_UTS * 35/100 + n_UAS * 35/100)
            daftar[nama] = [nama, nim, n_tugas, n_UTS, n_UAS, akhir]
        else:
            print("Data {0} tidak ada".format(nama))

    # Cari
    elif perintah.lower() == 'c':
        print("Mencari daftar nilai: ")
        print("=================================================")
        nama = input("Masukan nama untuk mencari daftar nilai : ")
        if nama in daftar.keys():
            print("Nama {0}, dengan NIM : {1}\n"
                  "Nilai Tugas: {2}, UTS: {3}, dan UAS: {4}\n"
                  "dan nilai akhir {5}".format(nama, daftar[nama][1],
                                               daftar[nama][2], daftar[nama][3],
                                               daftar[nama][4], daftar[nama][5]))
        else:
            print("'{}' tidak ditemukan.".format(nama))

    # Hapus
    elif perintah.lower() == 'h':
        nama = input("Masukan nama untuk menghapus data : ")
        if nama in daftar.keys():
            del daftar[nama]
            print("Data '{}' dihapus.".format(nama))
        else:
            print("'{}' tidak ditemukan.".format(nama))

    else:
        print("Silahkan masukan perintah terlebih dahulu.")
