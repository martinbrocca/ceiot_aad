# CEIoT - Arquitectura de Datos - Trabajo Final

## Objetivo

<p>Desarrollar el modelo e implementación de un aplicativo para visualizar una topología de red a nivel de capa 1/2 </p>
<p>Realizar el diseño lógico e implementación de una CMDB* a escala para dispositivos de redes bajo un modelo relacional. La CMDB Deberá constar de datos básicos para describir los dispositivos (Marca, Modelo, Función, etc.) y deberá incluir información de protocolos de descubrimiento de capa de enlace (CDP/LLDP) </p>
<p>&Realizar el diseño de una base de datos de grafos para almacenar las relaciones de los nodos como así también algunas propiedades básicas para su filtrado.</p>
<p>Realizar un aplicativo simple (o visualización a través de la base de datos) de las capacidades de filtrado y reporte de la topología.</p>
<p>*CMDB: Base de datos de inventario y administración de configuraciones de dispositivos </p>

## Consideraciones

<p>Por no contar con un laboratorio real, tanto los dispositivos como la topología serán generados manualmente (o por script de generación)</p>
<p>El proceso de carga en la BD de grafos no será en tiempo real (batch y por frecuencia fija)</p>

## Implementacion

### Modelo DER y Base de Datos Relacional

<p> La Base de datos elegida, sera la sugerida por la materia: PostgreSQL </p>
<p>El modelo contará con una tabla de equipos, para control de inventario de dispositivos, una tabla de ubicaciones, para indicar el lugar de instalación, y finalmente sendas tablas de Estado y Clase, para indicar la condición del dispositivo, como así también su uso/función respectivamente. </p>
<p>La información de conectividad entre equipos será almacenada en una tabla de topología, que incluya la interfaz de red usada en esa conexión.</p>

<p>La topología será cargada en forma manual, simulando una estructura de árbol.</p>
<p>Un script de Python ejecutara la sentencia SQL para extraer la información, y guardara el resultado en un archivo en formato Json</p>

![alt text] (/images/DER.png)
