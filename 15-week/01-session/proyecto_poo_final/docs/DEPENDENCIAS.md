# Guía de dependencias entre entidades  
Sistema de Gestión de Impresoras 3D – FABLAB

## 1. Introducción

Este documento resume las dependencias entre las entidades del **Sistema de Gestión de Impresoras 3D del FABLAB**.  
La idea es dejar claro quién depende de quién y bajo qué reglas se controla el uso de las impresoras.

---

## 2. Concepto de dependencia

En este proyecto, una **dependencia** significa que una entidad necesita referenciar a otra para que sus datos tengan sentido.

Ejemplo sencillo:  
Una **solicitud de impresión** siempre debe estar asociada a una **impresora** específica.

Tipos de relaciones usadas:

- **1:1** – Uno a uno  
- **1:\*** – Uno a muchos (un padre puede tener varios hijos)  
- **N:1** – Muchos a uno (varios hijos pertenecen a un solo padre)

---

## 3. Árbol de dependencias

En este sistema solo hay dos entidades de datos centrales:

- **Impresora3D**: representa cada impresora física del FABLAB.  
- **SolicitudImpresion**: representa cada petición de uso hecha por un estudiante.

La clase **SistemaImpresoras3D** orquesta la lógica del sistema, pero no es una entidad de datos como tal.

### 3.1. Entidad Impresora3D (independiente)

**Propósito:** representar una impresora 3D del laboratorio.

**Atributos principales:**

- `id`: entero, identificador interno.  
- `codigo`: string corto, por ejemplo `"4020"`.  
- `nombre`: nombre descriptivo, por ejemplo `"CR-10 #1"`.  
- `estado`: `"DISPONIBLE"` o `"EN_USO"`.

**Ejemplos de registro:**

```text
1, "4020", "CR-10 #1", "DISPONIBLE"
2, "4021", "CR-10 #2", "DISPONIBLE"
3, "4022", "CR-10 #3", "EN_USO"
4, "4023", "CR-10 #4", "EN_USO"
```
Dependencias:

No depende de ninguna otra entidad.

Es referenciada por SolicitudImpresion mediante impresora_id.

Regla básica:

Una impresora debe existir antes de registrar solicitudes asociadas a ella.

3.2. Entidad SolicitudImpresion (depende de Impresora3D)
Propósito: representar una petición de uso de una impresora hecha por un estudiante.
No se maneja una tabla de estudiantes; los datos del estudiante se guardan directamente en la solicitud.

### Atributos principales:

id: entero, identificador interno de la solicitud.

codigo_estudiante: string, código único del estudiante (ejemplo: "1905001001").

nombre_estudiante: nombre completo del estudiante.

facultad: entero que representa la facultad:

1 = Ingeniería Mecatrónica

2 = Ingeniería de Energías Renovables

3 = Ingeniería Industrial

impresora_id: id de la impresora (Impresora3D.id) que se desea usar.

fecha_impresion: string en formato "dd/mm/aaaa".

duracion_minutos: duración estimada de la impresión en minutos.

material_gramos: cantidad de material PLA en gramos.

estado: cadena con uno de estos valores:

"PENDIENTE"

"EN_CURSO"

"FINALIZADA"

"RECHAZADA"

motivo_rechazo: texto opcional cuando la solicitud es rechazada (puede estar vacío).

Dependencias:

Depende de Impresora3D a través de impresora_id (N:1).

### Ejemplos de registros:

text
Copiar código
1, "1905001001", "Alex Ramírez", 1, 1,
   "10/06/2025", 120, 80, "FINALIZADA", None

3, "1905001003", "Diego Martínez", 2, 3,
   "20/06/2025", 180, 120, "EN_CURSO", None

5, "1905001005", "Luis Herrera", 1, 1,
   "25/06/2025", 120, 90, "PENDIENTE", None
Reglas de integridad:

impresora_id siempre debe apuntar a una impresora existente.

Toda solicitud nueva empieza en estado "PENDIENTE".

Solo se puede aprobar o rechazar una solicitud que esté en "PENDIENTE".

Solo se puede finalizar una impresión que esté en "EN_CURSO".

## 4. Rol de la clase SistemaImpresoras3D
Aunque no es una “tabla” de datos, la clase SistemaImpresoras3D es la que organiza todo.

Responsabilidades principales:

Mantener en memoria:

impresoras: List[Impresora3D]

solicitudes: List[SolicitudImpresion]

Crear solicitudes (crear_solicitud).

