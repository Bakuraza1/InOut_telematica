# Proyecto InOut


# 1. Introducción.

## Integrantes
Samuel David Villegas Bedoya
Julian Andres Ramirez Jimenez 
Julian Giraldo Perez

## 1.1 Propósito.
Este documento está dirigido a clientes potenciales, desarrolladores y en general personas que desean adquirir una mejor comprensión sobre lo que es el proyecto InOut. El principal objetivo es mostrar cuales son nuestros propósitos, metas y objetivos detrás de la creación de InOut, y además se adentrará de forma más profunda en los diferentes tipos de requerimientos que se consideran pertinentes para el correcto desarrollo del proyecto, todo con la finalidad de que el lector comprenda de forma íntegra de que se trata 
este proyecto.

## 1.2 Alcance.
La aplicación facilitará al usuario:
- La virtualización del inventario de una compañía.
- La posibilidad de realizar y ver comentarios sobre los diferentes productos

De forma general el software creado para este proyecto es una herramienta que permitirá a las empresas saber la opinión de sus usuarios sobre diferentes productos. De esta forma las compañías tendrán la capacidad de saber que opinan sus usuarios, y podrán crear estrategias que respondan a estas.

## 1.3 Visión general del producto.
### 1.3.1 Perspectiva del producto.
La idea para este proyecto nació al analizar que muchas veces a los super mercados minoristas o mayoristas pueden perder de vista la opinión del usuario, la cual resulta muchas veces vital para la toma de decisiones.

De ahí surgió nuestra idea, crear una plataforma web que ofrezca la capacidad de dejar comentarios sobre los diferentes productos de una compañia.
### 1.3.2 Funciones del producto.
La principal funcionalidad de nuestra plataforma web es la de dar a los dirigentes o empleados de los mercados anteriormente registrados, la capacidad de saber la opinión de diferentes usuarios sobre sus productos, a través de la implementación de un sistema de comentarios.

Algunas funcionalidades específicas de esta plataforma son:
- La capacidad de registrarse e iniciar sesión en la plataforma
- Poder registrar o eliminar productos
- La implementación de un sistema que permita visualizar comentarios
- La capacidad de crear un nuevo comentario

Mas adelante en la sección 3 se verá más a fondo diferentes requerimientos y funcionalidades con los que contará la plataforma.

### 1.3.3 Características de usuario.
En general esta plataforma va dirigida a todo tipo de tiendas, tanto mayoristas como minoristas, las cuales busquen tener un acercamiento a sus clientes.
### 1.3.4 Limitaciones.
En términos de software y hardware, los usuarios necesitaran de un dispositivo con capacidad de conexión a internet, preferiblemente un computador, y una cuenta registrada en la plataforma.

Por otro lado, en términos funcionales, principal limitación será la fiabilidad de los datos del inventario, dependerá de la calidad de estos datos que tan eficaces serán los análisis y las gráficas que se mostrarán.
# 1.4 Definiciones.


- Comentario: Juicio, opinión u observación personal que se hace o se expresa acerca de algo o alguien.

- Información: Información es el nombre por el que se conoce un conjunto organizado de datos procesados que constituyen un mensaje que cambia el estado de conocimiento del sujeto o sistema que recibe dicho mensaje.

- Plataforma web: Las plataformas web, son espacios en Internet que permiten la ejecución de diversas aplicaciones o programas en un mismo lugar para satisfacer distintas necesidades.

