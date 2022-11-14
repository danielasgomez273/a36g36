import importlib.util        
spec = importlib.util.spec_from_file_location(
  "InicializacionBD", "Model\InicializacionBD.py")    
InicializacionBD = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(InicializacionBD)

spec = importlib.util.spec_from_file_location(
  "HistorialRegistros", "Model\HistorialRegistros.py")    
HistorialRegistros = importlib.util.module_from_spec(spec)        
spec.loader.exec_module(HistorialRegistros)

from Registro import Registro
from Paciente import Paciente
from Prestador import Prestador

try:
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
except Exception as e:
    print("Error creando PACIENTES => ",e)

try:
    prestadorPrueba1 = Prestador('presta@gmail.com','1',1546475721,'hola soy un presador... estsa ')
    prestadorPrueba2 = Prestador('presta@gmail.com2','2',1546475722,'hola soy un presador... estsa ')
    prestadorPrueba3 = Prestador('presta@gmail.com3','3',1546475723,'hola soy un presador... estsa ')
    prestadorPrueba4 = Prestador('presta@gmail.com4','4',1546475724,'hola soy un presador... estsa ')
    prestadorPrueba5 = Prestador('presta@gmail.com5','5',1546475725,'hola soy un presador... estsa ')
except Exception as e:
    print("Error creando PRESTADORES => ",e)

try:
    r1 = Registro("14/11/22", 0.3, "primer registro", 1)
    r2 = Registro("14/11/22", 0.3, "primer registro", 1)
    r3 = Registro("14/11/22", 0.3, "primer registro", 1)
    r4 = Registro("14/11/22", 0.3, "primer registro", 1)
    r5 = Registro("14/11/22", 0.3, "primer registro", 1)
    r6 = Registro("14/11/22", 0.3, "primer registro", 1)
    r7 = Registro("14/11/22", 0.3, "primer registro", 2)
    r8 = Registro("14/11/22", 0.3, "primer registro", 2)
    r9 = Registro("14/11/22", 0.3, "primer registro", 2)
    r10 = Registro("14/11/22", 0.3, "primer registro", 2)
    r11 = Registro("14/11/22", 0.3, "primer registro", 3)
    r12 = Registro("14/11/22", 0.3, "primer registro", 3)
    r13 = Registro("14/11/22", 0.3, "primer registro", 3)
    r14 = Registro("14/11/22", 0.3, "primer registro", 3)
    r15 = Registro("14/11/22", 0.3, "primer registro", 1)
except Exception as e:
    print("Error creando REGISTROS DE GLUCEMIA => ",e)


HistorialRegistros.DeleteRegistroByID(13)