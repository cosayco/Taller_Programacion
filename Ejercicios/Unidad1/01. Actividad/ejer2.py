PI=3.1416

muestra=int(input("Ingrese cantidad de muestras:"))

for i in range(muestra):
    print("Muestra N°", i + 1)
    radio=float(input("Ingrese valor radio:"))
    altura=float(input("Ingrese valor de altura"))
    volumen=PI * radio**2 * altura
    print("Volumen=",volumen)


