# Fungsi bantu untuk mencari indeks dari nilai minimum dalam data
# Fungsi ini mengembalikan indeks nilai minimum dari data
def indeks_minimum(data):
    # [1] Tuliskan kode untuk mencari indeks nilai minimum
    # dan kembalikan indeks tersebut.
    indeks_min = 0
    min = data[indeks_min]
    for indeks in range(1, len(data)):
        if data[indeks] <= min:
            indeks_min = indeks
            min = data[indeks_min]

    return indeks_min


# Fungsi penyortiran seleksi secara rekursif
    
def selection_sort_rekursif(data):
    data_tersortir = []
    if len(data) <= 1:
        return data
    else:
        indeksmin = indeks_minimum(data)
        data_tersortir.append(data[indeksmin])
        data.pop(indeksmin)
    
        
    return selection_sort_rekursif(data_tersortir) + selection_sort_rekursif(data)


## ANOTHER EXAMPLE OF SELECTION SORT USING TO FIND MEDIAN OF A LIST
def sortir(data):
    # [1] Tuliskan kode algoritma penyortiran di bawah
    if len(data) < 2:
        return data
    else:
        pivot = data[0]
        lebih_kecil = []
        lebih_besar = []
        
        for elm in data[1:]:
            if elm <= pivot:
                lebih_kecil.append(elm)
            else:
                lebih_besar.append(elm)
        
        return sortir(lebih_kecil) + [pivot] + sortir(lebih_besar)
    
    
# Fungsi median menerima argumen sebuah list
# dan mengembalikan nilai median dari data dalam list tersebut
def median(data):
    # [2] Gunakan fungsi sortir untuk menyortir data
    sortir_data = sortir(data)
    
    # [3] Hitung median dengan dua kondisi untuk jumlah data genap dan jumlah data ganjil
    # lalu kembalikan nilai median
    n = len(data)
    median = (n - 1) // 2
    
    if n % 2 == 1:
        return sortir_data[median]
    else:
        return (sortir_data[median] + sortir_data[median + 1]) / 2.0
   