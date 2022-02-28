total = 0
jumlah = 0
stop = False

while stop == False :
    angka = input ("inpu angka: ")

    if angka == "":
        stop = True
    else:
        angka = float(angka)
        total += angka
        jumlah += 1

print(total)
print (jumlah)

rata2 = total / jumlah
print(rata2)