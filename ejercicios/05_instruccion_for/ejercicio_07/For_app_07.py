import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Al presionar el botón Mostrar pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        
        contador_de_divisores = 0
        numero_pedido = prompt("Ingrese un numero", "Numero")

        while numero_pedido == None or not numero_pedido.isdigit():
            numero_pedido = prompt("Ingrese un numero", "Numero")

        numero_pedido = int(numero_pedido)

        rango_a_recorrer = range(1, numero_pedido)

        for numero in rango_a_recorrer:

            if numero_pedido % numero == 0:
                print(numero)
                contador_de_divisores += 1
        print("-------------------")

        alert("Divisores", f"Se encontraron {contador_de_divisores} divisores")
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()