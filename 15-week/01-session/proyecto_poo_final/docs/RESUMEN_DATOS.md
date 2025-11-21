# Resumen de datos iniciales  
Sistema de Gestión de Impresoras 3D – FABLAB

## 1. Introducción

Este documento resume los datos de ejemplo que se usan en el backend del **Sistema de Gestión de Impresoras 3D del FABLAB**.  
Los datos sirven para probar el sistema en consola, mostrar el historial de uso, simular solicitudes pendientes y verificar las reglas de aprobación.

---

## 2. Impresoras 3D modeladas

Se modelan cuatro impresoras tipo CR-10, identificadas por un código corto similar al usado en el laboratorio.

| ID | Código | Nombre      | Estado inicial |
|----|--------|-------------|----------------|
| 1  | 4020   | CR-10 #1    | DISPONIBLE     |
| 2  | 4021   | CR-10 #2    | DISPONIBLE     |
| 3  | 4022   | CR-10 #3    | EN_USO         |
| 4  | 4023   | CR-10 #4    | EN_USO         |

Interpretación:

- Hay 4 impresoras activas en el sistema.
- Dos están libres para asignar nuevas solicitudes.
- Dos aparecen ya en uso, asociadas a solicitudes en curso.

---

## 3. Facultades y codificación

En las solicitudes no se guarda un objeto “facultad”, sino un número entero:

- `1` = Ingeniería Mecatrónica  
- `2` = Ingeniería de Energías Renovables  
- `3` = Ingeniería Industrial  

Los códigos de estudiante siguen un formato numérico similar a los códigos reales, por ejemplo:

- `1905001001`, `1905001002`, `1905001003`, etc.

Los nombres de estudiantes usados en los ejemplos son ficticios y se generaron solo para pruebas.

---

## 4. Solicitudes de impresión de ejemplo

Las solicitudes de impresión son el corazón del sistema. Cada solicitud tiene:

- Estudiante (código y nombre).
- Facultad (1, 2 o 3).
- Impresora asociada.
- Fecha de impresión.
- Duración en minutos.
- Material en gramos de PLA.
- Estado: `PENDIENTE`, `EN_CURSO`, `FINALIZADA` o `RECHAZADA`.

A continuación se muestran ejemplos agrupados por estado.

### 4.1. Solicitudes finalizadas

Representan impresiones ya realizadas.

| ID | Estudiante (código) | Estudiante (nombre) | Facultad | Impresora | Fecha       | Duración (min) | Material (g) | Estado      |
|----|----------------------|---------------------|----------|-----------|-------------|----------------|--------------|------------|
| 1  | 1905001001          | Alex Ramírez        | 1        | 4020      | 10/06/2025  | 120            | 80           | FINALIZADA  |
| 2  | 1905001002          | Daniela López       | 3        | 4021      | 12/06/2025  | 90             | 60           | FINALIZADA  |

Lectura rápida:

- Se realizaron al menos dos trabajos de impresión completos.
- Participan estudiantes de Mecatrónica (1) e Industrial (3).

### 4.2. Solicitudes en curso

Son impresiones aprobadas que en teoría se están ejecutando.

| ID | Estudiante (código) | Estudiante (nombre) | Facultad | Impresora | Fecha       | Duración (min) | Material (g) | Estado   |
|----|----------------------|---------------------|----------|-----------|-------------|----------------|--------------|---------|
| 3  | 1905001003          | Diego Martínez      | 2        | 4022      | 20/06/2025  | 180            | 120          | EN_CURSO |
| 4  | 1905001004          | Laura Sánchez       | 1        | 4023      | 21/06/2025  | 150            | 100          | EN_CURSO |

Relación con impresoras:

- La impresora 4022 está ocupada por la solicitud 3.
- La impresora 4023 está ocupada por la solicitud 4.
- Por eso ambas impresoras aparecen en estado `EN_USO`.

### 4.3. Solicitudes pendientes

Son solicitudes registradas por estudiantes que aún no han sido aprobadas ni rechazadas por el administrador.

| ID | Estudiante (código) | Estudiante (nombre) | Facultad | Impresora | Fecha       | Duración (min) | Material (g) | Estado     |
|----|----------------------|---------------------|----------|-----------|-------------|----------------|--------------|-----------|
| 5  | 1905001005          | Luis Herrera        | 1        | 4020      | 25/06/2025  | 120            | 90           | PENDIENTE  |
| 6  | 1905001006          | Sofía Ríos          | 2        | 4021      | 25/06/2025  | 60             | 40           | PENDIENTE  |

Uso típico:

- Estas solicitudes se muestran en el menú de administrador.
- Desde ahí se decide si se aprueban o rechazan.

### 4.4. Solicitudes rechazadas (opcional)

No es obligatorio tener datos de este tipo para que el sistema funcione, pero se puede usar un ejemplo para probar la lógica:

| ID | Estudiante (código) | Estudiante (nombre) | Facultad | Impresora | Fecha       | Duración (min) | Material (g) | Estado     | Motivo rechazo                  |
|----|----------------------|---------------------|----------|-----------|-------------|----------------|--------------|-----------|---------------------------------|
| 7  | 1905001007          | Mario Castillo      | 1        | 4020      | 26/06/2025  | 240            | 300          | RECHAZADA | Material excede el límite diario |

---

## 5. Historial por impresora (ejemplo)

Con estos datos, el historial de cada impresora quedaría, por ejemplo:

### Impresora 4020 (CR-10 #1)

- Solicitud 1 – 10/06/2025 – 120 min – FINALIZADA.  
- Solicitud 5 – 25/06/2025 – 120 min – PENDIENTE.  
- Solicitud 7 – 26/06/2025 – 240 min – RECHAZADA.

Estado actual:

- La impresora 4020 aparece como `DISPONIBLE`.  
- Tiene un uso histórico (impresión finalizada) y varias solicitudes registradas.

### Impresora 4022 (CR-10 #3)

- Solicitud 3 – 20/06/2025 – 180 min – EN_CURSO.

Estado actual:

- La impresora 4022 aparece `EN_USO` porque tiene una impresión en curso.

De forma similar se puede leer el historial de las otras dos impresoras.

---

## 6. Estadísticas generales

Sobre los datos de ejemplo:

- Impresoras totales: **4**  
  - Disponibles: 2  
  - En uso: 2  

- Solicitudes totales: **7**  
  - Finalizadas: 2  
  - En curso: 2  
  - Pendientes: 2  
  - Rechazadas: 1  

Distribución por facultad (sobre estas solicitudes):

- Mecatrónica (1): varias solicitudes repartidas en distintos estados.  
- Renovables (2): al menos dos solicitudes.  
- Industrial (3): al menos una solicitud finalizada.

Estas cantidades son suficientes para:

- Probar el menú de estudiante (creación de nuevas solicitudes).  
- Probar el menú de administrador (aprobación, rechazo y finalización).  
- Ver historiales de uso por impresora y comprobar el cambio de estados.

---

## 7. Comentario final

Los datos se diseñaron para que:

- El sistema tenga casos en todos los estados posibles (`PENDIENTE`, `EN_CURSO`, `FINALIZADA`, `RECHAZADA`).  
- Existan impresoras libres y otras ocupadas para probar las validaciones.  
- Se puedan mostrar historiales variados por impresora durante la ejecución del programa.