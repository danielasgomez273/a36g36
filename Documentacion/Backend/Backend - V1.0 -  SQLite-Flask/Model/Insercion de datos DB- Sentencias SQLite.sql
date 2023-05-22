
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
INSERT INTO prestador (email_prestador,contraseña_prestador,telefono_prestador,informacion_extra_prestador)
VALUES
('presta@gmail.com','1',1546475721,'hola soy un presador... estsa '),
('presta@gmail.com2','2',1546475722,'hola soy un presador... estsa '),
('presta@gmail.com3','3',1546475723,'hola soy un presador... estsa ');
SELECT * FROM prestador;
 
-- Creamos servicios y lo relacionamos con prestadores
INSERT INTO servicio (nombre_servicio,descripcion_servicio,sede_servicio,precio_servicio,comentarios_servicio,duracion_servicio,id_prestador_fk)    
VALUES
('Analisis Clinico Sangre','Analisis de glucosa en sangre','Colon 1500 CBA',1000,'sin comentarios aun', '00:45:00',1),
('Consulta Nutricionista (Dra Allende)','Consulta con Dra Allende','Colon 1500 CBA',1200,'sin comentarios aun', '00:45:00',2),
('Analisis Clinico Completo','Analisis de sangre completo','Colon 1500 CBA',1000,'sin comentarios aun', '00:45:00',3),
('Consulta Diabetologo (DrPerez) ','Consulta con Dr Perez','Colon 1500 CBA',1200,'sin comentarios aun', '00:45:00',1),
('Analisis Clinico T4L','Analisis de glucosa en sangre, T4libre','Colon 1500 CBA',1000,'sin comentarios aun', '00:45:00',3);
SELECT * FROM servicio;

/* MUESTRA SERVICIOS DE UN PRESTADOR  */
SELECT * FROM servicio INNER JOIN prestador ON servicio.id_prestador_fk = prestador.id_prestador
WHERE prestador.id_prestador =3;


-- Creamos pacientes
INSERT INTO paciente (nombre_paciente, apellido_paciente, email_paciente, contraseña_paciente , fecha_nacimiento , sexo ,telefono_paciente) VALUES 
('davvid','cosbFta','david@hotmail.com1', 'miPassword1', '01/05/1992', 'masculino', 1546417572),
('david','costa','david@hotmail.com2', 'miPassword2', '01/05/1992', 'masculino', 154647157221),
('david','costa','david@hotmail.com3', 'miPassword3', '01/05/1992', 'masculino', 154641754722),
('davvid','cosbFta','david@hotmail.com4', 'miPassword4', '01/05/1992', 'masculino', 151463475723),
('david','costa','david@hotmail.com5', 'miPassword5', '01/05/1992', 'masculino', 154614175724),
('david','costa','david@hotmail.com6', 'miPassword6', '01/05/1992', 'masculino', 154614475725),
('davvid','cosbFta','david@hotmail.com7', 'miPassword7', '01/05/1992', 'masculino', 15464755726),
('davvid','cosbFta','david@hotmail.com8', 'miPassword8', '01/05/1992', 'masculino', 15464725726);
SELECT * FROM paciente;

-- Creamos fichas medicas y las relacionamos con pacientes
INSERT INTO ficha_medica (tipo_diabetes, terapia_insulina, terapia_pastillas, tipo_glucometro, tipo_sensor, comorbilidades, objetivo_glucosa, id_paciente_fK) VALUES 
('1', 'tarapia_insu', 'terapia_past', 'tipo_gluoc', 'tipo_sensor', 'comorb', 'obj_gluco',1),
('2', 'tarapia_insu', 'terapia_past', 'tipo_gluoc', 'tipo_sensor', 'comorb', 'obj_gluco',2),
('1', 'tarapia_insu', 'terapia_past', 'tipo_gluoc', 'tipo_sensor', 'comorb', 'obj_gluco',3),
('1', 'tarapia_insu', 'terapia_past', 'tipo_gluoc', 'tipo_sensor', 'comorb', 'obj_gluco',4),
('2', 'tarapia_insu', 'terapia_past', 'tipo_gluoc', 'tipo_sensor', 'comorb', 'obj_gluco',5),
('1', 'tarapia_insu', 'terapia_past', 'tipo_gluoc', 'tipo_sensor', 'comorb', 'obj_gluco',6),
('2', 'tarapia_insu', 'terapia_past', 'tipo_gluoc', 'tipo_sensor', 'comorb', 'obj_gluco',7),
('1', 'tarapia_insu', 'terapia_past', 'tipo_gluoc', 'tipo_sensor', 'comorb', 'obj_gluco',8);
SELECT * FROM ficha_medica;

