import math

def mean(data):
    mean = sum(data) / len(data)
    return mean

def var(data):
    var = 0
    for i in data:
        var += (i - mean(data)) ** 2
    result = var / len(data)
    return result

def std(data):
    std = var(data) ** (1/2)
    return std

def sortir(data):
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


def median(data):
    sortir_data = sortir(data)
    n = len(data)
    median = (n-1) // 2

    if n % 2 == 1:
        return sortir_data[median]
    else:
        return (sortir_data[median] + sortir_data[median + 1]) / 2.0


'''
def mean(data):
    mean = sum(data) / len(data)
    return mean

def var(data):
    sum = 0
    for i in (0, len(data)-1):
        var = (data[i] - mean(data)) ** 2
        penyebutsum = var + sum
        sum = penyebutsum

    varvalue = penyebutsum / len(data)
    return varvalue

def std(data):
    std = var(data) ** (1/2)
    return std

def sortir(data):
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


def median(data):
    sortir_data = sortir(data)
    n = len(data)
    median = (n-1) // 2

    if n % 2 == 1:
        return sortir_data[median]
    else:
        return (sortir_data[median] + sortir_data[median + 1]) / 2.0
'''