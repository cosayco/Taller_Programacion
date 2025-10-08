import numpy as np

#Ejercicio 1
a = np.array([10, 20, 30, 40, 50])
print("Tipo:", type(a))
print("Tamaño:", a.size)
print("Forma:", a.shape)

#Ejercicio 2
matriz = np.zeros([3, 4])
print("Matriz de ceros:\n", matriz)

#Ejercicio 3
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
suma = a + b
print("Suma:", suma)

#Ejercicio 4
identidad = np.eye(4)
identidad[np.diag_indices(4)] = 5
print("Matriz modificada:\n", identidad)

#Ejercicio 5
densidades = np.array([[2.7, 7.8], [10.5, 8.9]])
print("Media:", np.mean(densidades))
print("Máximo:", np.max(densidades))
print("Mínimo:", np.min(densidades))

#Ejercicio 6
aleatoria = np.random.rand(3, 3)
print("Matriz aleatoria:\n", aleatoria)
