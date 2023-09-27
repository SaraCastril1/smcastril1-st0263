# info de la materia: ST0263 Topicos especiales en telematica
#
## Estudiante: Manuela Tolosa - mtolosag@eafit.edu.co ; Sara María Castrillón Ríos - smcastril1@eafit.edu.co; Simon Gomez Arango - sgomeza13@eafit.edu.co
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Aplicación Monolítica con Balanceo y Datos Distribuidos (BD y archivos)
  
# 1. breve descripción de la actividad
Desplegar un CMS WordPress empleando la tecnología de contenedores en una arquitectura de alta disponibilidad con su propio dominio y certificado SSL. Se utilizará un balanceador de cargas de la capa de aplicación del WordPress, dos servidores adicionales para la base de datos y archivos distribuidos en NFS. Se desplegarán cinco VM en Google GCP para implementar esta arquitectura y mejorar la disponibilidad de la aplicación.
  
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

En general, se cumplieron con la mayoría de los requerimientos funcionales y no funcionales propuestos por el profesor. Sin embargo, no se pudo cumplir con el requisito de implementar un certificado SSL para las conexiones seguras a través de HTTPS.

Se desplegaron las cinco máquinas virtuales en Google Cloud, de las cuales dos correspondían al CMS WordPress, una a la base de datos MySQL, una al servidor NFS de archivos compartidos y una al balanceador de cargas basado en Nginx. Tres de estos servicios corren en contenedores de Docker (WordPress, base de datos y balanceador de carga).
  

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Como se mencionó anteriormente, del reto no se pudo cumplir con el requisito de el certificado SSL para las conexiones seguras, por lo que no se puede acceder por https sino solo por http.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

El diseño implementado es el que plantea el profesor en el enunciado:
![image](https://user-images.githubusercontent.com/60147085/228666003-3a14e263-5e38-4af1-9fbe-53d850e3d282.png)

Los dokcer con el wordpress tienen mapeado en el volumen una carpeta compartida que se conecta al servidor nfs, de esta forma, cualquier cambio quese haga desde cualquier maquina virtual (wordpress_main y wordpress_backup) se actualize en ambas automaticamente.


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Si quiere subir imagenes para probar el nfs, puede ingresar mediante la ruta reto3ssm.us.to/login, donde la usuario es user y la contraseña password

## como se compila y ejecuta.
todos los docker compose se encuentran en la ruta ~/ de la instancia.
Primero se levantan todas las maquinas virtuales, luego en las maquinas de "wordpress_main" y "wordpress_backup" conectarlas al servidor nfs con el comando:
```
sudo mount 100.24.108.199:/var/nfs/general /nfs/wp
```
Una vez hecho esto, puede proceder a iniciar el nginx, para esto, aplicar los siguientes comandos en la instancia "nginx_server"
```
sudo systemctl stop nginx
sudo docker-compose up -d
```
esto se hace para que utilice el nginx de docker y no nativo de la maquina
Ahora podemos levantar los docker con wordpress, para esto simplemente vamos a las instancias de "wordpress_main" y "wordpress_backup" y realizamos:
```
sudo docker-compose up -d
```
Una vez hecho esto, deberia poder conectarse por la url:
http://reto3ssm.us.to/
La url se conecta al servidor de nginx
  
## detalles del desarrollo.
  Todo el desarrollo está desplegado en la nube de Google Cloud Platform (GCP) utilizando IaaS, específicamente las máquinas virtuales del servicio Compute Engine. Se utilizaron contenedores de Docker montados a través de Docker Compose para los componentes de la aplicación en WordPress, la base de datos y el balanceador de carga. Para el servidor NFS, se configuró el host directamente en la máquina virtual.
  
## detalles técnicos
  - Tipo de maquina virtual: e2-Small.
  - Sistema operativo: Ubuntu 18.04 LTS.
  - Docker version 20.10.21.
  - Docker-compose version 1.17.1.
  - Base de datos: MySQL 5.7.
  - Balanceador de carga: NGINX.
  - CMS :WordPress.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
  Los diferentes parámetros se configuran en los archivos de Docker Compose, donde se especifica la dirección IP, los puertos, la conexión a la base de datos, las variables de ambiente, entre otros. Se pueden editar estos parámetros según las necesidades de cada caso.

  
## Organización del código por carpetas
  El código está organizado en varias carpetas, como se muestra:
![image](https://github.com/SaraCastril1/smcastril1-st0263/assets/67118511/d658a822-d936-42a7-80ce-f598f4d4b0e7)


## Resultados o pantallazos 
  
  Video Funcionando:
  https://drive.google.com/file/d/1AFZ70PPShL4-D9TiAPvRKnX5RekOTU5-/view?usp=sharing


# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## IP o nombres de dominio en nube o en la máquina servidor.
  - IPs:
  nfs:  100.24.108.199
  nginx: 54.235.70.229
  db:44.218.125.229
  wordpress1: 18.214.11.58
  wordpress2: 54.91.31.240
  
  - Dominio: http://reto3ssm.us.to/
  


.

## Resultados o pantallazos 
![WhatsApp Image 2023-09-27 at 1 31 18 PM (1)](https://github.com/SaraCastril1/smcastril1-st0263/assets/74980999/9d797834-004f-4b5c-a949-f6b9770f5e2c)


# referencias:

