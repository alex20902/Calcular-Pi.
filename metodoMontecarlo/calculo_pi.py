#calculo de pi.
#Puntos aleatorios dentro del cuadrado y circulo.
#Resultado.

#Hugo Alexander Vázquez Montejo.

import random
import tkinter as tk
from tkinter import Canvas

def monte_carlo_pi(num_samples):
    inside_circle = 0
    outside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1
        else:
            outside_circle += 1

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate, inside_circle, outside_circle

def calcular_pi():
    num_samples = int(entry_samples.get())
    pi_estimate, inside_circle, outside_circle = monte_carlo_pi(num_samples)
    resultado_label.config(text=f"Estimación de π: {pi_estimate}")
    puntos_dentro_label.config(text=f"Puntos dentro del círculo: {inside_circle}")
    puntos_fuera_label.config(text=f"Puntos fuera del círculo: {outside_circle}")
    
    canvas.delete("all")

    canvas.create_oval(50, 50, 250, 250, outline="blue")

    for _ in range(num_samples):
        x = random.uniform(50, 250)
        y = random.uniform(50, 250)
        distance = (x - 150)**2 + (y - 150)**2

        if distance <= 10000:  # El radio del círculo es 100 (radio al cuadrado = 10000)
            canvas.create_oval(x, y, x + 2, y + 2, fill="yellow")  # Puntos dentro del círculo
        else:
            canvas.create_oval(x, y, x + 2, y + 2, fill="red")   # Puntos fuera del círculo


window = tk.Tk()
window.title("--Cálculo de π--")

window.configure(bg="lightgreen")

sample_label = tk.Label(window, text="Número de Muestras:")
sample_label.pack()
entry_samples = tk.Entry(window)
entry_samples.pack()

calculate_button = tk.Button(window, text="Calcular π", command=calcular_pi)
calculate_button.pack()

# Resultados numéricos
resultado_label = tk.Label(window, text="")
resultado_label.pack()

puntos_dentro_label = tk.Label(window, text="")
puntos_dentro_label.pack()

puntos_fuera_label = tk.Label(window, text="")
puntos_fuera_label.pack()

canvas = Canvas(window, width=300, height=300, bg="white")
canvas.pack()

window.mainloop()

