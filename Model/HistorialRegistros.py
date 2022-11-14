import sqlite3

class HistorialRegistros():
    def __init__(self):
        pass

    def ReadRegistrosByIdUsuario(ID):
        conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
        cursor = conexionSqlite3.cursor()
        sentenciaSql= "SELECT * FROM registros_glucemia WHERE registros_glucemia.idpacienteFK ="+ ID + ";"
        try:
            cursor.execute(sentenciaSql)
            lecturaBD = cursor.fetchall()
            print("Lectura desde bd Read=> ",lecturaBD)
        except:
            print("Ocurrio un error al leer datos de BD")
        finally:
            conexionSqlite3.close()


    def ReadAllRegistros():
        conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
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
        conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
        cursor = conexionSqlite3.cursor()
        sentenciaSql= "UPDATE registros_glucemia SET " + campo + " = '" + valor +"' WHERE registros_glucemia.idregistros_glucemia="+ID
        print(sentenciaSql)
        try:
            cursor.execute(sentenciaSql)
            print("Update en BD de pte con ID",ID, "Se actualizo ", campo, "al valor ", valor)
            conexionSqlite3.commit()
        except:
            print("Ocurrio un error al leer datos de BD")
        finally:
            conexionSqlite3.close()


    def DeleteRegistroByID(ID):
        conexionSqlite3 = sqlite3.connect("nuevaPruebaDB.db")
        cursor = conexionSqlite3.cursor()
        sentenciaSql= "DELETE FROM registros_glucemia WHERE registros_glucemia.idregistros_glucemia ="+ ID + ";"
        try:
            cursor.execute(sentenciaSql)
            print("Borrado de bd REGISTRO con id=",ID)
            conexionSqlite3.commit()
        except:
            print("Ocurrio un error al leer datos de BD")
        finally:
            conexionSqlite3.close()