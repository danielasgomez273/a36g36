import importlib.util        
spec = importlib.util.spec_from_file_location(
  "InicializacionBD", "Model\InicializacionBD.py")    
InicializacionBD = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(InicializacionBD)




spec = importlib.util.spec_from_file_location(
  "PacienteConexionSqlite3", "Model\PacienteConexionSqlite3.py")    
PacienteConexionSqlite3 = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(PacienteConexionSqlite3)

spec = importlib.util.spec_from_file_location(
  "RegistroConexionSqlite3", "Model\RegistroConexionSqlite3.py")    
RegistroConexionSqlite3 = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(RegistroConexionSqlite3)

spec = importlib.util.spec_from_file_location(
  "PrestadorConexionSqlite3", "Model\PrestadorConexionSqlite3.py")    
PrestadorConexionSqlite3 = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(PrestadorConexionSqlite3)

from Registro import Registro
from Paciente import Paciente
from Prestador import Prestador

def agregarPacientes():
    pacientePrueba =  Paciente('davvid','cosbFta',154647572,'david@gmail.com','0')
    pacientePrueba1 = Paciente('david','costa',1546475721,'david@gmail.com2','1')
    pacientePrueba2 = Paciente('david','costa',1546475722,'david@gmail.com3','2')
    pacientePrueba3 = Paciente('davvid','cosbFta',1546475723,'david@gmail.com4','3')
    pacientePrueba4 = Paciente('david','costa',1546475724,'david@gmail.com5','4')
    pacientePrueba5 = Paciente('david','costa',1546475725,'david@gmail.com6','5')
    pacientePrueba6 = Paciente('davvid','cosbFta',1546475726,'7david@gmail.com','6')
    pacientePrueba7 = Paciente('david','costa',1546475727,'8david@gmail.com','7')
    pacientePrueba8 = Paciente('david','costa',1546475728,'david@gmail.com9','8')
    pacientePrueba9 =  Paciente('davvid','cosbFta',1546475729,'david@gmail.com10','9')
    pacientePrueba10 = Paciente('david','costa',15464757210,'david@gmail.com11','10')
    pacientePrueba11 = Paciente('david','costa',15464757211,'david@gmail.com12','11')
    pacientePrueba12 = Paciente('davvid','cosbFta',15464757212,'david@gmail.com13','12')
    pacientePrueba13 = Paciente('david','costa',15464757213,'david@gmail.com14','13')
    pacientePrueba14 = Paciente('davvid','cosbFta',15464757214,'david@gmail.com15','14')

def agregarPrestadores():
    prestadorPrueba1 = Prestador('presta@gmail.com','1',1546475721,'hola soy un presador... estsa ')
    prestadorPrueba2 = Prestador('presta@gmail.com2','2',1546475722,'hola soy un presador... estsa ')
    prestadorPrueba3 = Prestador('presta@gmail.com3','3',1546475723,'hola soy un presador... estsa ')
    prestadorPrueba4 = Prestador('presta@gmail.com4','4',1546475724,'hola soy un presador... estsa ')
    prestadorPrueba5 = Prestador('presta@gmail.com5','5',1546475725,'hola soy un presador... estsa ')
    
def agregarRegistros():
    r1 = Registro("10/11/22 11:00:00", 0.3, "1 registro", 1)
    r2 = Registro("11/11/22 11:00:00", 0.3, "2 registro", 1)
    r3 = Registro("12/11/22 11:00:00", 0.3, "3 registro", 1)
    r4 = Registro("13/11/22 11:00:00", 0.3, "f registro", 1)
    r5 = Registro("14/10/21 11:00:00", 0.3, "4 registro", 1)
    r6 = Registro("15/10/22 11:00:00", 0.3, "2 registro", 1)
    r7 = Registro("17/01/22 11:00:00", 0.3, "11 registro", 2)
    r8 = Registro("19/03/22 11:00:00", 0.3, "22 registro", 2)
    r9 = Registro("21/07/22 11:00:00", 0.3, "33 registro", 2)
    r10 = Registro("23/09/22 11:00:00", 0.3, "44 registro", 2)
    r11 = Registro("22/01/22 11:00:00", 0.3, "55 registro", 3)
    r12 = Registro("05/08/22 11:00:00", 0.3, "5 registro", 3)
    r13 = Registro("07/04/22 11:00:00", 0.3, "6 registro", 3)
    r14 = Registro("14/09/22 11:00:00", 0.3, "8 registro", 3)
    r15 = Registro("14/10/22 11:00:00", 0.3, "po  registro", 1)

def agregarTodos():
    agregarPacientes()
    agregarPrestadores()
    agregarRegistros()

# Ingreso de datos
# agregarTodos()
# Consultas de prueba

# Consultas de prueba PACIENTE
# print("El id del prestador es => ",PacienteConexionSqlite3.getIdPacienteByEmail("david@gmail.com"))
# PacienteConexionSqlite3.ReadPacienteByID(2)
# PacienteConexionSqlite3.ReadAllPacientes()
# PacienteConexionSqlite3.UpdatePacienteByID(4,"nombre_paciente", "Edgardo")
# PacienteConexionSqlite3.DeletePacienteByID(2)

# Consultas de prueba REGISTROS
# RegistroConexionSqlite3.ReadAllRegistros()
# RegistroConexionSqlite3.DeleteRegistroByID(40)
# RegistroConexionSqlite3.UpdateRegistroByID(1,"valor_glucemia",9)

# Consultas de prueba PRESTADOR
# print("El id del prestador es => ",PrestadorConexionSqlite3.getIdPrestadorByEmail("presta@gmail.com4"))
# PrestadorConexionSqlite3.ReadPrestadorByID(4)
# PrestadorConexionSqlite3.ReadAllPrestadores()
# PrestadorConexionSqlite3.UpdatePrestadorByID(3,"email_prestador", "davidcst2991@gmail.com")
# PrestadorConexionSqlite3.DeletePrestadorByID(2)

