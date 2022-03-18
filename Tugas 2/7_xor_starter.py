mesaji = "label"
hasil = ""
for i in  mesaji:
    hasil += chr(ord(i)^13)

print(hasil)