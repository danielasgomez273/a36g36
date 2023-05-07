import sqlite3

def CreatePaciente(nombre_paciente, apellido_paciente, email_paciente, contraseña_paciente , fecha_nacimiento , sexo ,telefono_paciente):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("INSERT INTO paciente (nombre_paciente, apellido_paciente, email_paciente, contraseña_paciente , fecha_nacimiento , sexo ,telefono_paciente) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (nombre_paciente, apellido_paciente, email_paciente, contraseña_paciente , fecha_nacimiento , sexo ,telefono_paciente))

        conexionSqlite3.commit()
        IDDesdeBD = cursor.lastrowid
        print("Guarde PACIENTE en DB")    
    except Exception as e:
        print("Ocurrio un error al guardar datos en BD", e)
    finally:
        conexionSqlite3.close()
    return IDDesdeBD

def getIdPacienteByEmail(email_paciente):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("SELECT id_paciente FROM paciente WHERE paciente.email_paciente = ?",(email_paciente,))
        lecturaBD = cursor.fetchall()
        resultados=lecturaBD
    except Exception as e:
        print("Ocurrio un error al leer datos de BD", e)
    finally:
        conexionSqlite3.close()
    return resultados[0][0]

def ReadPacienteByID(id_paciente):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("SELECT * FROM paciente WHERE paciente.id_paciente = ?", (str(id_paciente),))
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd ReadPacienteByID=> ",lecturaBD)
    except Exception as e:
        print("Ocurrio un error al leer datos de BD",e)
    finally:
        conexionSqlite3.close()

def ReadAllPacientes():
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("SELECT * FROM paciente")
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd ReadAllPacientes=> ",lecturaBD)
    except Exception as e:
        print("Ocurrio un error al leer datos de BD", e)
    finally:
        conexionSqlite3.close()

def UpdatePacienteByID(id_paciente,campo, valor):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("UPDATE paciente SET "+campo+" =? WHERE paciente.id_paciente= ?", (valor, str(id_paciente)))
        print("Update en BD de pte con id_paciente",id_paciente, "Se actualizo ", campo, "al valor ", valor)
        conexionSqlite3.commit()
    except Exception as e:
        print("Ocurrio un error al leer datos de BD", e)
    finally:
        conexionSqlite3.close()

def DeletePacienteByID(id_paciente):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("DELETE FROM paciente WHERE paciente.id_paciente= ?", (str(id_paciente),))
        print("Borrado de bd PTE con id_paciente=",id_paciente)
        conexionSqlite3.commit()
    except Exception as e:
        print("Ocurrio un error al leer datos de BD",e)
    finally:
        conexionSqlite3.close()