# 2. Referencias.
Referencias utilizadas para el entendimiento de los requerimientos y establecimiento de objetivos: 
- Ruiz, A. (2020, 9 julio). Big Data: Los efectos positivos de la analítica de datos en la empresa. Tecnología para los negocios. Recuperado de https://ticnegocios.camaravalencia.com/servicios/tendencias/los-efectos-positivos-de-la-analitica-de-datos-en-la-empresa/#:%7E:text=La%20anal%C3%ADtica%20de%20datos%20es,servicio%2C%20podremos%20ajustar%20la%20producci%C3%B3n.
- Tobar, A. R. (2022, 6 abril). Las herramientas digitales que hacen crecer a los almacenes de barrio. La Tercera. Recuperado de https://www.latercera.com/transformadores/noticia/las-herramientas-digitales-que-hacen-crecer-a-los-almacenes-de-barrio/BDYIB5TEIBHY3GFO4VEZFUJJJ4/
- Navarro, Y. (2022, 3 agosto). Ventajas de digitalizar tus inventarios de almacén. Kizeo Forms. Recuperado de https://www.kizeo-forms.com/es/ventajas-de-digitalizar-tus-inventarios-de-almacen/

Para realizar esta plantilla se usaron los elementos presentes en el estándar internacional ISO/IEC/IEEE 29148. 

# 3. Requerimientos específicos.
## 3.1 Interfaces externas.
Las principales interfaces externas son dos, y vienen dadas por dos interacciones que tendrá la aplicación, estas son: La interfaz de usuario (interacción con el usuario) y la conexión con la base de datos (interacción con la base de datos), en base a estas interacciones se han destacado varios puntos.

- (EI1) Interfaces de usuario: La aplicación podrá mostrar al usuario de forma cómoda la información disponible, y a su vez a través de la interfaz de usuario se podrá interactuar con la aplicación

- (EI2) Conectividad: El sistema debe estar comunicándose de forma óptima con la base de datos, y las búsquedas en la misma deben dar resultados coherentes. 

Cabe destacar que la aplicación no está pensada para interactuar con otras aplicaciones ya existentes.




## 3.2 Funciones.

- (RF1) El sistema debe permitir al usuario ingresar un nuevo producto
- (RF2) El sistema debe permitir al usuario eliminar un producto
- (RF3) El sistema debe permitir al usuario modificar el numero de productos disponibles
- (RF4) El sistema debe permitir al usuario guardar información como los productos y su cantidad en una base de datos
- (RF5) El sistema debe permitir al usuario visualizar los comentarios hechos en cierto producto.
- (RF6) El sistema debe permitir al usuario crear nuevos comentarios en ciertos productos.
- (RF7) Si el usuario no está registrado con una cuenta, el sistema debe permitir al usuario registrarse en la plataforma
- (RF8) Si el usuario posee una cuenta, el sistema debe permitir al usuario iniciar sesión en la plataforma
- (RF9) El sistema debe permitir al usuario visualizar los productos que se han registrado
- (RF10) El sistema debe permitir al usuario mostrar a través de la interfaz el número de productos disponibles  
- (RF12) El sistema debe permitir al usuario montar imágenes de sus productos para una mejor visualización
- (RF13) El sistema debe mostrar a través de la interfaz las imágenes de los productos

## 3.3 Requerimientos de usabilidad.

- (RU1) El Sistema debe actualizar el número de inventario en la interfaz cuando se hagan cambios
- (RU2) El Sistema debe actualizar los comentarios presentes en un productos cuando hayan cambios en los mismos 
- (RU3) El sistema debe tener una interfaz intuitiva para que el usuario pueda navegar a través de la plataforma de la forma más sencilla y optima posible.


## 3.4 Requerimientos de rendimiento.

- (RP1) El sistema debe mantener el correcto funcionamiento del inventario incluso con gran cantidad de productos
- (RP2) El proceso de inicio de sesión no debe tomar más de 10 segundos 
- (RP3) El proceso de registro no debe tomar más de 3 minutos
- (RP4) El sistema no debe consumir demasiados recursos de la maquina
- (RP5) El sistema debe cargar las gráficas de forma rápida y eficaz 

## 3.5 Requisitos lógicos de la base de datos.

- (RL1) La base de datos debe ser coherente y legible para una persona ajena al desarrollo
- (RL2) La base de datos debe responder correctamente a las búsquedas y sentencias
- (RL3) Cada persona o mercado debe tener una entrada en la base de datos, dentro de la cual se encuentre sus propios atributos.


## 3.6 Restricciones de diseño.