-- Creamos registros de glucemia y las relacionamos con pacientes
INSERT INTO registro_glucemia (fecha_registro,hora_registro, valor_glucemia, comentario_registro, id_paciente_fK) VALUES
('2022-10-01', '10:00:00', 0.19, 'primera medicion', 1),
('2022-10-02', '11:00:00', 0.29, 'a medicion', 1),
('2022-11-03', '12:00:00', 0.39, 'asc medicion', 1),
('2022-02-04', '13:00:00', 0.49, 'ASD medicion', 2),
('2021-03-05', '14:00:00', 0.59, 'AS medicion', 4),
('2021-04-05', '15:00:00', 0.19, 'pridxamera medicion', 6),
('2021-05-06', '15:00:00', 0.29, 'priadvmera medicion', 1),
('2020-06-06', '12:00:00', 0.39, 'da medicion', 2),
('2020-06-04', '02:00:00', 0.49, 'vd medicion', 5),
('2020-07-02', '17:00:00', 0.59, 'e medicion', 1);
SELECT * FROM registro_glucemia;

/* MUESTRA REGISTROS DE GLUCEMIA DE UN PTE  */
SELECT * FROM paciente 
INNER JOIN registro_glucemia ON paciente.id_paciente = registro_glucemia.id_paciente_fk
WHERE paciente.id_paciente = 1;


-- Creamos carritos y lo relacionamos con pacientes
INSERT INTO carrito (id_paciente_fk , estado_carrito) VALUES
(1 , 'pago pendiente'),
(2 , 'pago pendiente'),
(3 , 'pago pendiente');
SELECT * FROM carrito;


-- Creamos FACTURA y lo relacionamos a carritos
INSERT INTO factura (id_carrito_fk , fecha_completa_factura , concepto_factura, valor_factura , medio_pago_factura , estado_pago) VALUES
(1 , '2021-03-06 17:24:57', 'pago carrito', 1253 , 'contado efectivo', 'aprobado'),
(2 , '2021-03-06 17:24:57', 'pago carrito', 12243 , 'tarjeta credito', 'aprobado'),
(3 , '2021-03-06 17:24:57', 'pago carrito', 125323 , 'transferencia', 'aprobado');

/* MUESTRA LAS FACTURAS DE PAGO RELACIONADAS A CARRTI  */
SELECT * FROM factura
INNER JOIN carrito ON factura.id_carrito_fk = carrito.id_carrito
WHERE factura.id_carrito_fk = 1;



-- Creamos paquetes
INSERT INTO paquete (duracion_total , precio_total , sede_paquete , fecha_seleccionada) VALUES
('00:30::00' , 7500 , 'caba' , '06/05/2023 10:00'),
('00:30::00' , 7500 , 'caba' , '06/05/2023 10:00'),
('00:30::00' , 7500 , 'caba' , '06/05/2023 10:00');
SELECT * FROM paquete

-- Creamos tabla union PAQUETE - SERVICIO
INSERT INTO paquete_servicio (id_paquete_fk , id_servicio_fk ) VALUES
(1 , 1),
(1 , 2),
(2 , 1);
SELECT * FROM paquete_servicio

-- Creamos tabla union CARRITO - PAQUETE
INSERT INTO carrito_paquete (id_carrito_fk , id_paquete_fk ) VALUES
(1 , 1),
(1 , 2),
(2 , 1);
SELECT * FROM carrito_paquete