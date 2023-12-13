# Ejercicio 1 A partir de una lista vacía, utilizar un ciclo while para cargar allí
#             números negativos del -15 al -1
n = -15
lista = []
while n < 0:
    lista.append(n)
    n +=1
    #print(lista)

print(f'La lista final es: {lista}\n')

# Ejercicio 2 ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo
#              los números pares?
# Respuesta = Si
n= 0
while n<len(lista):
    if (lista[n]%2==0):
        print(lista[n])
    n += 1

print()
print('---------------------------------------------------\n')

# Ejercicio 3 Resolver el punto anterior sin utilizar un ciclo while
for i in lista:
    if i%2==0:
        print(i)
        
print()
print('---------------------------------------------------\n')

# Ejercicio 4 Utilizar el iterable para recorrer sólo los primeros 3 elementos
for i in lista[:3]:
    print(i)

print()
print('---------------------------------------------------\n')

# Ejercicio 5 Utilizar la función **enumerate** para obtener dentro del iterable,
#             tambien el índice al que corresponde el elemento
for i,n in enumerate(lista):
    print(f'Indice: {i}, Elemento: {n}')

print()
print('---------------------------------------------------\n')

# Ejercicio 6 Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo
#             donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

listaX = [1,2,5,7,8,10,13,14,15,17,20]
for i in range(1,20):
    if i in listaX:
        continue
    else:
        listaX.insert(i-1,i)
print(listaX)
print('------------Ejercicio 7---------------------------------------\n')

# Ejercicio 7 La sucesión de Fibonacci es un listado de números que sigue la fórmula:
#             n0 = 0
#             n1 = 1
#             ni = ni-1 + ni-2
#             Crear una lista con los primeros treinta números de la sucesión.
fibo = []
for n in range(30):
    if n == 0 or n == 1:
        fibo.append(n)
    else:
        fibo.append(fibo[n-1]+fibo[n-2])

print(fibo)
print()
print('------------Ejercicio 8---------------------------------------\n')

# Ejercicio 8 Realizar la suma de todos los elementos del punto anterior
print(sum(fibo))
print()
print('------------Ejercicio 9---------------------------------------\n')

# Ejercicio 9 La proporción aurea se expresa con una proporción matemática que nace el número irracional
#             Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la
#             sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los
#             últimos 5 pares de dos números contiguos:
#             Donde i es la cantidad total de elementos
#             ni-1 / ni
#             ni-2 / ni-1
#             ni-3 / ni-2
#             ni-4 / ni-3
#             ni-5 / ni-4
Phi = []
n= -1
while n > -6:
    print(fibo[n]/fibo[n-1])
    n -= 1
print()
print('------------Ejercicio 10---------------------------------------\n')

# A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'



 