- (DC1) La plataforma debe ser "Genérica" esto con el ánimo de que cualquier tienda o supermercado lo pueda usar.
- (DC2) La disponibilidad de tiempo podría generar algunas restricciones en los campos que no resultan tan prioritarios.
- (DC3) Al tratarse de una plataforma web siempre se necesitará conexión a internet.

## 3.7 Atributos del sistema de software.

Él lo que respecta a los atributos del sistema de software se planea garantizar los siguientes puntos:

- (SA1) Mantenibilidad: En caso de necesitarse, los periodos de mantenimiento se deben hacer en horarios en los que no afecte a los usuarios, y además los mismos no deben afectar de ninguna forma lo que han registrado los usuarios.
- (SA2) Disponibilidad: La plataforma web debe estar disponible 24/7 para que el usuario siempre pueda llevar control de su inventario, a excepción, claro, de los periodos de mantenimiento.
- (SA3) Fiabilidad: El sistema debe funcionar correctamente en todo momento, y no arrojar errores o resultados que el usuario no espera.
- (SA4) Seguridad: Toda la información de las organizaciones debe ser privada y estar guardada de forma segura en la base de datos
- (SA5) Desempeño: El sistema no debe consumir demasiados recursos, y todos los procesos de búsqueda deben hacerse de forma rápida.

## 3.8 Información de apoyo.
- (SI1) Input/Output: En general el input será de tipo texto, en algunos casos se especificará si se debe ingresar un número.
- (SI2) El registro del usuario se hace a través de la misma plataforma, se pedirá un email, nombre del mercado y contraseña.
- (SI3) Algunos de los detalles en este documento pueden variar, esto al tratarse de un documento desarrollado en une etapa muy temprana.

# 4. Verificación.
## 4.1 Interfaces externas.

- (EI1) Interfaces de usuario: A lo largo del desarrollo se ira interactuando y probando la misma, además se pedirá a gente ajena al desarrollo que la pruebe, para así medir la calidad de la interfaz

- (EI2) Conectividad: A medida que se vaya desarrollando la base de datos se harán pruebas de estrés y de manejo de errores sobre la base de datos, para asegurar su estabilidad.

Cabe destacar que la aplicación no está pensada para interactuar con otras aplicaciones ya existentes.




## 4.2 Funciones.

- (RF1) Mediante un usuario de prueba se añadirá un nuevo producto, y se verificará que este se guarde.
- (RF2) Mediante un usuario de prueba se eliminará un producto, y se verificará que este se haya eliminado correctamente.
- (RF3) Mediante un usuario de prueba se modificará el inventario de ciertos productos, y se verificará que este cambio se guarde, y que la interfaz se actualice de acuerdo al cambio.
- (RF4) Se verificará que la información de los productos y su inventario se guarde en la basa de datos sin presentar perdidas de información.
- (RF5) Se verificara que los comentarios mostrados si sean los que correspondan al producto
- (RF6) Se añadirán nuevos comentarios y se verificara que estos sean añadidos correctamente a la base de datos
- (RF7) El usuario debe suministrar nombre, correo y contraseña para hacer el registro, y al finalizar el proceso el usuario debe tener el usuario y contraseña guardado en la base de datos
- (RF8) Se hará el proceso de inicio de sesión con diferentes usuarios de prueba, para comprobar su correcto funcionamiento.
- (RF9) Se añadirán diferentes productos de prueba para comprobar que estos se presenten de forma correcta.
- (RF10) Se añadirán y modificara el inventario de algunos productos de prueba, para revisar que la información del número del producto se actualice correctamente en la interfaz.
- (RF11) Se simulará una venta y se comprobará en la base de datos si el inventario disminuye satisfactoriamente
- (RF12) Se revisará que las imágenes montadas se guarden en la base de datos
- (RF13) Se comprobará que en la interfaz si se esté mostrando las imágenes de acuerdo al producto
 
## 4.3 Requerimientos de usabilidad.

