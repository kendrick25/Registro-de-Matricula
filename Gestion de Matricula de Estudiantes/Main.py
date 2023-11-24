from tkinter import *
from tkinter import ttk
from Conexion import * 
from tkinter import messagebox
def seleccionar(event):

    id =tvEstudiantes.selection()[0]

    if int(id)>0:

        cedula.set(tvEstudiantes.item(id, "values")[1])

        nombre.set(tvEstudiantes.item(id, "values")[2])

        direccion.set(tvEstudiantes.item(id, "values")[3])

        carrera.set(tvEstudiantes.item(id, "values")[4])

        año.set(tvEstudiantes.item(id, "values")[5])



def vaciar_tabla():

    filas=tvEstudiantes.get_children()

    for fila in filas:

        tvEstudiantes.delete(fila)



def llenar_tabla():

    vaciar_tabla()

    sql="select * from estudiante"

    db.cursor.execute(sql)

    filas = db.cursor.fetchall()

    for fila in filas:

        id=fila[0]

        tvEstudiantes.insert("",END,id,text=id,values=fila)

def eliminar():

    id=tvEstudiantes.selection()[0]

    if int(id)>0:

        sql = "DELETE FROM estudiante WHERE id="+id

        db.cursor.execute(sql)

        db.connection.commit()

        tvEstudiantes.delete(id)

        messagebox.showinfo("Advertecia...!", "Registro borrado con éxito!")

        limpiar()

    else:

        messagebox.showinfo("Advertecia...!", "Seleccione un registro para se eleminado!")

def modificarFalse():

    global modificar

    modificar=False

    tvEstudiantes.config(selectmode=NONE)

    btn_adicion.config(text="Guardar")

    btn_modificar.config(text="Seleccionar")

def modificarTrue():

    global modificar

    modificar=True

    tvEstudiantes.config(selectmode=BROWSE)

    btn_adicion.config(text="Adicionar")

    btn_modificar.config(text="Modificar")

def adicion():

    if modificar==False:

        if validar():

            val= (cedula.get(),nombre.get(), direccion.get(),carrera.get(),año.get())

            sql= "insert into estudiante(cedula, nombre, direccion, carrera, año) value(%s,%s,%s,%s,%s)"

            db.cursor.execute(sql, val)

            db.connection.commit()

            messagebox.showinfo("Advertecia...!", "Registro guardado con éxito!")

            llenar_tabla()

            limpiar()

        else:

            messagebox.showinfo("Advertecia...!", "no se permiten campos en blanco")

    else:

        modificarFalse()



def modificar():

        if modificar==True:

            if validar():
                val= (cedula.get(),nombre.get(), direccion.get(),carrera.get(),año.get())
                sql= "update estudiante set cedula=%s, nombre=%s, direccion=%s, carrera=%s, año=%s where id="+tvEstudiantes.selection()[0]

                db.cursor.execute(sql, val)
                db.connection.commit()
                messagebox.showinfo("Advertecia...!", "Registro guardado con éxito!")

                llenar_tabla()
                limpiar()

            else:

                messagebox.showinfo("Advertecia...!", "no se permiten campos en blanco")

        else:

            modificarTrue()



def salir():

    ventana.destroy()

def limpiar():

    cedula.set("")

    nombre.set("")

    direccion.set("")

    carrera.set("")

    año.set("")
    
def Actualizar():
    llenar_tabla()
    messagebox.showinfo("Advertecia...!", "Ya se actualizado la tabla")

def validar():

    return len(cedula.get()) and len(nombre.get()) and len(direccion.get()) and len(carrera.get()) and len(año.get())


#Colores
fondo_botones = "#919191"
txt_entradas = "#76d55d"

ventana = Tk()

