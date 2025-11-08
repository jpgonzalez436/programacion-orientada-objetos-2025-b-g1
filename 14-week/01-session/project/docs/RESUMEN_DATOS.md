# 📊 Resumen del Sistema de Gestión - CORHUILA

## 🎯 Análisis de Datos Iniciales del Diagrama

Este documento presenta un análisis detallado de los datos iniciales planteados en el diagrama de clases y las dependencias entre entidades.

---

## 📋 Estructura de Entidades y Dependencias

### 1️⃣ CATEGORÍA (Entidad Independiente)
**Propósito:** Clasificar elementos según su tipo

| ID | Nombre | Descripción |
|----|--------|-------------|
| 1 | Computadores | Dispositivos electrónicos |
| 2 | Muebles | Elementos de mobiliario |
| 3 | Videobeam | Dispositivos de proyección |
| 4 | Aire acondicionado | Dispositivos de climatización |
| 5 | Tablero | Elementos de mobiliario |
| 6 | Telón de proyección | Elementos de mobiliario |

**Dependencias:**
- ✅ No depende de ninguna otra entidad
- ➡️ Es referenciada por: **Elemento**

---

### 2️⃣ ELEMENTO (Depende de Categoría)
**Propósito:** Inventario de recursos disponibles

| ID | Nombre | Descripción | CategoríaId |
|----|--------|-------------|-------------|
| 1 | Computador HP | PC de clase HP + Cable de poder + mouse + teclado | 1 |
| 2 | Computador Dell | PC de clase Dell + Cargador | 1 |
| 3 | Computador Mac | PC de clase Mac + Cargador | 1 |
| 4 | Silla plástica | Silla de plástico color azul | 2 |
| 5 | Mesa madera | Mesa de madera para oficina | 2 |
| 6 | Computador HP | PC de clase HP + cargador + cable de red | 1 |
| 7 | Silla plástica | Silla de plástico color negro | 2 |
| 8 | Proyector Epson | Proyector de alta definición | 3 |
| 9 | Aire acondicionado LG | Aire acondicionado portátil | 4 |
| 10 | Tablero blanco | Tablero blanco para marcadores | 5 |
| 11 | Telón de proyección | Telón de proyección eléctrico | 6 |

**Dependencias:**
- ⬅️ Depende de: **Categoría** (N:1)
- ➡️ Es referenciado por: **RecursoSalón**

**Análisis por Categoría:**
- Categoría 1 (Computadores): 4 elementos
- Categoría 2 (Muebles): 3 elementos
- Categoría 3 (Videobeam): 1 elemento
- Categoría 4 (Aire acondicionado): 1 elemento
- Categoría 5 (Tablero): 1 elemento
- Categoría 6 (Telón): 1 elemento

---

### 3️⃣ EMPRESA (Entidad Independiente)
**Propósito:** Información institucional

| ID | Nombre | NIT | Dirección |
|----|--------|-----|-----------|
| 1 | Corporación Universitaria del Huila - CORHUILA | 900123456-7 | Calle 123 |

**Dependencias:**
- ✅ No depende de ninguna otra entidad
- ➡️ Es referenciada por: **Sede**

---

### 4️⃣ SEDE (Depende de Empresa)
**Propósito:** Campus universitarios

| ID | Nombre | Dirección | EmpresaId |
|----|--------|-----------|-----------|
| 1 | Sede Quirinal | Calle 123 #45-67 | 1 |
| 2 | Sede Prado Alto | Carrera 8 #9-10 | 1 |

**Dependencias:**
- ⬅️ Depende de: **Empresa** (N:1)
- ➡️ Es referenciada por: **Bloque**

**Análisis:**
- Total sedes: 2
- Empresa CORHUILA tiene 2 sedes

---

### 5️⃣ BLOQUE (Depende de Sede)
**Propósito:** Edificaciones dentro de cada sede

| ID | Nombre | SedeId | Sede |
|----|--------|--------|------|
| 1 | Bloque A | 1 | Quirinal |
| 2 | Bloque B | 1 | Quirinal |
| 3 | Bloque C | 1 | Quirinal |
| 4 | Bloque A | 2 | Prado Alto |
| 5 | Bloque B | 2 | Prado Alto |
| 6 | Bloque C | 2 | Prado Alto |
| 7 | Laboratorios | 2 | Prado Alto |

**Dependencias:**
- ⬅️ Depende de: **Sede** (N:1)
- ➡️ Es referenciado por: **Salón**

**Análisis por Sede:**
- Sede Quirinal: 3 bloques
- Sede Prado Alto: 4 bloques

---

### 6️⃣ SALÓN (Depende de Bloque)
**Propósito:** Espacios académicos

| ID | Nombre | Capacidad | BloqueId | Bloque | Sede |
|----|--------|-----------|----------|--------|------|
| 1 | Salón 508 | 30 | 6 | Bloque C | Prado Alto |
| 2 | Salón 411 | 30 | 6 | Bloque C | Prado Alto |
| 3 | Salón 409 | 30 | 6 | Bloque C | Prado Alto |
| 4 | Salón 208 | 30 | 5 | Bloque B | Prado Alto |

