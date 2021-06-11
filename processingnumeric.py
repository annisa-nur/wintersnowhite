# Program ini meminta pengguna memasukkan tiga buah angka float
# dan menuliskan keduanya, masing-masing dalam satu baris, 
# ke file angka.txt
def main():
    
    # [1] Minta pengguna memasukkan tiga buah angka desimal
    # Gunakan prompt "Masukkan sebuah angka desimal: " untuk angka pertama
    # dan prompt "Masukkan sebuah angka desimal lainnya: " untuk angka kedua dan ketiga 
    angka1 = input("Masukkan sebuah angka desimal: ")
    angka2 = input("Masukkan sebuah angka desimal lainnya: ")
    angka3 = input("Masukkan sebuah angka desimal lainnya: ")
    
    
    # [2] Buka file angka.txt untuk ditulis dan tuliskan angka-angka yang didapat
    # dari pengguna ke file tersebut masing-masing dalam baris baru.
    with open('angka.txt', 'w') as out_file:
        out_file.write(str(angka1) + '\n')
        out_file.write(str(angka2) + '\n')
        out_file.write(str(angka3) + '\n')        
    
    # [3] Tampilkan pesan "Data telah berhasil disimpan dalam file angka.txt."
    print('Data telah berhasil disimpan dalam file angka.txt.')

    
# Panggil fungsi main
main()

## another example
# Program ini membaca isi file angka_float.txt
# dan mengalikan angka yang terdapat dalam file tersebut
def main():
    
    # [1] Buka file dengan statement with atau 3 langkah menggunakan file: buka, proses, tutup.
    # Lalu ambil angka pertama pada baris pertama dan angka kedua pada baris kedua, simpan
    # angka pada setiap baris isi file masing-masing ke sebuah variabel 
    with open('angka_float.txt', 'r') as infile:
        angka1 = float(infile.readline())
        angka2 = float(infile.readline())

        
    # [2] Hitung hasi kali dan tampikan sesuai dengan ketentuan program yang diminta
    kali = round(angka1 * angka2, 2)
    print('Baris 1 file angka_float.txt berisi: ' + str(angka1))
    print('Baris 2 file angka_float.txt berisi: ' + str(angka2)) 
    print('Hasil kali baris 1 dan baris 2 = ' + str(kali))




# Panggil fungsi main
main()

