import mysql.connector

class PacienteConexion:
    def __init__(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                                         host='127.0.0.1',
                                         port=3306,
                                         database='zzz',
                                         user='root',
                                         password='154647572')

        except mysql.connector.Error as error:
            print("Error de conexion", error)

    def CrearTablaPaciente(self):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sentenciaSql = ''' CREATE TABLE IF NOT EXISTS `paciente` (
                                `idpaciente` int AUTO_INCREMENT,
                                `nombre_paciente` varchar(45) NOT NULL,
                                `apellido_paciente` varchar(45) NOT NULL,
                                `telefono_paciente` varchar(45) NOT NULL UNIQUE,
                                `email_paciente` varchar(45) NOT NULL UNIQUE,
                                `contraseña_paciente` varchar(45) NOT NULL UNIQUE,
                                PRIMARY KEY (`idpaciente`)
                                ); '''
                                                
                cursor.execute(sentenciaSql)
                #self.connection.commit()
                #sentenciaSql = "INSERT INTO paciente (nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente)"
                #datosUsuario =(nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente)
                # cursor.execute(sentenciaSql, datosUsuario)

            except:
                print("Ocurrio un error de conexion")

    def RegistroNuevoUsuario(self): #(nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente)
        nombre_paciente = "david"
        apellido_paciente = "costa"
        telefono_paciente = "2644641117572"
        email_paciente = "da91@gmail.com"
        contraseña_paciente ="1aa1223"

        datosUsuario = nombre_paciente + apellido_paciente + telefono_paciente + email_paciente + contraseña_paciente


        if self.connection.is_connected():
            try:
              #   self.CrearTablaPaciente()  #crea tabla si no existe...
                cursor = self.connection.cursor()
                sentenciaSql = '''INSERT INTO paciente ("nombre_paciente", "apellido_paciente", "telefono_paciente", "email_paciente", "contraseña_paciente") 
                VALUES (''' + datosUsuario + ");"



                cursor.execute(sentenciaSql)
                self.connection.commit()
                #sentenciaSql = "INSERT INTO paciente (nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente)"
                #datosUsuario =(nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente)
                # cursor.execute(sentenciaSql, datosUsuario)

            except:
                print("Ocurrio un error de conexion")


#llamar a creacion de paciente
nuevoUsuario= PacienteConexion()
nuevoUsuario.CrearTablaPaciente()
#print(PacienteConexion.__dict__)
#nuevoUsuario.RegistroNuevoUsuario()