**Dependencias:**
- ⬅️ Depende de: **Bloque** (N:1)
- ➡️ Es referenciado por: **RecursoSalón**

**Análisis:**
- Total salones: 4
- Capacidad total: 120 personas
- Capacidad promedio: 30 personas/salón
- Todos en Sede Prado Alto
- Bloque C: 3 salones
- Bloque B: 1 salón

---

### 7️⃣ RECURSOSALÓN (Entidad Puente - Depende de Salón y Elemento)
**Propósito:** Asignación de elementos a salones

| ID | SalónId | Salón | ElementoId | Elemento | Cantidad |
|----|---------|-------|------------|----------|----------|
| 1 | 1 | Salón 508 | 6 | Computador HP | 30 |
| 2 | 1 | Salón 508 | 7 | Silla plástica | 30 |
| 3 | 1 | Salón 508 | 5 | Mesa madera | 31 |
| 4 | 1 | Salón 508 | 8 | Proyector Epson | 1 |
| 5 | 1 | Salón 508 | 9 | Aire acondicionado LG | 1 |
| 6 | 1 | Salón 508 | 10 | Tablero blanco | 1 |
| 7 | 1 | Salón 508 | 11 | Telón de proyección | 1 |

**Dependencias:**
- ⬅️ Depende de: **Salón** (N:1)
- ⬅️ Depende de: **Elemento** (N:1)
- ✅ Es la entidad integradora del sistema

**Análisis:**
- Total asignaciones: 7 registros
- Solo el Salón 508 tiene recursos asignados
- Total elementos asignados: 95 unidades
  - 30 computadores
  - 30 sillas
  - 31 mesas
  - 4 equipos tecnológicos (proyector, aire, tablero, telón)

---

## 🔗 Mapa Completo de Dependencias

```
┌─────────────────────────────────────────────────────────────────┐
│                    FLUJO DE DEPENDENCIAS                        │
└─────────────────────────────────────────────────────────────────┘

RAMA EMPRESARIAL (Estructura Física):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Empresa (1)
    ↓ tiene (1:*)
Sede (2)
    ↓ contiene (1:*)
Bloque (7)
    ↓ incluye (1:*)
Salón (4)
    ↓
    ↓ dispone de (1:*)
    ↓
┌───────────────┐
│ RecursoSalón  │ ← ENTIDAD PUENTE
│   (7 registros)│
└───────────────┘
    ↑
    ↑ es parte de (1:*)
    ↑
Elemento (11)
    ↑ pertenece a (N:1)
Categoría (6)

RAMA DE RECURSOS (Inventario):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📊 Estadísticas Generales

### Distribución de Datos
- **Empresas:** 1
- **Sedes:** 2
- **Bloques:** 7 (3 en Quirinal + 4 en Prado Alto)
- **Salones:** 4 (todos en Prado Alto)
- **Categorías:** 6
- **Elementos:** 11
- **Recursos Asignados:** 7 asignaciones (95 unidades totales)

### Capacidad Instalada
- **Capacidad total:** 120 personas
- **Salones equipados:** 1 de 4 (25%)
- **Elementos en uso:** 7 de 11 (64%)

---

## ✅ Integridad Referencial

### Validación de Relaciones

**Categoría → Elemento:**
- ✅ Todas las categorías (1-6) existen
- ✅ Todos los elementos (1-11) referencian categorías válidas
- ✅ No hay elementos huérfanos

**Empresa → Sede:**
- ✅ La empresa ID 1 existe
- ✅ Ambas sedes (1-2) referencian la empresa correctamente

**Sede → Bloque:**
- ✅ Ambas sedes (1-2) existen
- ✅ Todos los bloques (1-7) referencian sedes válidas
- ✅ No hay bloques huérfanos

**Bloque → Salón:**
- ✅ Los bloques 5 y 6 existen
- ✅ Todos los salones referencian bloques válidos
- ✅ No hay salones huérfanos

**Salón + Elemento → RecursoSalón:**
- ✅ El salón 1 existe
- ✅ Todos los elementos (5-11) existen
- ✅ No hay referencias inválidas

---

## 🎯 Conclusiones

### Fortalezas del Modelo
1. **Integridad:** Todas las relaciones son válidas
2. **Coherencia:** Los datos siguen el patrón del diagrama UML
3. **Trazabilidad:** Cada registro tiene IDs únicos
4. **Escalabilidad:** Estructura permite crecimiento

### Observaciones
1. **Datos concentrados:** Solo Prado Alto tiene salones activos
2. **Recursos limitados:** Solo Salón 508 tiene asignaciones
3. **Oportunidad:** Potencial para equipar más salones

### Recomendaciones
1. Asignar recursos a los demás salones (411, 409, 208)
2. Activar salones en Sede Quirinal
3. Distribuir elementos según necesidades

---

**Documento generado automáticamente**  
Sistema de Gestión de Recursos - CORHUILA  
© 2025
