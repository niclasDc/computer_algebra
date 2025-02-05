import random
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def random_pairs_y_X():
    X = random.sample(range(0, 21), 6)  # Se asegura de que no haya valores repetidos
    y = [random.randint(0, 20) for _ in range(6)]
    pairs = list(zip(X, y))  # Generamos pares directamente a partir de X y Y
    return pairs, y, X

def newton_divided_differences(X, Y):
    n = len(X)
    coef = [y for y in Y]  # Copiamos los valores iniciales de Y
    
    for i in range(1, n):  # Iteramos sobre el número de niveles de la tabla
        for j in range(n - 1, i - 1, -1):  # Recorremos de atrás hacia adelante
            coef[j] = (coef[j] - coef[j - 1]) / (X[j] - X[j - i])

    return coef  # Estos son los coeficientes del polinomio de Newton


pairs, y, X = random_pairs_y_X()

def newton_polynomial(x, X, coef):
    """Evalúa el polinomio de Newton en un valor x dado"""
    n = len(X)
    p = coef[0]
    term = 1
    for i in range(1, n):
        term *= (x - X[i - 1])  # Producto acumulado (x - x0)(x - x1)...
        p += coef[i] * term  # Agregar el siguiente término
    return p

def plot_interpolation(X, Y, coefficients):
    """Grafica los puntos de interpolación y la función interpolante"""
    x_values = np.linspace(min(X) - 1, max(X) + 1, 300)  # Valores suaves en el rango
    y_values = [newton_polynomial(x, X, coefficients) for x in x_values]

    plt.figure(figsize=(8, 6))
    
    # Graficamos los puntos de interpolación
    plt.scatter(X, Y, color='red', label="Puntos dados")
    
    # Graficamos la función interpolante
    plt.plot(x_values, y_values, label="Polinomio interpolante", color='blue')
    
    # Configuración del gráfico
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Interpolación de Newton")
    plt.legend()
    plt.grid(True)
    
    plt.savefig("output.png")
    

# Generamos los datos y calculamos el polinomio
pairs, y, X = random_pairs_y_X()
coefficients = newton_divided_differences(X, y)

# Mostramos la gráfica
plot_interpolation(X, y, coefficients)

