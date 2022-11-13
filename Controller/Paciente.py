import importlib.util        
spec = importlib.util.spec_from_file_location(
  "PacienteConexionSqlite3", "Model\PacienteConexionSqlite3.py")    
ConexionBDpaciente = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(ConexionBDpaciente)

class Paciente():
    def __init__(self, nombre, apellido, telefono, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.contraseña = contraseña
        self.ID = ConexionBDpaciente.CreatePaciente(nombre, apellido, telefono, email, contraseña)     
       
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

    def deletePaciente(self):
        ConexionBDpaciente.DeletePacienteByID(id)

pacientePrueba =  Paciente('david','costa','2644641117572','daa91@gmail.com','liuadbva1223')
pacientePrueba2 =  Paciente('david','costa','2644641117572','dsa91@gmail.com','liuadbva1223')
pacientePrueba3 =  Paciente('david','costa','2644641117572','da9d1@gmail.com','liuadbva1223')
print("imprimiendo get_ID", pacientePrueba.get_ID())
print("imprimiendo get_ID", pacientePrueba2.get_ID())
print("imprimiendo get_ID", pacientePrueba3.get_ID())
