/*  INGRESO DATOS  */
-- Primero creemos un nuevo prestador
INSERT INTO prestador (email,nombrePrestador,apellidoPrestador,contraseña,telefono,informacionExtra)
VALUES
("prestador01@gmail.com","enrique","baltazar","1234","12345678","datos enrique"),
("carlos02@gmail.com","melisa","alba","5678","15427583","datos melisa"),
("anaa03@gmail.com","gustavo","mitto","1276","174836298","datos gustavo");
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

/* INSERT DATOS */
INSERT INTO paciente (nombre_paciente, apellido_paciente, telefono_paciente, email_paciente, contraseña_paciente) VALUES 
("David1", "Costa", 26441, "1davidcst2991@gmail.com", "A123123"),
("David2", "Costa", 26442, "2davidcst2991@gmail.com", "S12A3123"),
("David3", "Costa", 26443, "3davidcst2991@gmail.com", "12S3123"),
("David3", "Costa", 26444, "4davidcst2991@gmail.com", "12V3123"),
("David5", "Costa", 26445, "5davidcst2991@gmail.com", "DD123123"),
("David6", "Costa", 26446, "6davidcst2991@gmail.com", "AAAA123123"),
("David7", "Costa", 26447, "7davidcst2991@gmail.com", "SSSS123123"),
("David8", "Costa", 26448, "8davidcst2991@gmail.com", "DD12312A3");
SELECT * FROM `zzz`.paciente;

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

/* carrito borrar idUusarioFk (hecho), unificar fecha y hora a datetime(hecho), borrar campo usuario.. PASAR TODO A CAMEL CASE */

/* AGREGAR CARRITOS, AGREGAR FACTURAS Y HACER CONSULTAS! !!  */
