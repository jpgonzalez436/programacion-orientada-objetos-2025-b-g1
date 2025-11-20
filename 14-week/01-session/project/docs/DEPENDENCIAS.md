# 🔗 Guía de Dependencias entre Entidades

## 📚 Introducción

Este documento explica en detalle las dependencias y relaciones entre todas las entidades del Sistema de Gestión de Recursos de CORHUILA, basado en el diagrama de clases UML proporcionado.

---

## 🎯 Concepto de Dependencia

Una **dependencia** en este contexto significa que una entidad (hija) necesita una referencia a otra entidad (padre) para existir de manera coherente en el sistema.

### Tipos de Relaciones
- **1:1** - Uno a uno
- **1:\*** - Uno a muchos (Un padre puede tener múltiples hijos)
- **N:1** - Muchos a uno (Múltiples hijos pertenecen a un padre)

---

## 🏗️ Árbol de Dependencias

### Rama Empresarial (Estructura Organizacional)

```
EMPRESA [Nivel 0 - Independiente]
│
├─ atributos: id, nombre, nit, direccion
├─ ejemplo: ID=1, CORHUILA, NIT=900123456-7
│
└──> SEDE [Nivel 1 - Depende de Empresa]
     │
     ├─ atributos: id, nombre, direccion, EmpresaId
     ├─ dependencia: EmpresaId → Empresa.id (N:1)
     ├─ ejemplos: 
     │  ├─ ID=1, Quirinal, EmpresaId=1
     │  └─ ID=2, Prado Alto, EmpresaId=1
     │
     └──> BLOQUE [Nivel 2 - Depende de Sede]
          │
          ├─ atributos: id, nombre, SedeId
          ├─ dependencia: SedeId → Sede.id (N:1)
          ├─ ejemplos:
          │  ├─ ID=1, Bloque A, SedeId=1 (Quirinal)
          │  ├─ ID=2, Bloque B, SedeId=1 (Quirinal)
          │  ├─ ID=6, Bloque C, SedeId=2 (Prado Alto)
          │  └─ ID=7, Laboratorios, SedeId=2 (Prado Alto)
          │
          └──> SALÓN [Nivel 3 - Depende de Bloque]
               │
               ├─ atributos: id, nombre, capacidad, BloqueId
               ├─ dependencia: BloqueId → Bloque.id (N:1)
               └─ ejemplos:
                  ├─ ID=1, Salón 508, capacidad=30, BloqueId=6
                  ├─ ID=2, Salón 411, capacidad=30, BloqueId=6
                  └─ ID=4, Salón 208, capacidad=30, BloqueId=5
```

### Rama de Recursos (Inventario)

```
CATEGORÍA [Nivel 0 - Independiente]
│
├─ atributos: id, nombre, descripcion
├─ ejemplos:
│  ├─ ID=1, Computadores, "Dispositivos electrónicos"
│  ├─ ID=2, Muebles, "Elementos de mobiliario"
│  └─ ID=3, Videobeam, "Dispositivos de proyección"
│
└──> ELEMENTO [Nivel 1 - Depende de Categoría]
     │
     ├─ atributos: id, nombre, descripcion, CategoriaId
     ├─ dependencia: CategoriaId → Categoria.id (N:1)
     └─ ejemplos:
        ├─ ID=1, Computador HP, CategoriaId=1
        ├─ ID=4, Silla plástica, CategoriaId=2
        ├─ ID=8, Proyector Epson, CategoriaId=3
        └─ ID=10, Tablero blanco, CategoriaId=5
```

### Entidad Puente (Conecta ambas ramas)

```
RECURSOSALÓN [Nivel 4 - Entidad Integradora]
│
├─ atributos: id, SalonId, ElementoId, cantidad
├─ dependencias:
│  ├─ SalonId → Salon.id (N:1)
│  └─ ElementoId → Elemento.id (N:1)
│
├─ propósito: Conecta la estructura física con el inventario
│
└─ ejemplos:
   ├─ ID=1, SalonId=1, ElementoId=6, cantidad=30
   │  └─ 30 Computadores HP en Salón 508
   │
   ├─ ID=2, SalonId=1, ElementoId=7, cantidad=30
   │  └─ 30 Sillas plásticas en Salón 508
   │
   └─ ID=4, SalonId=1, ElementoId=8, cantidad=1
      └─ 1 Proyector Epson en Salón 508
```

---

## 🔍 Análisis Detallado por Entidad

### 1. EMPRESA (Independiente)

**Nivel de dependencia:** 0 (no depende de nadie)

```yaml
Características:
  - Entidad raíz de la rama empresarial
  - No tiene dependencias hacia arriba
  - Es referenciada por Sede

Reglas de integridad:
  - Debe existir antes de crear sedes
  - Su eliminación afecta a todas las sedes (cascada)

Datos actuales:
  - Total registros: 1
  - CORHUILA es la única empresa en el sistema
```

---

