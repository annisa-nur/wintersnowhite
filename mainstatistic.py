import statistic

def main():

    nama_file = input('Masukkan nama file: ')

    try:
        with open(nama_file, 'r') as input_file:
            data = input_file.readlines()
            
            for idx in range(len(data)):
                data[idx] = float(data[idx])
                
            data_mean = statistic.mean(data)
            data_var = statistic.var(data)
            data_std = statistic.std(data)
            data_median = statistic.median(data)
            
            print(f'Mean dari data: {data_mean:.2f}')
            print(f'Variansi dari data: {data_var:.2f}')
            print(f'Standar Deviasi dari data: {data_std:.2f}')
            print(f'Median dari data: {data_median:.2f}')

    except FileNotFoundError:
        print(f'File {nama_file} tidak ditemukan.')
    
    except ValueError:
        print(f'File {nama_file} berisi data non-numerik.')
        
# Panggil fungsi main
main()