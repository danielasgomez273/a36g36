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




