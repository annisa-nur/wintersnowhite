# Program ini menuliskan angka 1 s.d 100 
# ke file daftar_angka.txt

# [1] Import module random
import random

# Definisi fungsi main
def main():
    
    # [2] Tuliskan kode untuk membuka file daftar_angka.txt untuk ditulis
    # Generasi angka acak antara 1 s.d 100 sebanyak 100 angka dengan fungsi randint
    # dan tulis masing-masing angka ke masing-masing baris pada file daftar_angka.txt.
    with open('daftar_angka.txt', 'w') as out_file:
        bilangan = random.randint(1, 100)
        for i in range(1, 101):
            out_file.write(str(i) + '\n')





# [3] Panggil fungsi main            
main()

##another example
# Program ini menghitung rata-rata penjualan
# dengan data yang terdapat dalam file sales.txt
def main():
    
    # Ikuti petunjuk pada komentar di bawah.
    # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
    # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah
    
    
    # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
    # dan variabel akumulator untuk menghitung total penjualan
    baris = 0
    tot_jual = 0
    banyak_baris = 0
    
    
    # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
    file_sales = open('sales.txt', 'r')
    
    
    # [3] Baca baris pertama isi file dan simpan ke suatu variabel
    baris = file_sales.readline()
    
    # [4] Tuliskan loop while untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
    # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
    # - inkrementasi variabel penghitung baris
    while baris != '':
        isi_baris = float(baris)
        tot_jual = tot_jual + isi_baris
        banyak_baris = banyak_baris + 1

        tot_jual = float(tot_jual)

        baris = file_sales.readline()
    
    file_sales.close()
        
    
    # [5] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
    # dan tampilkan hasilnya.    
    rata2 = tot_jual / banyak_baris
    print('Rata-rata penjualan: {:,.2f}'.format(rata2))



# Panggil fungsi main
main()

## another example
# Program ini menghitung rata-rata penjualan
# dengan data yang terdapat dalam file sales.txt
def main():
    
    # Ikuti petunjuk pada komentar di bawah.
    # Petunjuk pada kerangka program ini menggunakan 3 langkah menggunakan file: buka, proses, tutup.
    # Anda diperbolehkan menggunakan statement with, namun kode Anda akan sedikit berbeda dengan petunjuk di bawah
    
    
    # [1] Buat dua buah variabel: variabel penghitung baris untuk menghitung banyak baris (untuk digunakan sebagai banyak penjualan)
    # dan variabel akumulator untuk menghitung total penjualan
    baris = 0
    banyak_baris = 0
    tot_jual = 0
    
    
    # [2] Buka file sales.txt untuk dibaca dan simpan object file ke suatu variabel
    file_sales = open('sales.txt', 'r')
    
    
    # [3] Tuliskan loop for untuk mengiterasi isi file setiap barisnya dan lakukan hal berikut pada setiap iterasi:
    # - akumulasikan isi_baris ke variabel akumulator (jangan lupa konversi ke tipe numerik)
    # - inkrementasi variabel penghitung baris
    for baris in file_sales:
        isi_file = float(baris)
        tot_jual = tot_jual + isi_file
        banyak_baris = banyak_baris + 1
        
    file_sales.close()
    
    
    # [4] Hitung rata-rata dengan membagi total penjualan dan banyak penjualan (variabel akumulator / variabel penghitung baris)
    # dan tampilkan hasilnya.        
    rata2 = tot_jual / banyak_baris
    print('Rata-rata penjualan: {:,.2f}'.format(rata2))



# Panggil fungsi main
main()