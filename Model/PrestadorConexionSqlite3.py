import sqlite3

def CreatePrestador(email_prestador, contraseña_prestador, telefono_prestador,informacionExtra_prestador):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("INSERT INTO prestador (email_prestador, contraseña_prestador, telefono_prestador, informacionExtra_prestador) VALUES (?, ?, ?, ?)",
        (email_prestador, contraseña_prestador, telefono_prestador, informacionExtra_prestador))

        conexionSqlite3.commit()
        IDDesdeBD = cursor.lastrowid
        print("Guarde PRESTADOR en BD ")    
    except Exception as e:
        print("Ocurrio un error al guardar datos en BD", e)
    finally:
        conexionSqlite3.close()
    return IDDesdeBD

def getIdPrestadorByEmail(email_prestador):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("SELECT idPrestador FROM prestador WHERE prestador.email_prestador = ?", (email_prestador,))
        lecturaBD = cursor.fetchall()
        resultados=lecturaBD
        print("ID leido desde bd getIdPrestadorByEmail=> ",lecturaBD, "corresponde a email", email_prestador)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()
    return resultados[0][0]


def ReadPrestadorByID(ID):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("SELECT * FROM prestador WHERE prestador.idPrestador = ?", (str(ID),))
        lecturaBD = cursor.fetchall()
        print("Lectura desde ReadPrestadorByID=> ",lecturaBD)
    except Exception as e:
        print("Ocurrio un error al leer datos de BD", e)
    finally:
        conexionSqlite3.close()

def ReadAllPrestadores():
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("SELECT * FROM prestador")
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd ReadAllPrestadores=> ",lecturaBD)
    except Exception as e:
        print("Ocurrio un error al leer datos de BD", e)
    finally:
        conexionSqlite3.close()

def UpdatePrestadorByID(ID,campo, valor):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("UPDATE prestador SET "+campo+" =? WHERE prestador.idPrestador= ?", (valor, str(ID)))
        print("Update en BD de pte con ID",ID, "Se actualizo ", campo, "al valor ", valor)
        conexionSqlite3.commit()
    except Exception as e:
        print("Ocurrio un error al leer datos de BD", e)
    finally:
        conexionSqlite3.close()

def DeletePrestadorByID(ID):
    conexionSqlite3 = sqlite3.connect("OneDropBD.db")
    cursor = conexionSqlite3.cursor()
    try:
        cursor.execute("DELETE FROM prestador WHERE prestador.idPrestador = ?", (str(ID),))
        print("Borrado de PRESTADOR con id=",ID)
        conexionSqlite3.commit()
    except Exception as e:
        print("Ocurrio un error al BORRAR PRESTADOR de BD", e)
    finally:
        conexionSqlite3.close()
