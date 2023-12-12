import numpy as np
from random import *
import tkinter as tk


MAX_FIL = 1000
MAX_COL = 8
MAX_PADRES = 500    
MAX_ITER = 2000
PROB_MUTACION =0.05 #This is 5% probavility of mutation

class TableroAjedrez(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tablero de Ajedrez")
        self.geometry("400x400")
        self.crear_tablero()

    def crear_tablero(self):
        color = ["white", "black"]
        self.casillas = []
        for i in range(8):
            fila = []
            for j in range(8):
                square_color = color[(i + j) % 2]
                square = tk.Canvas(self, width=50, height=50, bg=square_color, borderwidth=0, highlightthickness=0)
                square.grid(row=i, column=j)
                fila.append(square)
            self.casillas.append(fila)

    def pintar_casilla_roja(self, row, col):
        # Verifica que la fila y la columna estén dentro del rango del tablero
        if 0 <= row < 8 and 0 <= col < 8:
            # Cambia el color de la casilla en la posición especificada a rojo
            self.casillas[row][col].configure(bg="red")

def crossover(i1, i2, p):
    for col in range(p,MAX_COL):
        aux = i1[col]
        i1[col] = i2[col]
        i2[col] = aux
        if random() > 1-PROB_MUTACION:
            i1[randint(0,7)]=randint(0,7)
            i2[randint(0,7)]=randint(0,7)
        return(i1,i2)

def evaluar_aptitud(solucion):
    ataques = 0
    n = len(solucion)
    for i in range(n):
        for j in range(i + 1, n):
            # Verificar si hay ataques en la misma fila o en diagonales
            if solucion[i] == solucion[j] or abs(solucion[i] - solucion[j]) == abs(i - j):
                ataques += 1
    if ataques == 0:
        return 0
    else:
        return 1/ataques

def calcula_fitness(sol, iter):
  #Calcula el fitness de todos los individuos de la poblacion
    fitness = np.zeros(MAX_FIL)
    for fil in range(MAX_FIL):
        fitness[fil]=evaluar_aptitud(sol[fil][:])
        if fitness[fil]==0:
            print("Iteración {} Solución: {}".format(iter, sol[fil][:], end=' '))
            app = TableroAjedrez()
            for col in range(8):
                app.pintar_casilla_roja(sol[fil][col],col)
            app.mainloop()
            for fil in range(MAX_FIL):
                print(sol[fil][:])
            exit(0)
    #Normaliza el fitness    
    for fil in range(MAX_FIL):
        fitness[fil]= fitness[fil] / np.sum(fitness)
    return(fitness)

def ini_poblacion():
    sol = np.ones((MAX_FIL,MAX_COL), dtype=int)
    for fil in range(MAX_FIL):
        for col in range(MAX_COL):
            sol[fil][col]= randint(0,7)
    return (sol)


def main():
    sol = ini_poblacion()
       
    for iter in range(MAX_ITER):
        #Calcula el fitness de todos los individuos de la poblacion
        fitness = calcula_fitness(sol, iter)
        sol_usada=np.zeros(MAX_FIL, dtype=int)
        #Selecion de MAX_PADRES padres
        
        padres = np.zeros((MAX_PADRES,8), dtype=int)
        p1=0
        while (p1 < MAX_PADRES):

            valor_ruleta=0
            detencion_ruleta=random()
            #Busca solucion donde se detuvo la ruleta
            for i in range(MAX_FIL):
                valor_ruleta += fitness[i]
                if (valor_ruleta > detencion_ruleta) and sol_usada[i]==0:
                    #Selecciona padre
                    padres[p1][:]= sol[i][:]
                    sol_usada[i] = 1
                    p1+=1 
                    break
        #Cruzamiento
        hijos = np.zeros((MAX_PADRES,8), dtype=int)
        for i in range(0,MAX_PADRES,2):
            hijos[i][:], hijos[i+1][:]=crossover(padres[i][:], padres[i+1][:], 4)

      
        #Remplazo aleatorio
        for i in range(MAX_PADRES):
            sol[randint(0,MAX_FIL-1)][:]=hijos[i][:]
  
           

if __name__ == "__main__":
    main()
