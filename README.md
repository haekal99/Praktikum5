# Praktikum5
Dictionary Input Nilai Mahasiswa

**Penjelasan Program**
1. Langkah pertama buat perintah untuk memasukan dictionary kosong, lalu masukan perintah "While true" agar program melakukan perulangan tanpa batas dan masukan perintah untuk menginput menu. Buat perintah "if" untuk membuat perulangan berhenti (break) ketika input dari menu yang di tampilkan adalah “K”.

2. Lalu buat perintah "elif" dan masukan perintah untuk menampilkan list ketika input menu adalah “l” dan buat perulangan "for" agar bisa menampilkan semua data yang sudah di input.
```python
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
        
 ```
 
 3. Buat perintah "elif" untuk membuat perintah tambah input data dari nilai mahasiswa ketika input menu adalah “T” dan buat perhitungan nilai dengan persentasi yang di inginkan untuk menampilkan nilai akhir
 ```python
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
```

4. Buat perintah "elif" untuk membuat perintah mengubah data yang sudah ada ketika input menu adalah “e” lalu buat buat perintah "if" agar kita bisa mencari nama yang ingin di ubah dan "else" jika data tersebut tidak ada.
```python
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
```

5. Buta perintah 'elif' untuk mencari salah satu data nilai
```python

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
  ```
            
6. Buat perintah "elif" untuk menghapus salah satu data nilai
```python
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
```

**FLOWCHART**

![FLOWCHART 5](https://user-images.githubusercontent.com/56957271/70290757-7e3f3580-180b-11ea-8c84-6a40d38c8963.JPG)


**Hasil dari input tersebut:**

![output 1](https://user-images.githubusercontent.com/56957271/70335387-ca28c380-1879-11ea-8b05-701a553e3106.JPG)

![output 2](https://user-images.githubusercontent.com/56957271/70335434-dc0a6680-1879-11ea-965b-bc023550061f.JPG)


**SELESAI**
