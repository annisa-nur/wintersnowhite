# Program ini menambahkan record nilai mahasiswa
# ke file nilai_mahasiswa.txt
def main():
    # [1] Minta pengguna berapa banyak record yang ingin dimasukkan
    jmlRec = int(input("Berapa banyak record nilai mahasiswa yang ingin Anda tambahkan? "))



    # [2] Buka file dengan statement with, minta input masing-masing record ke pengguna, dan tulis ke file
    # nilai_mahasiswa.txt
    with open('nilai_mahasiswa.txt', 'a') as rec:
        for count in range(1, jmlRec + 1):
            print(f'Masukkan record nilai mahasiswa ke {count}')
            nama = input('Nama: ')
            nilai = input('Nilai: ')
            
            rec.write(nama + '\n')
            rec.write(nilai + '\n')
        
            print()
        
# Panggil fungsi main
main()

## ANOTHER EXAMPLE
# Program ini membaca record nilai mahasiswa
# dari file nilai_mahasiswa.txt
def main():

    # [1] Buka file nilai_mahasiswa.txt dengan statement with untuk dibaca
    # Pada body statement with:
    # - Gunakan loop while untuk membaca field-field dari semua record
    # - Tampilkan record dengan tampilan:
    #           Nama: <nama_mahasiswa>
    #           Nilai: <nilai_mahasiswa>
    with open('nilai_mahasiswa.txt', 'r') as rec:
        nama = rec.readline()
        while nama != '':
            nilai = rec.readline()
            
            #Strip karakter baris baru dari field
            nama = nama.rstrip('\n')
            nilai = nilai.rstrip('\n')
            
            print(f'Nama: {nama}')
            print(f'Nilai: {nilai}')
            print()
            
            nama = rec.readline()



# Panggil fungsi main
main()

