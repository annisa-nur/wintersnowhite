# Program ini membaca file daftar_nilai.txt yang berisi data nilai ujian
# dari 30 mahasiswa dan mencari nilai rata-rata, nilai tertinggi, dan nilai terenda
from statistics import mean

def main():
    
    # Buat variabel untuk menyimpan hasil perhitungan dan inisialisasi dengan 0.0 (float)
    baris = 0
    tot_jual = 0
    banyak_baris = 0
    nilai_tertinggi = 0.0
    nilai_terendah = 0.0
    
    # [1] Tuliskan statement untuk membuka file daftar_nilai.txt untuk dibaca 
    # dan simpan isinya ke sebuah list
    file_nilai = open('daftar_nilai.txt', 'r')
        
    nilai = file_nilai.readlines()
            
    file_nilai.close()
        
    # [2] Tuliskan struktur loop untuk menghapus karakter baris baru pada setiap elemen
    # dari list
    index = 0
    while index < len(nilai):
        nilai[index] = nilai[index].rstrip('\n')
        index += 1

    
    # [3] Cari nilai rata-rata, nilai tertinggi, dan terendah. Gunakan loop.
    nilai = list(map(float, nilai))    
    rata2 = mean(nilai)
    highest = max(nilai)
    lowest = min(nilai)
    
    # [4] Tampilkan rata-rata, nilai tertinggi, dan nilai terendah.
    print(f'Rata-rata nilai ujian: {rata2: .2f}')
    print(f'Nilai ujian tertinggi: {highest: .2f}')
    print(f'Nilai ujian terendah: {lowest: .2f}')
        
    
# Panggil fungsi main()
main()


## another example
# Program ini menuliskan sebuah list ke file list_angka.txt
def main():
    
    angka = [234, 694, 123, 789, 923, 674, 534]
    
    # [1] Tuliskan kode untuk menuliskan list yang direferensikan oleh variabel angka
    # ke file list_angka.txt
    with open('list_angka.txt', 'w') as output_file:
        for elm in angka:
            output_file.write(str(elm) + '\n')
    
    
# Panggil fungsi main
main()