

"""

imc = peso / (altura^2)


imc <= 18 bajo peso
18 < imc < 26 peso normal
imc >= 26 sobre peso 

"""

peso = input("Ingrese peso del paciente: ")
peso = float(peso)


altura = input("Ingrese altura del paciente: ")
altura = float(altura)


imc = peso / (altura**2)

print("El paciente tiene un imc:",imc)


if imc <= 18:
    print("Bajo peso")
elif imc<26:
    print("Peso normal")
else:
    print("Sobre peso")