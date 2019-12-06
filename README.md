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

5. 
