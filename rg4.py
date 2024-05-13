import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import math

def runge_kutta(f, x0, y0, h, n):
    """
    Implementación genérica del método de Runge-Kutta para resolver ecuaciones diferenciales.
    
    Args:
    f : función que representa la ecuación diferencial dy/dx = f(x, y)
    x0 : valor inicial de x
    y0 : valor inicial de y en x0
    h : tamaño del paso
    n : número de pasos
    
    Returns:
    x : array de valores de x
    y : array de valores de y correspondientes a cada x
    """
    x = np.zeros(n+1)
    y = np.zeros(n+1)
    x[0] = x0
    y[0] = y0
    
    for i in range(n):
        k1 = h * f(x[i], y[i])
        k2 = h * f(x[i] + h/2, y[i] + (k1/2))
        k3 = h * f(x[i] + h/2, y[i] + (k2/2))
        k4 = h * f(x[i] + h, y[i] + k3)
        
        x[i+1] = x[i] + h
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) * (1/6)
    
    return x, y

# Función para obtener la ecuación diferencial del usuario
def get_function():
    f_string = entry_function.get()
    return lambda x, y: eval(f_string)

def plot_solution(x_values, y_values):
    """
    Grafica la solución de la EDO.

    Args:
        x_values: Lista de valores de x.
        y_values: Lista de valores de y correspondientes a los valores de x.
    """
    fig = plt.figure()
    plt.plot(x_values, y_values, label='Solución de la EDO')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solución de la EDO usando Runge-Kutta')
    plt.legend()
    plt.grid(True)
    return fig  

def solve():
    # Obtener los valores ingresados por el usuario
    x0 = float(entry_x0.get())
    y0 = float(entry_y0.get())
    h = float(entry_h.get())
    n = int(entry_n.get())

    # Resolver la EDO usando el método de Runge-Kutta
    f = get_function()
    x_values, y_values = runge_kutta(f, x0, y0, h, n)

    # Graficar la solución
    fig = plot_solution(x_values, y_values)
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Mostrar los resultados en una etiqueta
    results_label.config(text="Resultados:\n" + "\n".join(f"x = {x_values[i]}, y = {y_values[i]}" for i in range(len(x_values))))

root= tk.Tk()
root.title("Runge-Kutta método")

# Crear cuadros de texto y etiquetas para los datos de entrada
tk.Label(root, text="Utiliza math.sqrt(n) para representar la raiz").pack()
tk.Label(root, text="Función que representa la ecuación diferencial:").pack()
entry_function = tk.Entry(root)
entry_function.pack()

tk.Label(root, text="Valor inicial de x:").pack()
entry_x0 = tk.Entry(root)
entry_x0.pack()

tk.Label(root, text="Valor inicial de y(x0):").pack()
entry_y0 = tk.Entry(root)
entry_y0.pack()

tk.Label(root, text="Tamaño del paso (h):").pack()
entry_h = tk.Entry(root)
entry_h.pack()

tk.Label(root, text="Número de pasos a realizar:").pack()
entry_n = tk.Entry(root)
entry_n.pack()

# Botón para resolver la EDO
solve_button = tk.Button(root, text="Resolver", command=solve)
solve_button.pack()

# Etiqueta para mostrar los resultados
results_label = tk.Label(root, text="")
results_label.pack()

# Iniciar el bucle principal de Tkinter
root.mainloop()
