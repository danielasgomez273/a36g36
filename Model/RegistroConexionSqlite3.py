import sqlite3

def CreateRegistro(fecha_registro, valor_glucemia, comentario_registro,idpacienteFK):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("INSERT INTO registros_glucemia (fecha_registro, valor_glucemia, comentario_registro, idpacienteFK) VALUES (?, ?, ?, ?)",
        (fecha_registro, valor_glucemia, comentario_registro, idpacienteFK))

        conexionSqlite3.commit()
        IDDesdeBD = cursor.lastrowid
        print("Guarde registro en BD")    
    except:
        print("Ocurrio un error al guardar datos en BD")
    finally:
        conexionSqlite3.close()
    return IDDesdeBD

def ReadRegistrosByIdUsuario(ID):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("SELECT * FROM registros_glucemia WHERE registros_glucemia.idpacienteFK = ?",(str(ID),))
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd Read=> ",lecturaBD)
    except Exception as e:
        print("Ocurrio un error al leer datos de BD", e)
    finally:
        conexionSqlite3.close()

def ReadAllRegistros():
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "SELECT * FROM registros_glucemia;"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd ReadAllRegistros=> ",lecturaBD)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()

def UpdateRegistroByID(ID,campo, valor):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("UPDATE registros_glucemia SET "+campo+" =? WHERE registros_glucemia.idregistros_glucemia= ?", (valor, str(ID)))
        print("Update en BD de pte con ID",ID, "Se actualizo ", campo, "al valor ", valor)
        conexionSqlite3.commit()
    except Exception as e:
        print("Ocurrio un error al actualizar datos de BD",e)
    finally:
        conexionSqlite3.close()

def DeleteRegistroByID(ID):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("DELETE FROM registros_glucemia WHERE registros_glucemia.idregistros_glucemia =?",(str(ID),)) #COMA NECESARIA PARA QUE SEA UNA TUPLA EN VALORES MAYORES A 9!      
        print("Borrado de bd REGISTRO con id=",ID)
        conexionSqlite3.commit()
    except Exception as e:
        print("Ocurrio un error al BORRAR datos de BD", e)
    finally:
        conexionSqlite3.close()