- (RU1) Se actualizará el número de inventario de algunos productos y se comprobará que la interfaz se actualice.
- (RU2) Con ayuda de algunos datos de prueba se comprobará si la gráfica se actualiza por su cuenta ante la llegada de nueva información.
- (RU3) Se debe verificar que la calidad de la interfaz de usuario sea alta, esto se hará con la participación de testers, validando que sean capaces de encontrar las diferentes utilidades de forma rápida, y que la interacción con la aplicación sea sencilla e intuitiva.


## 4.4 Requerimientos de rendimiento.

- (RP1) Se añadirán 50 productos de prueba para comprobar la robustez de la plataforma.
- (RP2) Se hará el proceso de inicio de sesión 20 veces, para comprobar que nunca supere el tiempo límite.
- (RP3) Se hará proceso de registro 20 veces, para comprobar que nunca supere el tiempo límite.
- (RP4) Se comprobará la cantidad de recursos que usa la página y se evaluará si entra en un rango aceptable (Rango por definir).
- (RP5) Se comprobará si las gráficas cargan rápidamente, y de forma correcta.

## 4.5 Requisitos lógicos de la base de datos.

- (RL1) Se pedirá a personas fuera del desarrollo que vean la estructura de la base de datos, para comprobar que la misma tenga sentido y sea legible.
- (RL2) Se harán diversas búsquedas y sentencias en la base de datos y se comprobara que los resultados sean coherentes.
- (RL3) Se Registrarán diversos usuarios de prueba, y se revisara si cada uno efectivamente tiene su propia entrada en la base de datos.


## 4.6 Restricciones de diseño.

- (DC1) Se comprobará a través de la adición de diversos usuarios que tan bien se acopla a su estilo, para garantizar que cada usuario pueda plasmar su imagen en la plataforma. 
- (DC2) Se revisarán y priorizarán las diferentes tareas en cada Reunión, para buscar tener el mejor manejo del tiempo posible.
- (DC3) Se le especificara al cliente que la plataforma solo funciona con conexión a internet.

## 4.7 Atributos del sistema de software.

- (SA1) Mantenibilidad: Se simulará el proceso de mantenimiento con el proceso de actualización y se harán "Simulacros" que permitan asegurar que los futuros mantenimientos se hagan de forma correcta.
- (SA2) Disponibilidad: Se mantendrá abierta a la página unas 24 horas como prueba, para asegurar que esta siempre esté funcionando.
- (SA3) Fiabilidad: Se recorrerán las diferentes funciones de la página y se revisara que arrojen los resultados esperados.
- (SA4) Seguridad: se corroborará que la información en la base de datos sea privada, y que ningún usuario pueda acceder a la información de otro.
- (SA5) Desempeño: Se recorrerán las diferentes funciones de la página, y se medirán tiempos para asegurar que todo se ejecute de forma veloz.

