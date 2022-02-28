'''thn_lahir'' = input ("masukan tahun_lahir anda!")
thn_lahir = int(thn_lahir)

# umur = tahun sekarang - tahun lahir
umur = 2021 - thn_lahir
print(" umur Anda adalah=", umur)

if umur <= 13 :
    print("Anda memasuki katagori Anak-anak")
elif umur <= 20 :
    print("Anda memasuki katagori Remaja ")
elif umur <= 39 :
    print("Anda memasuki katagori Dewasa ")
else :
    print("Anda memasuki katagori Tua ")
'''
angka1 = int(input(""))
angka2 = int(input(""))

if angka1 < angka2 :
    print(angka1)
else :
    print(angka2)
