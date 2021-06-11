# Fungsi binary search rekursif menerapkan
# algoritma binary search secara rekursif
def binary_search_rekursif(num, data):
    low = 0
    high = len(data) - 1
    minus = -1
    
    
    while low <= high:
        last_index = low + high
        mid_index = (low + high) // 2
        if num == data[mid_index]:
            return mid_index
        elif num < data[mid_index]:
            low = binary_search_rekursif(num, data[0:mid_index-1])
        else:
            high = binary_search_rekursif(num, data[mid_index+1:last_index])
    return minus