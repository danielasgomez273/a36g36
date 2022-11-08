import sqlite3

def CreatePaciente(nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente):
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    nombre_paciente = "'"+nombre_paciente+"',"
    apellido_paciente = "'"+apellido_paciente+"',"
    telefono_paciente = "'"+telefono_paciente+"',"
    email_paciente = "'"+email_paciente+"',"
    contraseña_paciente = "'"+contraseña_paciente+"'"
    datosUsuario = nombre_paciente + apellido_paciente + telefono_paciente + email_paciente + contraseña_paciente

    sentenciaSql= '''
            INSERT INTO paciente (nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente)
            VALUES (''' + datosUsuario + ");"   
    print("sentencia sql => ",sentenciaSql)
    # try:
    cursor.execute(sentenciaSql)
    conexionSqlite3.commit()
    print("Guarde en BD=> ", datosUsuario)    
    # except:
    # print("Ocurrio un error al guardar datos en BD")
    # finally:
    conexionSqlite3.close()
    # return getIdPacienteByEmail(email_paciente)

def getIdPacienteByEmail(email_paciente):
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    resultados=None
    sentenciaSql= "SELECT idpaciente FROM paciente WHERE paciente.email_paciente ='"+ email_paciente + "';"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        resultados=lecturaBD
        print("ID leido desde bd getIdPacienteByEmail=> ",lecturaBD)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()
    return resultados


def ReadPacienteByID(ID):
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "SELECT * FROM paciente WHERE paciente.idpaciente ="+ ID + ";"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd Read=> ",lecturaBD)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()

def ReadAllPacientes():
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "SELECT * FROM paciente;"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd ReadAll=> ",lecturaBD)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()

def UpdatePacienteByID(ID,campo, valor):
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "UPDATE paciente SET " + campo + " = '" + valor +"' WHERE paciente.idpaciente="+ID
    print(sentenciaSql)
    try:
        cursor.execute(sentenciaSql)
        print("Update en BD de pte con ID",ID, "Se actualizo ", campo, "al valor ", valor)
        conexionSqlite3.commit()
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()

def DeletePacienteByID(ID):
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "DELETE FROM paciente WHERE paciente.idpaciente ="+ ID + ";"
    try:
        cursor.execute(sentenciaSql)
        print("Borrado de bd PTE con id=",ID)
        conexionSqlite3.commit()
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()


# LLAMADO DE FUNCIONES DE CRUD 

print("estoy retornando id dl pte",getIdPacienteByEmail('da91@gmail.com'))

# CreatePaciente()
# ReadPacienteByID("3")
# ReadAllPacientes()
# DeletePacienteByID("5")
# UpdatePacienteByID("6", "nombre_paciente", "David")



