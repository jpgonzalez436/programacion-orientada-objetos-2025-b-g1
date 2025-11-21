# Sistema de Gestión de Impresoras 3D – FABLAB

## 1. Descripción del proyecto

Este proyecto implementa un sistema sencillo para gestionar el uso de las impresoras 3D del laboratorio FABLAB.  
La idea es simular de forma ordenada el proceso real: un estudiante solicita el uso de una impresora, la solicitud pasa por aprobación del administrador (como si fueran las firmas), y luego la impresora queda marcada en uso hasta que termina el tiempo estimado de impresión.

No se usan bases de datos ni frameworks web. Todo está hecho con Python básico, programación orientada a objetos y menús por consola, más una parte web estática en HTML/CSS para presentar el proyecto.

---

## 2. Estructura del proyecto

```text
proyecto_poo_final/
├── application/
│   ├── index.html               # Página principal del sistema
│   ├── src/
│   │   └── css/
│   │       └── styles.css       # Estilos generales
│   └── view/
│       ├── dashboard.html       # Resumen del sistema de impresoras
│       ├── impresoras.html      # Listado y detalle de impresoras 3D
│       └── solicitudes.html     # Explicación del flujo de solicitudes
│
├── backend/
│   ├── __init__.py              # Inicialización del módulo backend
│   ├── modelos_impresora.py     # Clases: Impresora3D y SolicitudImpresion
│   ├── menu_impresoras.py       # Menú interactivo en consola (usuario y admin)
│   └── main.py                  # Punto de entrada, datos de prueba y arranque
│
├── architecture/
│   └── diagram_class_impresoras.wsd   # Diagrama de clases UML (PlantUML)
│
├── dependencias.md              # Guía de relaciones entre entidades
├── resumen_datos.md             # Resumen de datos y ejemplos de uso
└── README.md                    # Este archivo
```

## 3. Modelo de datos
El modelo es intencionalmente simple. Solo se manejan dos entidades de datos y una clase “sistema” que coordina todo.

3.1. Impresora3D
Representa una impresora 3D del FABLAB.

Campos principales:

id: identificador interno.

codigo: código de inventario (por ejemplo, 4020, 4021, etc.).

nombre: nombre descriptivo (por ejemplo, "CR-10 #1").

estado: "DISPONIBLE" o "EN_USO".

En esta versión se modelan cuatro impresoras CR-10 (4020, 4021, 4022 y 4023).

3.2. SolicitudImpresion
Representa una petición de uso de una impresora hecha por un estudiante.

Campos principales:

id: identificador de la solicitud.

codigo_estudiante: código único del estudiante.

nombre_estudiante: nombre completo del estudiante.

facultad: número entero que representa la facultad:

1 = Ingeniería Mecatrónica

2 = Ingeniería de Energías Renovables

3 = Ingeniería Industrial

impresora_id: id de la impresora solicitada.

fecha_impresion: fecha en formato dd/mm/aaaa.

duracion_minutos: duración estimada de la impresión.

material_gramos: cantidad de PLA en gramos.

estado: "PENDIENTE", "EN_CURSO", "FINALIZADA" o "RECHAZADA".

motivo_rechazo: texto opcional cuando se rechaza la solicitud.

3.3. SistemaImpresoras3D
Clase que mantiene:

Lista de impresoras.

Lista de solicitudes.

Y expone métodos para:

Crear solicitudes.

Buscar historial por impresora.

Listar solicitudes pendientes.

Aprobar, rechazar y finalizar solicitudes.

Consultar estado actual de cada impresora.

## 4. Reglas de negocio principales
Las reglas se intentan mantener claras y manejables:

Toda solicitud nueva entra en estado PENDIENTE.

Solo el administrador (menú con contraseña 1234) puede aprobar o rechazar solicitudes.

Al aprobar una solicitud:

La solicitud pasa a EN_CURSO.

La impresora asociada pasa a EN_USO.

Al finalizar una impresión:

La solicitud pasa a FINALIZADA.

La impresora vuelve a DISPONIBLE.

No se puede aprobar una solicitud si:

La impresora ya está EN_USO, o

Ya existe otra impresión aprobada (en curso o finalizada) para la misma impresora y la misma fecha.

El sistema asume que, idealmente, solo debe haber una impresión por día en cada impresora.

## 5. Uso del backend (consola)
5.1. Ejecución
Ubicarse en la carpeta del proyecto y ejecutar:

bash
Copiar código
python backend/main.py
El programa muestra un menú principal con opciones, por ejemplo:

Ver listado de impresoras y su estado.

Ver historial de uso de una impresora.

Crear una nueva solicitud de uso (rol estudiante).

Entrar al menú de administrador (clave 1234).

5.2. Menú de estudiante
Desde el menú de estudiante se puede:

Seleccionar una impresora.

Ingresar los datos de la solicitud:

Código y nombre del estudiante.

Facultad (1, 2 o 3).

Fecha de impresión.

Duración estimada en minutos.

Gramos de material PLA.

La solicitud queda registrada como PENDIENTE y se almacena en el historial del sistema.

5.3. Menú de administrador
Desde el menú de administración (clave fija 1234) se puede:

Ver todas las solicitudes en estado PENDIENTE.

Aprobar o rechazar solicitudes:

Al aprobar, el sistema valida reglas de disponibilidad y fecha.

Al rechazar, se puede escribir un motivo de rechazo.

Ver solicitudes EN_CURSO y marcarlas como FINALIZADA.

De esta forma se simula el flujo de firmas y aprobación que en la realidad pasa por vicerrector, director de programa y jefe de laboratorio, pero reducido a un paso de aprobación para mantener el proyecto simple.

## 6. Parte web (HTML)
La carpeta application/ contiene:

index.html: página principal del sistema.

view/dashboard.html: resumen del sistema de impresoras.

view/impresoras.html: detalle de las impresoras 3D modeladas.

view/solicitudes.html: explicación del flujo de solicitud, aprobación y uso.

Importante:

La parte web es estática.

No está conectada directamente al código Python.

Sirve para presentar el contexto, las entidades y el flujo del sistema en la sustentación.

Los estilos se comparten con el archivo src/css/styles.css, que también se reutiliza del proyecto guía, adaptado al nuevo contexto.

## 7. Tecnologías utilizadas
Python 3

Programación orientada a objetos básica, sin librerías externas.

Estructura simple en módulos (modelos_impresora, menu_impresoras, main).

HTML5 y CSS3

Vistas estáticas para explicar el sistema.

Reutilización y adaptación del diseño base del proyecto de ejemplo.

PlantUML

Archivo diagram_class_impresoras.wsd para el diagrama de clases.

## 8. Alcance y limitaciones
Alcance:

Gestión básica de:

Impresoras 3D.

Solicitudes de uso.

Aprobaciones y finalización de impresiones.

Historial de uso por impresora.

Simulación de flujo administrativo de forma simplificada.

Limitaciones:

No hay base de datos; todo se guarda en memoria mientras el programa está en ejecución.

La parte web no está conectada al backend Python.

Los nombres de estudiantes y códigos usados como ejemplo son inventados y solo se usan para pruebas.

## 9. Contexto académico
Este proyecto se desarrolla como trabajo final de Programación Orientada a Objetos, con las siguientes condiciones:

Código lo más simple posible, respetando lo básico de POO y PEP 8.

Sin uso de frameworks ni librerías avanzadas.

Enfoque en:

Diseño de clases.

Relaciones entre entidades.

Reglas de negocio claras y fáciles de explicar.

Separación mínima entre backend (Python) y vistas (HTML/CSS)