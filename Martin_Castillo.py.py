#PRUEBA Y ERROR MONAMI
#Trabajo
import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x450")

Numeros = tkinter.Entry(ventana, font="Helvetica 20")
Numeros.grid(row=0, column=0, columnspan=10)

Cuadro_Final = tkinter.Label(ventana, text ="", font = "Helvetica 25", bg="lightgray" )
Cuadro_Final.grid(row=1, column=0, columnspan=10)

Ans = None
Last_OP = None
Last_Numb = None
def Limpiar():
    global Ans, Last_Numb, Last_OP
    Numeros.delete(0, tkinter.END)
    Cuadro_Final.config(text = "")
    Ans = None
    Last_OP = None
    Last_Numb = None

def resultado(numero):
    Numeros.insert(tkinter.END, numero)

def Borrar():
    texto_actual = Numeros.get()
    Numeros.delete(len(texto_actual)-1, tkinter.END)


def salir():
    ventana.destroy()

def Igual():
    global Ans, Last_Numb, Last_OP
    Expresion = Numeros.get().strip()
    Expresion = Expresion.replace("^", "**").replace("x", "*")
    print("============")
    print(Ans)

    try:
        if Expresion == "":
            if Ans is not None and Last_OP is not None and Last_Numb is not None:
                Expresion = f"{Ans}{Last_OP}{Last_Numb}"
                
                print("if")
            else:
                return
        if Ans is not None and Expresion[0] in "+-*/^":
                Expresion = str(Ans)+ Expresion
                print(Calculo,Expresion)
                print("elif")
        Calculo = eval(Expresion)
        print(Ans)
        Ans = Calculo
        print(Ans)       
        for i in range(len(Expresion)-1, -1,-1):
            if Expresion[i] in "+-*/^":
                Last_OP = Expresion[i]
                Last_Numb = Expresion[i + 1:].strip()
                break         
        Cuadro_Final.config(text=str(Calculo))
        Numeros.delete(0,tkinter.END)  
    except Exception as a:
        Numeros.delete(0, tkinter.END)
        Numeros.insert(tkinter.END, "Syntax Error")
        Cuadro_Final.config(text="")
        Ans = None
        Last_Numb = None
        Last_OP = None
        print("Error", a)


numeros = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
index = 0
for i in range(2, 5):          # filas  2, 3, 4
    for j in range(3):         # columnas 0, 1, 2
        if index < len(numeros):
            valor = numeros[index]
            boton = tkinter.Button(ventana, text=valor, width=10, height=5, command=lambda v=valor: resultado(v))
            boton.grid(row=i, column=j)
            index += 1

operaciones = [("+", "+"), ("/", "/"), ("-", "-"),("^", "**"), ("x", "*")]
posiciones = [(2,4), (2,5), (3,4), (3,5), (4,4)]

for (texto, simbolo), (fila, columna) in zip(operaciones, posiciones):
    tkinter.Button(ventana, text=texto, command=lambda s=simbolo: resultado(s),width=10, height=5).grid(row=fila, column=columna)

tkinter.Button(ventana, text="C", width=10, height=5, command=Limpiar).grid(row=5, column=0)
tkinter.Button(ventana, text="=", width=10, height=5, command=Igual, bg = "DodgerBlue3").grid(row=5, column=2)
tkinter.Button(ventana, text="Salir", width=21, height=5, command=salir).grid(row=5, column=4, columnspan=2)
tkinter.Button(ventana, text="0", width=10, height=5, command=lambda: resultado("0")).grid(row=5, column=1)

tkinter.Button(ventana, text="DEL", command=Borrar, width=10, height=5,bg ="lightcoral").grid(row=4, column=5)

ventana.mainloop()