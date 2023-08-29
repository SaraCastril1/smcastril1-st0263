# ST0263 Temas especiales en telemática
#
# Sara María Castrillón Ríos - smcastril1@eafit.edu.co
#
# Edwin Nelson Montoya Múnera - emontoya@eafit.edu.co
#

# Procesos comunicantes por API REST, RPC y MOM
#
# 1. breve descripción de la actividad
#
<texto descriptivo>

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se cumplió la funcionalidad de Apigateway, con ayuda de un API_Rest de flask, la cual toma las peticiones. Se cumplió la funcionalidad tanto de buscar archivos como la de listarlos, la fucionalidad del primer microservicio conectado a traves de gRPC y se construyó correctamente la interfaz en donde se despliega en aws con una ip elastica.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
No se cumplió que el microservicio 2 devuelva la respuesta a las peticiones entrantes.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
- La arquitectura es basada en microservicios los cuales se comunican entre si mediante grpc y colas.
- En la comunicacion por grpc se utilizan callbacks para atrapar posibles errores.
- En la comunicacion por colas se utilizan funciones asincronas


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
La principal tecnologia usada fue python, para el API REST se creo una API con flask, y para la comunicacion con los microservicios gRPC y Rabbitmq. 
Se utilizó docker para lanzar el el servidor de rabbitMQ y make para facilitar la compilación.

## como se compila y ejecuta.
Primero verificar que esta corriendo rabbitmq en la imagen de docker, si no esta corriendo inicializar:
```
docker start rabbit-server
```
Luego ir a la carpeta de repositorio
```
cd smcastril1-st0263
```
Luego en tres consolas diferentes compilar e inicializar el apigateway y los dos microservicios
```
cd ApiGateway
make API_Gateway
python3 producer_grpc.py
```
```
cd microservicio1
make srv_1
python3 consumer_grpc.py
```
```
cd microservicio2
make srv_2
python3 consumer_grpc.py
```
## detalles técnicos
Para el rabbitmq se utilizan los exchange para administrar la cola.
El grpc se implemento mediante callbacks
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
La API de flask corre en el puerto 5000, el de grpc en el puerto 50051 y rabbitmq por los puertos por defecto(5672 y 15672)

## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
Cada servicio esta separado en carpetas idependientes, cada uno tiene sus propias dependencias y variables de entorno
