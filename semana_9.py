import tkinter as tk
from tkinter import ttk
import mysql.connector

# Configuración de la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="logistica"
)

mycursor = mydb.cursor()

# Función para agregar un nuevo envío
def agregar_envio():
    # Obtener datos de los campos de entrada
    numero_seguimiento = entry_numero_seguimiento.get()
    origen = entry_origen.get()
    destino = entry_destino.get()
    fecha_entrega = entry_fecha_entrega.get()

    sql = "INSERT INTO logistica.envios (NumeroSeguimiento, Origen, Destino, FechaEntregaPrevista) VALUES (%s, %s, %s, %s)"
    val = (numero_seguimiento, origen, destino, fecha_entrega)
    mycursor.execute(sql, val)
    mydb.commit()

    # Actualizar la tabla de envíos
    mostrar_envios()

# Función para mostrar los envíos en una tabla
def mostrar_envios():
    # Limpiar la tabla actual
    for row in tree.get_children():
        tree.delete(row)

    # Obtener los datos de la base de datos
    mycursor.execute("SELECT * FROM logistica.envios")
    myresult = mycursor.fetchall()

    # Insertar los datos en la tabla
    for x in myresult:
        tree.insert("", "end", values=x)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Seguimiento de Envíos")

#Frame
frame_entrada = tk.Frame(ventana)

#Entradas
frame_entrada.pack(pady=10)
etiqueta_agregar=tk.Label(frame_entrada, text= "Agregar envio")
etiqueta_agregar.pack()
tk.Label(frame_entrada, text="Numero de seguimientio: ").pack(side=tk.LEFT)
entry_numero_seguimiento = tk.Entry(frame_entrada)
entry_numero_seguimiento.pack(side=tk.LEFT, fill=tk.X)
tk.Label(frame_entrada, text="Origen: ").pack(side=tk.LEFT)
entry_origen = tk.Entry(frame_entrada)
entry_origen.pack(side=tk.LEFT, fill=tk.X)
tk.Label(frame_entrada, text="Destino: ").pack(side=tk.LEFT)
entry_destino = tk.Entry(frame_entrada)
entry_destino.pack(side=tk.LEFT, fill=tk.X)
tk.Label(frame_entrada, text="Fecha de Entrega Prevista: ").pack(side=tk.LEFT)
entry_fecha_entrega = tk.Entry(frame_entrada)
entry_fecha_entrega.pack(side=tk.LEFT, fill=tk.X)


# Botón para agregar un envío
boton_agregar = tk.Button(ventana, text="Agregar Envío", command=agregar_envio)
boton_agregar.pack()

# Tabla para mostrar los envíos
tree = ttk.Treeview(ventana, columns=("ID", "NumeroSeguimiento", "Origen", "Destino", "FechaEntregaPrevista"))
tree.heading("ID", text="ID")
tree.heading("NumeroSeguimiento", text="Número de Seguimiento")
tree.heading("Origen", text="Origen")
tree.heading("Destino", text="Destino")
tree.heading("FechaEntregaPrevista", text="Fecha de Entrega Prevista")
# ... (otras columnas)
tree.pack()

# Llamar a la función para mostrar los envíos al iniciar la aplicación
mostrar_envios()

ventana.mainloop()