Consultar historial de una impresora (obtener_historial_impresora).

Listar solicitudes pendientes (obtener_solicitudes_pendientes).

Aprobar y rechazar solicitudes (aprobar_solicitud, rechazar_solicitud).

Finalizar impresiones (finalizar_impresion).

Consultar estado de cada impresora (obtener_estado_impresora).

Además:

Asigna el id de cada nueva solicitud.

Mantiene sincronizado el estado de la impresora con el estado de las solicitudes:

Solicitud "EN_CURSO" → impresora "EN_USO".

Solicitud "FINALIZADA" → impresora "DISPONIBLE".

## 5. Matriz de dependencias
Entidad	Nivel	Depende de	Es referenciada por	Tipo de relación
Impresora3D	0	–	SolicitudImpresion	1:*
SolicitudImpresion	1	Impresora3D	SistemaImpresoras3D	N:1 (respecto a Impresora3D)
SistemaImpresoras3D	–	– (orquestador)	–	Maneja listas en memoria

Resumen práctico:

Una impresora puede aparecer en muchas solicitudes.

Cada solicitud solo puede apuntar a una impresora.

## 6. Reglas globales del sistema
6.1. Integridad referencial
Toda solicitud debe apuntar a una impresora válida.

No se deben dejar solicitudes que referencien impresoras que ya no existen.

Ejemplo:

Si impresora_id = 3, la impresora con id = 3 debe existir.

6.2. Estado de la impresora según las solicitudes
Cuando se aprueba una solicitud y pasa a "EN_CURSO", la impresora asociada pasa a "EN_USO".

Cuando se finaliza una impresión, la solicitud pasa a "FINALIZADA" y la impresora vuelve a "DISPONIBLE".

No se puede aprobar una solicitud si la impresora ya está "EN_USO".

6.3. Una impresión por día y por impresora
Regla de negocio importante:

Para una impresora concreta y una fecha concreta, no debe haber más de una impresión aprobada (en curso o finalizada).

En otras palabras:

Si ya existe una solicitud "EN_CURSO" o "FINALIZADA" para la impresora X el día dd/mm/aaaa, no se debe aprobar otra solicitud para esa misma impresora y esa misma fecha.

6.4. Flujo de vida de una solicitud
Registro de solicitud (menú estudiante)

Se piden: código, nombre, facultad (1, 2 o 3), impresora, fecha, duración estimada y gramos de material.

La solicitud entra en estado "PENDIENTE".

Revisión por administrador (menú admin, clave 1234)

Ve todas las solicitudes en "PENDIENTE".

Para cada una puede:

Aprobar (si la impresora está disponible y no tiene otra impresión ese día).

Rechazar, indicando un motivo.

Aprobación

La solicitud pasa a "EN_CURSO".

La impresora pasa a "EN_USO".

Finalizar impresión

Desde el menú admin se marca la solicitud como finalizada.

La solicitud pasa a "FINALIZADA".

La impresora vuelve a "DISPONIBLE".

## 7. Ejemplos de escenarios
7.1. Aprobación válida
Impresora 1 está "DISPONIBLE" el 25/06/2025.

Hay una solicitud pendiente para esa impresora y esa fecha.

Resultado esperado:

El administrador la aprueba.

La solicitud queda "EN_CURSO".

La impresora pasa a "EN_USO".

7.2. Aprobación con impresora ocupada
Impresora 3 está "EN_USO" el 20/06/2025.

Llega otra solicitud pendiente para esa misma impresora y la misma fecha.

Resultado esperado:

El sistema no debe permitir aprobarla.

La solicitud se mantiene "PENDIENTE" o se devuelve un mensaje de error.

7.3. Finalizar una impresión
Hay una solicitud "EN_CURSO" asociada a la impresora 4.

Resultado esperado:

Al finalizar:

La solicitud pasa a "FINALIZADA".

La impresora vuelve a "DISPONIBLE".

## 8. Conclusiones del proyecto
El modelo de dependencias se mantiene intencionalmente simple:

Solo relaciona impresoras y solicitudes de impresión.

Usa una clase de sistema para orquestar la lógica, sin meter más capas de complejidad.

Con esto se logra:

Mantener integridad de datos (sin referencias rotas).

Tener control básico y claro sobre el uso de las impresoras.

Evitar choques de impresión en la misma impresora y fecha.

Contar con un historial de uso por impresora, útil para revisar el funcionamiento del sistema y sustentar el proyecto.