import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    La suma acumulada de los negativos
    La suma acumulada de los positivos
    Cantidad de números positivos ingresados
    Cantidad de números negativos ingresados
    Cantidad de ceros
    Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        acumulador_negativo = 0
        acumulador_positivo = 0
        numero_ingresado = ''
        contador_negativos = 0
        contador_positivos = 0
        contador_de_ceros = 0
        diferencia = 0

        while numero_ingresado != None:
            numero_ingresado = prompt("Numeros", "Ingrese un numero")

            if numero_ingresado != None:
                numero_ingresado = int(numero_ingresado)

                if numero_ingresado < 0 :
                    acumulador_negativo += numero_ingresado
                    contador_negativos += 1

                elif numero_ingresado > 0:
                    acumulador_positivo += numero_ingresado
                    contador_positivos += 1
                else:
                    contador_de_ceros += 1

        diferencia = contador_positivos - contador_negativos
        mensaje = f"La suma de los positivos es { acumulador_positivo} \n"
        mensaje = mensaje  + f" La suma de los negativos es {acumulador_negativo} \n"
        mensaje = mensaje + f"La cantidad de los positivos es {contador_positivos} \n"
        mensaje = mensaje + f"La cantidad de los negativos es {contador_negativos} \n"
        mensaje = mensaje + f"La cantidad de ceros es {contador_de_ceros} \n"
        mensaje = mensaje + f"La diferencia entre los negativos y positivos es {diferencia}"

        alert("Respuesta", message = mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