### 2. SEDE (Depende de Empresa)

**Nivel de dependencia:** 1

```yaml
Depende de:
  - Empresa (obligatorio)

Dependencia:
  EmpresaId → Empresa.id

Reglas de integridad:
  - NO puede existir una sede sin empresa
  - EmpresaId debe corresponder a una empresa válida
  - Una empresa puede tener múltiples sedes (1:*)

Ejemplo de validación:
  ✅ VÁLIDO: SedeId=1, EmpresaId=1 (CORHUILA existe)
  ❌ INVÁLIDO: SedeId=3, EmpresaId=99 (Empresa 99 no existe)

Datos actuales:
  - Total registros: 2
  - Ambas sedes pertenecen a CORHUILA (EmpresaId=1)
```

---

### 3. BLOQUE (Depende de Sede)

**Nivel de dependencia:** 2

```yaml
Depende de:
  - Sede (obligatorio)
  - Indirectamente de Empresa (a través de Sede)

Dependencia:
  SedeId → Sede.id

Cadena de dependencia:
  Bloque → Sede → Empresa

Reglas de integridad:
  - NO puede existir un bloque sin sede
  - SedeId debe corresponder a una sede válida
  - Una sede puede tener múltiples bloques (1:*)

Ejemplo de validación:
  ✅ VÁLIDO: BloqueId=1, SedeId=1 (Sede Quirinal existe)
  ❌ INVÁLIDO: BloqueId=8, SedeId=99 (Sede 99 no existe)

Datos actuales:
  - Total registros: 7
  - Distribución:
    • Sede Quirinal (1): 3 bloques
    • Sede Prado Alto (2): 4 bloques
```

---

### 4. SALÓN (Depende de Bloque)

**Nivel de dependencia:** 3

```yaml
Depende de:
  - Bloque (obligatorio)
  - Indirectamente de Sede (a través de Bloque)
  - Indirectamente de Empresa (a través de Sede)

Dependencia:
  BloqueId → Bloque.id

Cadena de dependencia:
  Salón → Bloque → Sede → Empresa

Reglas de integridad:
  - NO puede existir un salón sin bloque
  - BloqueId debe corresponder a un bloque válido
  - Un bloque puede tener múltiples salones (1:*)

Ejemplo de validación:
  ✅ VÁLIDO: SalonId=1, BloqueId=6 (Bloque C existe)
  ❌ INVÁLIDO: SalonId=5, BloqueId=99 (Bloque 99 no existe)

Trazabilidad completa del Salón 508:
  Salón 508 (ID=1)
    → Bloque C (ID=6)
      → Sede Prado Alto (ID=2)
        → CORHUILA (ID=1)

Datos actuales:
  - Total registros: 4
  - Todos en Sede Prado Alto
  - Bloque C: 3 salones
  - Bloque B: 1 salón
```

---

### 5. CATEGORÍA (Independiente)

**Nivel de dependencia:** 0 (no depende de nadie)

```yaml
Características:
  - Entidad raíz de la rama de recursos
  - No tiene dependencias hacia arriba
  - Es referenciada por Elemento

Reglas de integridad:
  - Debe existir antes de crear elementos
  - Su eliminación afecta a todos los elementos (cascada)

Datos actuales:
  - Total registros: 6
  - Categorías: Computadores, Muebles, Videobeam, 
                Aire acondicionado, Tablero, Telón
```

---

### 6. ELEMENTO (Depende de Categoría)

**Nivel de dependencia:** 1

```yaml
Depende de:
  - Categoría (obligatorio)

Dependencia:
  CategoriaId → Categoria.id

Reglas de integridad:
  - NO puede existir un elemento sin categoría
  - CategoriaId debe corresponder a una categoría válida
  - Una categoría puede tener múltiples elementos (1:*)

Ejemplo de validación:
  ✅ VÁLIDO: ElementoId=1, CategoriaId=1 (Computadores existe)
  ❌ INVÁLIDO: ElementoId=12, CategoriaId=99 (Categoría 99 no existe)

Datos actuales:
  - Total registros: 11
  - Distribución por categoría:
    • Computadores (1): 4 elementos
    • Muebles (2): 3 elementos
    • Videobeam (3): 1 elemento
    • Aire acondicionado (4): 1 elemento
    • Tablero (5): 1 elemento
    • Telón (6): 1 elemento
```

---

### 7. RECURSOSALÓN (Entidad Puente - Doble Dependencia)

**Nivel de dependencia:** 4 (el más profundo)

