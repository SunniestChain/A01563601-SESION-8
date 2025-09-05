par = False
x=0
while par == False:
    x = float(input("numero: "))
    if x%2 != 0:
        print('parr imbecil!!')
        par = False
    else:
        par = True

print("ya ahora si feliz")
print('numero: ',x)