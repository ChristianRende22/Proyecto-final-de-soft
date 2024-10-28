indice= float(input("Introduce el indice de la nota: "))
dtrevesti= float(input("Introduce el dtrevesti de la nota: "))
Matriz= float(input("Introduce la matriz de la nota: "))
Borrador= float(input("Introduce el borrador de la nota: "))
mapadigi= float(input("Introduce el mapa de digitos de la nota: "))
podcst= float(input("Introduce el poder de la nota: "))
nota1= float(input("Introduce la nota 1: "))
nota2= float(input("Introduce la nota 2: "))
nota3= float(input("Introduce la nota 3: "))
nota4= float(input("Introduce la nota 4: "))

notas= nota1 + nota2 + nota3 + nota4 

notaF= notas * .05
notaI= indice * .05
notade= dtrevesti * .05
notaM= Matriz * .05
notaB= Borrador *.1
notaM2= mapadigi * .05
notaP= podcst * .15

print("Nota de la asignatura: PI")
print("Nota 1: ", nota1)
print("Nota 2: ", nota2)
print("Nota 3: ", nota3)
print("Nota 4: ", nota4)
print(notaF)
print("Indice: ", notaI)
print("Dtrevesti: ", notade)
print("Matriz: ", notaM)
print("Borrador: ", notaB)
print("Mapa de digitos: ", notaM2)
print("PODCST: ", notaP)

SUMMA= notaI + notade + notaM + notaB + notaM2 + notaP + notaF
print("Total: ", SUMMA)