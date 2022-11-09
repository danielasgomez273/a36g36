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
        self.ID = None 
        ConexionBDpaciente.CreatePaciente(nombre, apellido, telefono, email, contraseña)     
       
    def get_ID(self):
        self.ID = ConexionBDpaciente.getIdPacienteByEmail(self.email)
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
        # Atributos a sumar??..
    
    # FUNCIONES A DESARROLLAR..

    def DeletePaciente(self):
        id = self.get_ID(self)
        ConexionBDpaciente.DeletePacienteByID(id)

pacientePrueba =  Paciente('david','costa','2644641117572','da91@gmail.com','liuadbva1223')
pacientePrueba2 =  Paciente('david','costa','2644641117572','da91@gmail.com','liuadbva1223')
pacientePrueba3 =  Paciente('david','costa','2644641117572','da91@gmail.com','liuadbva1223')
print("imprimiendo get_ID", pacientePrueba.get_ID())
print("imprimiendo get_ID", pacientePrueba2.get_ID())
print("imprimiendo get_ID", pacientePrueba3.get_ID())
