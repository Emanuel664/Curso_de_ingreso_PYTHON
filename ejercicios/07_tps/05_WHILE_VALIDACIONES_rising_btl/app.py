import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
       
        apellido = prompt("Datos","Ingrese su apellido")
      
        while (apellido == None or apellido == "")or not apellido.isalpha():

            apellido = prompt("Apellido", "Ingrese su apellido")

            edad = prompt("Edad", "Ingrese su edad")

            while edad == None or edad.isdigit() == False or int(edad) < 19 or int(edad) > 90:
                edad = prompt(title = "Edad", prompt = "Ingrese una edad valida")
            edad = int(edad)

            estado_civil = prompt("Estado civil", "Ingrese su estado civil")
            while (estado_civil == None or not estado_civil.isalpha()) or estado_civil != "Soltero" or estado_civil != "Soltera" or estado_civil != "Casado" or estado_civil != "Casada" or estado_civil != "Divorciado" or estado_civil != "Divorciada" or estado_civil != "Viudo" or estado_civil != "Viuda":
                estado_civil = prompt("Estado civil", "Reingrese su estado civil")

                if estado_civil == "Soltero" or estado_civil == "Soltera":
                    estado_civil == "Soltero/a"
                elif estado_civil == "Casado" or estado_civil == "Casada":
                    estado_civil == "Casado/a"
                elif estado_civil == "Divorsiado" or estado_civil == "Divorsiada":
                    estado_civil == "Divorsiado/a"
                else:
                    estado_civil = "Viudo/a"

                legajo = prompt(title = "Legajo", prompt = "Ingrese su legajo")
                while legajo == None or not legajo.isdigit() or int(legajo) < 1000 or int(legajo) > 9999:
                    legajo = prompt(title = "Legajo", prompt = "Ingrese un legajo valido")
                legajo = int(legajo)

                self.txt_apellido.delete(0,100)
                self.txt_apellido.insert(0,apellido)
                self.txt_edad.delete(0,100)
                self.txt_edad.insert(0,edad)
                self.combobox_tipo.set(estado_civil)
                self.txt_legajo.delete(0,100)
                self.txt_legajo.insert(0,legajo)

        





if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
