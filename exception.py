# Program ini meminta pengguna memasukkan dua angka untuk operasi pembagian
# Program menampilkan pesan jika terjadi eksepsi
def main():
    # [1] Tuliskan statement try/except
    # Pada body klausa try:
    #     - Minta dua angka ke pengguna
    #     - Lakukan pembagian
    # Pada body klausa except untuk ValueError
    #     - Tampilkan pesan: "Nilai yang diinput salah."
    # Pada body klausa except untuk ZeroDivisionError
    #     - Tampilkan pesan: "Tidak dapat membagi dengan nol."
    try:
        Pembilang = int(input("Masukkan sebuah angka yang akan dibagi: "))
        Penyebut = int(input("Masukkan sebuah angka pembagi: "))
        pembagian = float(Pembilang / Penyebut)
        print(f'{str(Pembilang)} dibagi dengan {str(Penyebut)} sama dengan {str(pembagian)}')
    except ValueError:
        print('Nilai yang diinput salah.')
    except ZeroDivisionError:
        print('Tidak dapat membagi dengan nol.')

## ANOTHER EXAMPLE OF EXCEPTION HANDLING
from statistics import mean

def main():
    # List untuk menyimpan isi file
    list_angka = []
    
    # [1] Tuliskan statement yang meminta pengguna memasukkan nama file dengan prompt: Masukkan nama file: "
    nama_file = input('Masukkan nama file: ')
    
    # [2] Tuliskan exception handler dengan statement try/except
    
    # Pada body klausa try: buka file, baca isinya, dan simpan isinya ke list_angka
    try:
        infile = open(nama_file, 'r')

        list_angka = infile.readlines()
        
        infile.close()
            
        index = 0
        while index < len(list_angka):
            list_angka[index] = list_angka[index].rstrip('\n')
            index += 1
        
        list_angka = list(map(float, list_angka ))    
        rata2 = mean(list_angka )
        highest = max(list_angka )
        lowest = min(list_angka )
            
    # Pada body klausa except untuk FileNoFoundError tampilkan pesan "File tidak ditemukan."
    except FileNotFoundError:
        print('File tidak ditemukan.')
    # Pada body klausa except untuk ValueError tampilkan pesan "Terdapat data non numerik dalam file."
    except ValueError:
        print('Terdapat data non numerik dalam file.')
    # Pada body klausa else: Cari rata-rata, nilai tertinggi, nilai terenda dan tampilkan hasilnya
    else:
        print(f'Rata-rata nilai:{rata2: .2f}')
        print(f'Nilai tertinggi:{highest: .2f}')
        print(f'Nilai terendah:{lowest: .2f}')
    
    
    
# Panggil fungsi main
main()