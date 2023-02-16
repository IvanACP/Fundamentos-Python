def nuevoTema(tema):
    print("\n=========", tema, "=========\n")

#Este es un comentario de una linea 
nuevoTema("Operadores aritmeticos")
print("Operador division entera (10 // 3:", 10 // 3)#Operador //
print("Operador potencia (5 ** 3):",5 ** 3)#Operador **

nuevoTema("Operadores aritmeticos")
print("Operador and (True and False):",True and False)

#Actividad: Imprimir la tabla de verdad de los operadores logicos.

nuevoTema("Operadores aritmeticos")
print("Operador and (True and True):",True and True)
print("Operador and (True and False):",True and False)
print("Operador and (True and True):",False and True)
print("Operador and (True and False):",False and True)

print("Operador or (True or False):",True or True)
print("Operador or (True or False):",True or False)
print("Operador or (True or False):",False or True)
print("Operador or (True or False):",False or False)

print("Operador not (True not False):",False)
print("Operador not (True not False):",True)


#AcTIVIDAD: Agregar los demas operadores de comparacion
nuevoTema("Operadores aritmeticos")
print("2==3", 2==3)
print("2!=3", 2!=3)
print("2<3", 2<3)
print("2<=3", 2<=3)
print("2>3",2>3)
print("2>=3", 2>=3)

nuevoTema("Variables")
variable1=10
variable2=6.24
variable3="Juancho"
dosPalabras="Hola"
dos_Palabras="hello"

print(variable1,variable2,variable3,dos_Palabras,dosPalabras)

a,b,c=10,5.16,"Palabra"
print(a,b,c)

nuevoTema("Enteros")
w=105
x=54395839486
y=-256
z=0b00110011
h=0xffa

print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Numeros flotantes")
x=1297.50
print(x, type(x))
y=0.5637939
print(y,type(y))


nuevoTema("Numero Complejos")
x=-46j
y=12+45j
z=2j
print(x,type(x))
print(y,type(y))
print(z,type(z))

nuevoTema("Booleanos")
lis=[8]
print(lis, "Es", bool(lis))
t=()
print(t, "Es", bool(t))
new="HEllo"
print(new,"Es",bool(new))
num=99
print(num,"Es",bool(num))
comp=1+0j
print(comp,"Es",bool(comp))
val=None#None equivale a NUll
print(val,"Es",bool(val))


nuevoTema("Listas")#No son arreglos
a=[10,20.5,"Pythonlis"]
print(a)
print(a[1])
a[0]="HOLA"
print(a)

nuevoTema("Tuplas")
t=(25,"tuple", 1+10j,3.1416)
print(t)
print(t[2])
print("t[1:4]", t[1:4])#Rango
#t[1]=34 operacion no valida en tuplas. 


nuevoTema("Conjuntos")
t={50,20,30,40,10,50}
print("Conjunto t=", t, type(t))


nuevoTema("Diccionario")
d={1:"Valor1", "Valor2":2j}
print(d, type(d))
print("d[Valor2]:", d["Valor2"])

nuevoTema("Cadenas")
cadena1 = "Cadena con comillas dobles"
cadena2 = "Cadena con comillas simples"

print(cadena1, type(cadena1))
print(cadena2, type(cadena2))

cadenaMultilinea='''Esta es una cadena y de varias lineas con tabulares y saltos de linea'''
print(cadenaMultilinea)
print("Segmentacion de cadenas")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1="hola"
cadena4=(cadena1+" ")*5
print(cadena4)
cadena5=cadena4.upper()
print(cadena4)



