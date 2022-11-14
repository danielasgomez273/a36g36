import sqlite3
import time

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
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    resultados=None
    sentenciaSql= "SELECT idPrestador FROM prestador WHERE prestador.email_prestador ='"+ email_prestador + "';"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        resultados=lecturaBD
        print("ID leido desde bd getIdPrestadorByEmail=> ",lecturaBD, "corresponde a email", email_prestador)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()
    return resultados


def ReadPrestadorByID(ID):
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "SELECT * FROM prestador WHERE prestador.idPrestador ="+ ID + ";"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd Read=> ",lecturaBD)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()

def ReadAllPrestadores():
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "SELECT * FROM prestador;"
    try:
        cursor.execute(sentenciaSql)
        lecturaBD = cursor.fetchall()
        print("Lectura desde bd ReadAll=> ",lecturaBD)
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()

def UpdatePrestadorByID(ID,campo, valor):
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "UPDATE prestador SET " + campo + " = '" + valor +"' WHERE prestador.idPrestador="+ID
    print(sentenciaSql)
    try:
        cursor.execute(sentenciaSql)
        print("Update en BD de pte con ID",ID, "Se actualizo ", campo, "al valor ", valor)
        conexionSqlite3.commit()
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()

def DeletePrestadorByID(ID):
    conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
    cursor = conexionSqlite3.cursor()
    sentenciaSql= "DELETE FROM prestador WHERE prestador.idPrestador ="+ ID + ";"
    try:
        cursor.execute(sentenciaSql)
        print("Borrado de bd PTE con id=",ID)
        conexionSqlite3.commit()
    except:
        print("Ocurrio un error al leer datos de BD")
    finally:
        conexionSqlite3.close()


# LLAMADO DE FUNCIONES DE CRUD 


# print("estoy retornando id PRESTAODR",getIdPrestadorByEmail('da91@gmail.com'))

# CreatePrestador()
# ReadPrestadorByID("3")
# ReadAllPrestadores()
# DeletePrestadorByID("5")
# UpdatePrestadorByID("6", "nombre_prestador", "David")



