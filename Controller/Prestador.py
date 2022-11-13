import importlib.util        
spec = importlib.util.spec_from_file_location(
  "PrestadorConexionSqlite3", "Model\PrestadorConexionSqlite3.py")    
ConexionBDprestador = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(ConexionBDprestador)

class Prestador():
    def __init__(self,email, contraseña, telefono, informacionExtra):
        self.email = email
        self.contraseña = contraseña
        self.telefono = telefono
        self.informacionExtra = informacionExtra        
        self.ID = ConexionBDprestador.CreatePrestador(email, contraseña, telefono, informacionExtra)     
       
    def get_ID(self):
        return self.ID
    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_telefono(self):
        return self.telefono
    def get_email(self):
        return self.email
    def get_contraseña(self):
        return self.contraseña
   
    #  def updatePaciente(self,campo, valor):
     #   ConexionBDpaciente.UpdatePacienteByID(self.get_ID, campo, valor)
      
    
    def set_nombre(self, nombre,campo, valor):     
        self.nombre = nombre
     #   updatePaciente(self,"nombre_paciente", valor)

    def set_apellido(self,apellido):
        self.apellido = apellido
    def set_telefono(self,telefono):
        self.telefono = telefono
    def set_contraseña(self, contraseña):
        self.contraseña = contraseña

    # FUNCIONES A DESARROLLAR..

    def deletePrestador(self):
        ConexionBDprestador.DeletePrestadorByID(id)

prestadorPrueba =  Prestador('dqaa91@gmail.com','liuadbava1223','26446411572','hola soy un presador... estsa ')
prestadorPrueba2 =  Prestador('daaa91@gmail.com','liuaasdbva1223','264464111772','hola soy un presador... estsa ')
prestadorPrueba3 =  Prestador('ddaa91@gmail.com','liuaddbva1223','26446117572','hola soy un presador... estsa ')
prestadorPrueba4 =  Prestador('dafa91@gmail.com','liuhadbva1223','241117572','hola soy un presador... estsa ')

print("imprimiendo get_ID", prestadorPrueba.get_ID())
print("imprimiendo get_ID", prestadorPrueba2.get_ID())
print("imprimiendo get_ID", prestadorPrueba3.get_ID())



