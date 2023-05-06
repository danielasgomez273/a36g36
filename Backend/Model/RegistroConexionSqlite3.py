import sqlite3

def CreateRegistro(fecha_registro,hora_registro, valor_glucemia, comentario_registro, id_paciente_fK):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("INSERT INTO registro_glucemia (fecha_registro,hora_registro, valor_glucemia, comentario_registro, id_paciente_fK) VALUES (?, ?, ?, ?, ?)",
        (fecha_registro,hora_registro, valor_glucemia, comentario_registro, id_paciente_fK))

        conexionSqlite3.commit()
        IDDesdeBD = cursor.lastrowid
        print("Guarde registro en BD")    
    except:
        print("Ocurrio un error al guardar datos en BD")
    finally:
        conexionSqlite3.close()
    return IDDesdeBD

def ReadRegistrosByIdUsuario(id_paciente_fK):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("SELECT * FROM registro_glucemia WHERE registro_glucemia.id_paciente_fK = ?",(str(id_paciente_fK),))
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd Read=> ",lecturaBD)
    except Exception as e:
        print("Ocurrio un error al leer datos de BD", e)
    finally:
        conexionSqlite3.close()

def ReadAllRegistros():
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "SELECT * FROM registro_glucemia;"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd ReadAllRegistros=> ",lecturaBD)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()

def UpdateRegistroByID(id_registro_glucemia,campo, valor):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("UPDATE registro_glucemia SET "+campo+" =? WHERE registro_glucemia.id_registro_glucemia= ?", (valor, str(id_registro_glucemia)))
        print("Update en BD registro glucemia, con id_registro_glucemia",id_registro_glucemia, "Se actualizo ", campo, "al valor ", valor)
        conexionSqlite3.commit()
    except Exception as e:
        print("Ocurrio un error al actualizar datos de BD",e)
    finally:
        conexionSqlite3.close()

def DeleteRegistroByID(id_registro_glucemia):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("DELETE FROM registro_glucemia WHERE registro_glucemia.id_registro_glucemia =?",(str(id_registro_glucemia),)) #COMA NECESARIA PARA QUE SEA UNA TUPLA EN VALORES MAYORES A 9!      
        print("Borrado de bd REGISTRO con id_registro_glucemia ",id_registro_glucemia)
        conexionSqlite3.commit()
    except Exception as e:
        print("Ocurrio un error al BORRAR datos de BD", e)
    finally:
        conexionSqlite3.close()