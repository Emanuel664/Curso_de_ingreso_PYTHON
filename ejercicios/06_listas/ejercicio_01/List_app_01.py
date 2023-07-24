import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón  'Mostrar', se deberán mostrar los números 
almacenados en el vector lista_datos utilizando Dialog Alert para informar cada elemento.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

        self.lista_datos = [2,3,5,7,11,13]


    def btn_mostrar_on_click(self):
        # lista_de_nombres = []

        # lista_de_nombres.append('Juan')

        # lista_de_nombres.append('Pedro')

        # lista_de_nombres.append('Juan')

        # print(lista_de_nombres.index('Juan'))

        # indice = 3

        # if len(lista_de_nombres) >= index:
        #     print(lista_de_nombres[3])

        # lista_de_nombres.pop()

        # for nombre in lista_de_nombres:
        #     print(nombre) 
         
        lista = self.lista_datos

        # contador = 0
        # while contador < len(lista):

        #     elemento = lista[contador]

        #     contador += 1

        #     print(elemento)

        alert("Lista", lista)

        
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()