```yaml
Depende de:
  - Salón (obligatorio)
  - Elemento (obligatorio)
  - Indirectamente: Bloque, Sede, Empresa, Categoría

Dependencias:
  SalonId → Salon.id
  ElementoId → Elemento.id

Cadena de dependencia COMPLETA:
  RecursoSalón 
    → Salón → Bloque → Sede → Empresa
    → Elemento → Categoría

Reglas de integridad:
  - NO puede existir sin salón y elemento válidos
  - SalonId debe corresponder a un salón existente
  - ElementoId debe corresponder a un elemento existente
  - La cantidad debe ser mayor a 0

Ejemplo de validación:
  ✅ VÁLIDO: 
     RecursoId=1, SalonId=1, ElementoId=6, cantidad=30
     (Salón 508 existe, Computador HP existe)
  
  ❌ INVÁLIDO: 
     RecursoId=8, SalonId=99, ElementoId=1, cantidad=10
     (Salón 99 no existe)

Trazabilidad completa del Recurso ID=1:
  RecursoSalón (ID=1)
    → Salón 508 (ID=1)
      → Bloque C (ID=6)
        → Sede Prado Alto (ID=2)
          → CORHUILA (ID=1)
    → Computador HP (ID=6)
      → Categoría Computadores (ID=1)

Datos actuales:
  - Total registros: 7
  - Todos asignados al Salón 508
  - Representa 95 unidades totales de equipamiento
```

---

## 📊 Matriz de Dependencias

| Entidad | Nivel | Depende de | Es referenciada por | Tipo Relación |
|---------|-------|------------|---------------------|---------------|
| Empresa | 0 | - | Sede | 1:* |
| Sede | 1 | Empresa | Bloque | N:1, 1:* |
| Bloque | 2 | Sede | Salón | N:1, 1:* |
| Salón | 3 | Bloque | RecursoSalón | N:1, 1:* |
| Categoría | 0 | - | Elemento | 1:* |
| Elemento | 1 | Categoría | RecursoSalón | N:1, 1:* |
| RecursoSalón | 4 | Salón + Elemento | - | N:1, N:1 |

---

## ✅ Reglas Globales de Integridad

### 1. Integridad Referencial
- **Toda clave foránea debe apuntar a un registro existente**
- Ejemplo: Si BloqueId=6, el Bloque con ID=6 debe existir

### 2. Cascada de Eliminación
- **Al eliminar un padre, se afectan todos sus hijos**
- Ejemplo: Eliminar Sede 2 → Eliminar Bloques 4,5,6,7 → Eliminar Salones 1,2,3,4

### 3. Orden de Creación
- **Los padres deben existir antes que los hijos**
```
Orden correcto de creación:
1. Empresa + Categoría (independientes)
2. Sede + Elemento (dependen del nivel 0)
3. Bloque (depende de Sede)
4. Salón (depende de Bloque)
5. RecursoSalón (depende de Salón y Elemento)
```

### 4. Orden de Eliminación
- **Eliminar hijos antes que padres**
```
Orden correcto de eliminación:
1. RecursoSalón (nivel más profundo)
2. Salón
3. Bloque
4. Sede
5. Empresa + Elemento + Categoría
```

---

## 🎯 Ejemplos Prácticos

### Ejemplo 1: Crear un nuevo salón

```
Pasos requeridos:
1. ✅ Verificar que existe la Empresa (CORHUILA, ID=1)
2. ✅ Verificar que existe la Sede (Prado Alto, ID=2)
3. ✅ Verificar que existe el Bloque (Bloque C, ID=6)
4. ✅ AHORA podemos crear el Salón:
   INSERT Salón(id=5, nombre="Salón 510", capacidad=40, BloqueId=6)
```

### Ejemplo 2: Asignar recursos a un salón

```
Pasos requeridos:
1. ✅ Verificar que existe el Salón (Salón 508, ID=1)
2. ✅ Verificar que existe el Elemento (Proyector, ID=8)
3. ✅ AHORA podemos crear la asignación:
   INSERT RecursoSalón(id=8, SalonId=1, ElementoId=8, cantidad=2)
```

### Ejemplo 3: Consultar toda la información de un salón

```sql
-- Obtener información completa del Salón 508
SELECT 
  s.nombre AS salon,
  b.nombre AS bloque,
  sd.nombre AS sede,
  e.nombre AS empresa,
  el.nombre AS elemento,
  c.nombre AS categoria,
  rs.cantidad
FROM RecursoSalon rs
  JOIN Salon s ON rs.SalonId = s.id
  JOIN Bloque b ON s.BloqueId = b.id
  JOIN Sede sd ON b.SedeId = sd.id
  JOIN Empresa e ON sd.EmpresaId = e.id
  JOIN Elemento el ON rs.ElementoId = el.id
  JOIN Categoria c ON el.CategoriaId = c.id
WHERE s.id = 1;
```

---

## 🚀 Conclusión

Las dependencias entre entidades garantizan:
- ✅ **Integridad de datos**
- ✅ **Consistencia del sistema**
- ✅ **Trazabilidad completa**
- ✅ **Estructura lógica y escalable**

El sistema está diseñado con dos ramas principales (Empresarial y Recursos) que se conectan a través de **RecursoSalón**, permitiendo una gestión eficiente y organizada.

---

**© 2025 CORHUILA - Sistema de Gestión de Recursos**