## 4.8 Información de apoyo.
- (SI1) Input/Output: Se revisarán los inputs y se pondrán placeholders que especifiquen el input esperado.
- (SI2 Se comprobará el proceso de registro a través de la creación de una cuenta de prueba.
- (SI3) Se intentará que los puntos establecidos en este documento no cambien demasiado, pero de necesitar cambios se actualizará el documento.

# 5 Arquitectura

## 5.1 Vista Lógica
En el diagrama se pueden ver dos clases que corresponden a usuarios que se registran, por un lado esta el mercado, este es quien ingresara, eliminara o modificara los productos presentes en la base de datos, de esta forma un mercado posee cero o muchos productos. Por otro lado tenemos al usuario, que son quienes no pueden modificar los productos pero si podrán crear comentarios sobre los mismos, un usuario puede crear cero o muchos comentarios, y a la vez un producto puede tener cero o muchos comentarios.
![Clases_tel drawio](https://user-images.githubusercontent.com/110442546/198854836-d79c888b-517e-4116-b0da-1c015f439b3d.png)

 ## 5.2 Modelo de datos
 A continuación se dará una explicación de cada elemento visto en el diagrama.

-   Producto(Producto a vender):
    
    -   id: identificador único
    -   Categoría: Identificador de la categoría a la que pertenece
    -   Empresa: Identificador de la Empresa a la que pertenece
    -   Cantidad: Cantidad disponible de dicho producto
    -   Nombre: Nombre del producto
    -   Precio: Precio del producto
-   Mercado(Empresa que vende el producto):
    
    -   id: identificador único
    -   Nombre: Nombre de la Empresa para ingresar
    - Password: Contraseña para ingresar 
- Usuario:
    -   id: identificador único
    -   Nombre: Nombre del usuario
    - Apellido: Apellido del usuario
    - Dirección: Dirección del usuario
    - Ciudad: Ciudad del usuario
    - UserName: Nombre de usuario
    -   Correo: Correo del usuario
    -   Password: Contraseña del usuario
-   Comentario(Comentario de cierto producto):
    
    -   id: identificador único
    -   id_Productos: id del producto a quien pertenece
    -   id_Usuario: id del usuario que hizo el comentario  
    - Comentario: Comentario realizado
![datos_tel drawio](https://user-images.githubusercontent.com/110442546/198854879-eceed427-eaae-4b49-a8cd-e72c2ed636d5.png)

## 5.3 Diagrama de despliegue 
En este diagrama se observa como el browser busca en el servidor DNS la respectiva ip del dominio que se haya ingresado, en este caso, http://inoutinventario.online, cuando ya se tiene la ip el cliente se comunica a través del protocolo HTTP con el servidor de la aplicación, el cual finalmente se comunica por TCP/Ip con el servidor de datos para realizar las diferentes funciones.
![Despliegue_tel drawio](https://user-images.githubusercontent.com/110442546/198854878-35befc1e-a797-4136-9a09-9c6dd329595b.png)

## 5.4 Diagrama de Navegación
En este diagrama se puede observar como es la navegación a través de la aplicación.
![Nave_telematica drawio](https://user-images.githubusercontent.com/110442546/198865581-f2c966f1-7faf-4fc1-87ea-953ac0d68d99.png)


# 6 Desarrollo y Despliegue 
## 6.1 Aplicación
La aplicación fue desarrollada en django, Django es un framework web de alto nivel que permite el desarrollo rápido de sitios web seguros y mantenibles. En este desarrollamos los diferentes modelos, views, templates y demas elementos necesarios para la creación de la aplicación 
## 6.2 Base de datos
El gestor de base de datos utilizado fue postgresql, para que esta pudiera ser utilizada en el despliegue se creo una instancia de AWS como servido de base de datos. 
## 6.3 DNS
Para implementar el DNS se creo una nueva instancia en AWS la cual gracias a bind9 funciono como servidor DNS.
## 6.4 Dominio
Para el dominio se utilizo freenom, pagina web que permite obtener un dominio y configurarlo de forma gratuita.
## 6.5 Despliegue 
Para realizar el despliegue de la aplicacion se deben seguir varios pasos.
### Instanciar servidores InOut (Servers Ecommenrce)
Una vez instanciados los 3 se debe ejecutar la aplicacion InOut en cada una, para esto se hace.
sudo su
cd Proyecto_tel/InOut
python 3 manage.py runserver 0.0.0.0:3000

Cabe destacar que dos de los servers tendran una ip elastica y el tercero no la tendra, debido a que no se permitio crear mas instancias con estas caracteristicas.

### Intanciar Ecommerce main server 
Este es el serivdor principal, el cual tendra diferentes configuraciones que permiten el despliegue de la aplicacion, para esto se debe ejecutar.
sudo su
nano /etc/nginx/nginx.conf  
Y en este archivo modificar la ip del tercer server dentro de upstreambackend con la ip publica de la instancia del tercer server para finalmente ejecutar.
service nginx restart

### DNS primario y secundario
Se deben inicializar sus instancias correspondientes, dicho DNS fue configurado con la ayuda de bind9.

### Pruebas
De esta forma ya se podra utilizar la aplicacion si se ingresa al dominio http://inoutinventario.online
