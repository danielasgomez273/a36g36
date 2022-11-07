import sqlite3
conexionSqlite3 = sqlite3.connect("crandoBDdePrueba.db")
cursor = conexionSqlite3.cursor()

def CreatePaciente(): #(nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente)
    nombre_paciente = "'david'"+","
    apellido_paciente = "'costa'"+","
    telefono_paciente = "'2644641117572'"+","
    email_paciente = "'da91@gmail.com'"+","
    contraseña_paciente ="'1aa1223'"
    datosUsuario = nombre_paciente + apellido_paciente + telefono_paciente + email_paciente + contraseña_paciente
    sentenciaSql= '''
            INSERT INTO paciente (nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente)
            VALUES (''' + datosUsuario + ");"    
    try:
        cursor.execute(sentenciaSql)
        conexionSqlite3.commit()
        conexionSqlite3.close()
        print("Guarde en BD=> ", datosUsuario)
       
    except:
        print("Ocurrio un error al guardar datos en BD")

def ReadPacienteByID(ID):
    sentenciaSql= "SELECT * FROM paciente WHERE paciente.idpaciente ="+ ID + ";"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd Read=> ",lecturaBD)
        conexionSqlite3.close()
    except:
        print("Ocurrio un error al leer datos de BD")

def ReadAllPacientes():
    sentenciaSql= "SELECT * FROM paciente;"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd ReadAll=> ",lecturaBD)
        conexionSqlite3.close()
    except:
        print("Ocurrio un error al leer datos de BD")


def UpdatePacienteByID(ID,campo, valor):
    sentenciaSql= "UPDATE paciente SET " + campo + " = '" + valor +"' WHERE paciente.idpaciente="+ID
    print(sentenciaSql)
    try:
        cursor.execute(sentenciaSql)
        print("Update en BD de pte con ID",ID, "Se actualizo ", campo, "al valor ", valor)
        conexionSqlite3.commit()
        conexionSqlite3.close()
    except:
        print("Ocurrio un error al leer datos de BD")

def DeletePacienteByID(ID):
    sentenciaSql= "DELETE FROM paciente WHERE paciente.idpaciente ="+ ID + ";"
    try:
        cursor.execute(sentenciaSql)
        print("Borrado de bd PTE con id=",ID)
        conexionSqlite3.commit()
        conexionSqlite3.close()
    except:
        print("Ocurrio un error al leer datos de BD")



# LLAMADO DE FUNCIONES DE CRUD 

# CreatePaciente()
# ReadPacienteByID("3")
# ReadAllPacientes()
# DeletePacienteByID("5")
# UpdatePacienteByID("6", "nombre_paciente", "David")



