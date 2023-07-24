'''
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por consola (print)

'''
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        
        ciclo = True
        maximo_de_votos = -1
        contador = 0
        bandera = True
        nombre_maximo_votos = ""
        nombre_minimo_votos = ""
        minimo_de_votos = None
        edad_minima = None
        edad_maxima = None
        acumulador_de_edad = 0
        acumulador_de_votos = 0

       
        while True:

            nombre = prompt(title = "Nombre", prompt = "Ingrese el nombre del candidato")
            while  nombre == None  or not nombre.isalpha():
                nombre = prompt("Nombre","Ingrese el nombre del candidato")

            edad = prompt("Edad", "Ingrese su edad")
            while edad == None or not edad.isdigit() or int(edad) < 25:
                edad = prompt("Edad", "Ingrese una edad valida")

            edad = int(edad)

            cantidad_de_votos = prompt("Votos", "Cantidad de votos")
            while cantidad_de_votos == None or not cantidad_de_votos.isdigit() or int(cantidad_de_votos) <= 0:
                cantidad_de_votos = prompt("Error", "Ingrese una cantidad valida")
            
            cantidad_de_votos = int(cantidad_de_votos)

            if bandera == True:
                maximo_de_votos = cantidad_de_votos
                minimo_de_votos = cantidad_de_votos
                nombre_maximo_votos = nombre
                nombre_minimo_votos = nombre
                edad_minima = edad
                edad_maxima = edad
                bandera = False

            else:
                if cantidad_de_votos > maximo_de_votos:
                    maximo_de_votos = cantidad_de_votos
                    nombre_maximo_votos = nombre
                    edad_maxima = edad
                elif cantidad_de_votos < minimo_de_votos:
                    minimo_de_votos = cantidad_de_votos
                    nombre_minimo_votos = nombre
                    edad_minima = edad

            acumulador_de_edad += edad
            contador += 1
            acumulador_de_votos += cantidad_de_votos


            pregunta = question("Pregunta", "¿Desea continuar?")

            if not pregunta:
             break  
        
        promedio = acumulador_de_edad / contador
        print(f"el candidato con mayor numeros de votos es {nombre_maximo_votos} con {maximo_de_votos} votos")
        print(f"el candidato con menor numeros de votos es {nombre_minimo_votos} de {edad_minima} años con {minimo_de_votos} votos")
        print(f"Promedio de edad {promedio}")
        print(f"Total de votos {acumulador_de_votos}")     




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
