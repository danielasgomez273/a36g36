
/*
********************************************************************************
NOTA: Dejamos este archivo, solo para mostrar algunas sentencias en lenguaje
Sql de manera anectotica, sin embargo, LA CREACION DE BD Y EL INGRESO DE DATOS
SE OBTIENE CORRIENDO EL ARCHIVO "main.py", DENTRO DE LA CARPETA "Controller".

DICHO ARCHIVO, SE ENCARGA DE INICIALIZAR LA BASE DE DATOS.
DE TODOS MODOS, SE DEJARA COMENTADO EL CODIGO PARA INICIAZAR
********************************************************************************
*/


/*  INGRESO DATOS  */
-- Primero creemos un nuevo prestador
INSERT INTO prestador (email,contraseña,telefono,informacionExtra)
VALUES
('presta@gmail.com','1',1546475721,'hola soy un presador... estsa '),
('presta@gmail.com2','2',1546475722,'hola soy un presador... estsa '),
('presta@gmail.com3','3',1546475723,'hola soy un presador... estsa ');
SELECT * FROM prestador;

INSERT INTO servicio (nombreServicio,descripcion,monto,sede,idPrestador)
VALUES
("Analisis Clinico GSangre","Analisis de glucosa en sangre",1000,"Colon 1500 CBA",1),
("Consulta Nutricionista (Dra Allende)","Consulta con Dra Allende",1200,"Colon 1500 CBA",2),
("Analisis Clinico Completo","Analisis de sangre completo",1000,"Colon 1500 CBA",3),
("Consulta Diabetologo (DrPerez) ","Consulta con Dr Perez",1200,"Colon 1500 CBA",1),
("Analisis Clinico T4L","Analisis de glucosa en sangre, T4libre",1000,"Colon 1500 CBA",3);
SELECT * FROM servicio;

/* MUESTRA SERVICIOS DE UN PRESTADOR  */
SELECT * FROM servicio INNER JOIN prestador ON servicio.idPrestador = prestador.idPrestador
WHERE prestador.idPrestador =3;


/* INSERT DATOS PACIENTES*/
INSERT INTO paciente (nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente) VALUES 
('davvid','cosbFta',154647572,'david@gmail.com','0'),
('david','costa',1546475721,'david@gmail.com2','1'),
('david','costa',1546475722,'david@gmail.com3','2'),
('davvid','cosbFta',1546475723,'david@gmail.com4','3'),
('david','costa',1546475724,'david@gmail.com5','4'),
('david','costa',1546475725,'david@gmail.com6','5'),
('davvid','cosbFta',1546475726,'7david@gmail.com','6'),
('davvid','cosbFta',1546475726,'7david@gmail.com','6');
SELECT * FROM paciente;

INSERT INTO ficha_medica (tipo_diabetes, terapia_insulina, terapia_pastillas, tipo_glucometro, tipo_sensor, comorbilidad, objetivo_glucosa, fecha_nacimiento, sexo, idpacienteFK) VALUES 
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 1),
(2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 2),
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 3),
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 4),
(2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 5),
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 6),
(2, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 7),
(1, "tarapia_insu", "terapia_past", "tipo_gluoc", "tipo_sensor", "comorb", "obj_gluco", "1992-12-02" , "masculino", 8);
SELECT * FROM ficha_medica;


INSERT INTO registros_glucemia (fecha_registro, valor_glucemia, comentario_registro, idpacienteFK) VALUES
("2022-10-01 10:00:00", 0.19, "primera medicion", 1),
("2022-10-02 11:00:00", 0.29, "a medicion", 1),
("2022-11-03 12:00:00", 0.39, "asc medicion", 1),
("2022-02-04 13:00:00", 0.49, "ASD medicion", 2),
("2021-03-05 14:00:00", 0.59, "AS medicion", 4),
("2021-04-05 15:00:00", 0.19, "pridxamera medicion", 6),
("2021-05-06 15:00:00", 0.29, "priadvmera medicion", 1),
("2020-06-06 12:00:00", 0.39, "da medicion", 2),
("2020-06-04 02:00:00", 0.49, "vd medicion", 5),
("2020-07-02 17:00:00", 0.59, "e medicion", 1);
SELECT * FROM registros_glucemia;

SELECT * FROM paciente 
INNER JOIN registros_glucemia ON paciente.idpaciente = registros_glucemia.idpacienteFK
WHERE paciente.idpaciente = 1;

INSERT INTO carrito (sede, fechaElegida, horaElegida, monto, idUsuarioFK, idServicioFK, idpacienteFK) VALUES
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1),
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1),
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1),
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1),
("SJ", "2020-07-02", "17:00:00", 150, 1,1,1);
SELECT * FROM carrito;

