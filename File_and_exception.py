def main():

    found = False
    
    try:
        inputfile = input("Masukkan nama file: ")

        with open(inputfile, 'r') as myfile :
            print(f"File {inputfile} berhasil dibuka.\n")
            namamhs = input("Masukkan nama mahasiswa yang ingin dicari: ")
            
            nama = myfile.readline()
            while nama != '':
                nilai = myfile.readline()
                nama = nama.rstrip('\n')
                nilai = nilai.rstrip('\n')
                
                
                if (nama == namamhs):
                    print(f"Nama Mahasiswa: {nama}")
                    print(f"Nilai: {nilai}")
                    found = True
                    

                nama = myfile.readline()

 
    except FileNotFoundError:
        print(f"File {inputfile} tidak ditemukan.")
        
    else :
        if found != True:
            print(f"Nama {namamhs} tidak ditemukan.")
        
                    
# Panggil fungsi main
main()