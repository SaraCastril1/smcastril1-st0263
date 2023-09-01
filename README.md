# ST0263 Temas especiales en telemática
#
# Sara María Castrillón Ríos - smcastril1@eafit.edu.co
#
# Edwin Nelson Montoya Múnera - emontoya@eafit.edu.co
#

# Procesos comunicantes por API REST, RPC y MOM
#
# 1. breve descripción de la actividad
Este reto buscaba comunicar diferentes procesos remotos a través de gRPC de manera sicrónica, con una integración de un middleware oriented message (rabbitMQ) como estrategia de toleracia a fallos asincrónica, en caso de que el servidor gRPC callera.

Se tenia un productor de mensajes gRPC alojado en una maquina remota, el cual tiene la capacidad de conectarse a un cliente, en nuestro caso Postman a través de API REST. Desde el productor gRPC, podemos conectarnos a un consumidor de mensajes, puede ser el pricipal, o el de MOM que es propuesto para casos de fallo. sin embargo el cliente no sabrá quien respondió a su petición, para garantizar la transparencia.
Una vez el cliente se conecta al productor y este ultimo lo dijire a un cosumidor, se atendera la petición de listar o encontrar archivos y se le enviará respuesta una vez completada.


## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se cumplió la funcionalidad de Apigateway, con ayuda de un API_Rest de flask, la cual toma las peticiones y las tranforma de JSON, que es el standar de la red a mensajes que puedan ser enviados por gRPC o AMQP a través de protobuffers. 
Se cumplió la funcionalidad tanto de buscar archivos como la de listarlos, la fucionalidad del primer microservicio conectado a traves de gRPC y se construyó correctamente la interfaz en donde se despliega en aws con una IP elastica.
Se cumplió la funcionalidad de toleracia a fallos en donde se responde a las peticiones de manera asincrónica con ayuda de rabbitMQ y que se haga pulling al MOM de la solicitud encolada.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
No se cumplió que el microservicio 2 devuelva la respuesta a las peticiones entrantes, pues a pesar de que es capaz de devolver mensajes, tiene problemas a la hora de enviar la respuesta esperada.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- La arquitectura es basada en microservicios los cuales se comunican entre si mediante grpc y colas.
- En la comunicacion por grpc se utilizan callbacks para atrapar posibles errores.
- En la comunicacion por colas se utilizan funciones asincrónas

Descripción del tiempo de vida de la solicitud:
![image](https://github.com/SaraCastril1/smcastril1-st0263/assets/84990901/760a8676-86c6-485f-ba21-d93eaa53cba4)

Inicialmente un cliente Postman se conecta a el procutor API_Gateway de mensajes, enviandole la solicitud desead listar, o encontrar archivos.  El API_Gateway se encarga de generar un mensaje claro para lo microservicios y este es enviado a uno de ellos
donde se generará respuesta y se enviará nuevamente al cliente. En condiciones igeales nuestra opción 1 será el srv_1 el cual funciona a través de gRPC y devolverá la solicitud inmediatmente. En caso de que esté servidor halla fallado se enviará la solicitud al ser_2, el cual está atendiendo a través de colas, se ha creado una cola para las request, que es donde el MOM irá en bsca de ellas para procesarlas y luego depositarlas en una segunda cola de responses en donde el API_Gateway podrá generar pulls con ayuda de un ID para saber si su request ha sido procesada.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc.
La principal tecnologia usada fue python, para el API REST se creo una API con flask, y para la comunicacion con los microservicios se usó gRPC y Rabbitmq. 
Se utilizó docker para lanzar el el servidor de rabbitMQ y Makefile para facilitar la compilación.
Además de los archivos .proto para generar los contrados de mesajería IDL.

## como se compila y ejecuta.
Hay que tener en cuenta que se tienen 4 máquinas remotas.

La primera máquina a configurar es la de MOM con dirección IP elastica: 54.85.196.208
Se verificar que esta corriendo rabbitmq en la imagen de docker, si no esta corriendo inicializar:
```
docker start rabbit-server
```
Una vez inicializado el rabbitMO podemos ingresar desde el navegador a http://54.85.196.208:15672/ para acceder, vizualizar y modificar uestras colas y exchanges. El usuario y contraseña por defecto son "user" y "password".


Una vez hemos subido el rabbit-server, debemos empezar a correr los microservicios. Es indispensable que estos se corran primero, pues serán los que se podrán a esperar por peticiones.

Para correr el microservicio 1 nos ubicamos en la carpeta donde este se encuentra.
```
cd smcastril1-st0263/Reto2/Solucion-DEFINITIVO/srv_1
```
Una vez estamos el la carpeta, debemos compilar e instalar las dependencias necesarias, para lo cual se creó un Makefile que hará la tarea por usted.
```
make srv_1
```

Finalemente corremos el ejecutable del microservicio 1.
```
python3 consumer_grpc.py
```
A continuación se pondrá a correr el microservicio 2, los pasos a seguir son muy similares:

Para correr el microservicio 2 nos ubicamos en la carpeta donde este se encuentra.
```
cd smcastril1-st0263/Reto2/Solucion-DEFINITIVO/srv_2
```
Una vez estamos el la carpeta, debemos compilar e instalar las dependencias necesarias, para lo cual se creó un Makefile que hará la tarea por usted.
```
make srv_2
```

Finalemente corremos el ejecutable del microservicio 1.
```
python3 consumer_grpc.py
```

## detalles técnicos
Para el rabbitmq se utilizan los exchange para administrar la cola.
El grpc se implemento mediante callbacks
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
La API de flask corre en el puerto 5000, el de grpc en el puerto 50051 y rabbitmq por los puertos por defecto(5672 y 15672)

## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
Cada servicio esta separado en carpetas idependientes, cada uno tiene sus propias dependencias y variables de entorno