#Variables
db = DataBase()
moficicar= False
cedula = StringVar()
nombre = StringVar()
direccion = StringVar()
carrera = StringVar()
año = StringVar()
ventana.title("Formulario de Gestiòn de Estudiantes")
ventana.geometry("800x600")
ventana.resizable(width=False, height=False)
fondo =PhotoImage(file="Formulario de Gestión de Estudiantes.png")
fondo1 = Label(ventana, image=fondo).place(x=0,y=0,relwidth=1,relheight=1)
#Tabla de lista de estudiantes
#----------------------------------------------------------------------------------------------
tvEstudiantes=ttk.Treeview(ventana,height=6,selectmode=NONE)
tvEstudiantes.place(x=22,y=330)
tvEstudiantes["columns"] =("ID","CEDULA","NOMBRE","DIRECCION","CARRERA", "AÑO")
tvEstudiantes.column("#0",width=0, stretch=NO)
tvEstudiantes.column("ID",width=50)
tvEstudiantes.column("CEDULA",width=100)
tvEstudiantes.column("NOMBRE",width=150)
tvEstudiantes.column("DIRECCION",width=200)
tvEstudiantes.column("CARRERA",width=150)
tvEstudiantes.column("AÑO",width=100)
tvEstudiantes.heading("#0",text="")
tvEstudiantes.heading("ID",text="ID",anchor=CENTER)
tvEstudiantes.heading("CEDULA",text="Cedula",anchor=CENTER)
tvEstudiantes.heading("NOMBRE",text="Nombre",anchor=CENTER)
tvEstudiantes.heading("DIRECCION",text="Direccion",anchor=CENTER)
tvEstudiantes.heading("CARRERA",text="Carrera",anchor=CENTER)
tvEstudiantes.heading("AÑO",text="Año",anchor=CENTER)

tvEstudiantes.bind("<<TreeviewSelect>>",seleccionar)

#Textbox de Entrada
txt_año=Entry(ventana,textvariable=año, width=14, relief="flat", bg="white",font=(14))
txt_año.place(x=124,y=163)

txt_carrera=Entry(ventana,textvariable=carrera, width=36, relief="flat", bg="white",font=(14)) 
txt_carrera.place(x=401,y=163)

txt_cedula=Entry(ventana,textvariable=cedula, width=19, relief="flat", bg="white", font=(14)) 
txt_cedula.place(x=124,y=208)

txt_nombre=Entry(ventana,textvariable=nombre, width=37, relief="flat", bg="white",font=(14)) 
txt_nombre.place(x=401,y=210)

txt_direccion = Entry(ventana,textvariable=direccion, width=66, relief="flat",bg="white" , font=(14))
txt_direccion.place(x=139,y=259)
#Botones
#--------------------------------------------------------------------------------------------------------
btn_adicion =Button(ventana, text="Crear Nuevo", command=adicion, cursor="hand2", 
bg="#0041FF",fg="white", width=10, height=1, relief="flat",
font=("Comic Sans MS",11,"bold"))
btn_adicion.place(x=664,y=528)
#--------------------------------------------------------------------------------------------------------
btn_modificar =Button(ventana, text="Seleccionar", cursor="hand2", command=modificar, 
bg="#FFAC00",fg="white", width=8,height=1, relief="flat",
font=("Comic Sans MS",11,"bold"))
btn_modificar.place(x=660,y=97)
#--------------------------------------------------------------------------------------------------------
boton2 =Button(ventana, text="Eliminar", cursor="hand2", command=eliminar, bg="#FF0800",fg="white", 
width=8,height=1, relief="flat",
font=("Comic Sans MS",11,"bold"))
boton2.place(x=546,y=97)
#--------------------------------------------------------------------------------------------------------
boton2 =Button(ventana, text="Actualizar", cursor="hand2", command=Actualizar, bg="#0034FF",fg="white", 
width=8,height=1, relief="flat",
font=("Comic Sans MS",11,"bold"))
boton2.place(x=416,y=97)
#--------------------------------------------------------------------------------------------------------
boton3 =Button(ventana, text="Finalizar", cursor="hand2", command=salir, bg="#858585",fg="white", width=14,height=2, 
relief="flat",
font=("Comic Sans MS",11,"bold"))
boton3.place(x=495,y=517)
#--------------------------------------------------------------------------------------------------------
llenar_tabla()
ventana.mainloop()