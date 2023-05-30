# angka=123
def jumlah_digit(n):
    nstr=str(n)
    total=0
    for i in nstr:
        total=total+int(i)
    return total

hasil= jumlah_digit(12345)
print(hasil)

def jumlah_digit_rekursif(n):
    if n<10:
        return n
    else:
        return n %10 + jumlah_digit_rekursif(n//10)

hasil=jumlah_digit_rekursif(12345)
print(hasil)
