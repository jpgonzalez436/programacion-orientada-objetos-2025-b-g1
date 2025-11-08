# Sistema de Gestión de Recursos - CORHUILA

## 📋 Descripción del Proyecto

Sistema web para la gestión y administración de recursos e infraestructura de la Corporación Universitaria del Huila (CORHUILA). Permite visualizar y controlar la información de empresas, sedes, bloques, salones, categorías, elementos y sus respectivas asignaciones.

## 🏗️ Estructura del Proyecto

```
project/
├── application/
│   ├── index.html              # Página principal
│   ├── src/
│   │   └── css/
│   │       └── styles.css      # Estilos CSS del sistema
│   └── view/
│       ├── dashboard.html      # Panel de control
│       ├── empresa.html        # Vista de empresa
│       ├── sede.html          # Vista de sedes
│       ├── bloque.html        # Vista de bloques
│       ├── salon.html         # Vista de salones
│       ├── categoria.html     # Vista de categorías
│       ├── elemento.html      # Vista de elementos
│       └── recurso-salon.html # Vista de recursos por salón
└── architecture/
    └── diagram_class.wsd      # Diagrama de clases UML
```

## 📊 Modelo de Datos

### Entidades Principales

#### 1. **Gestión Empresarial** (Jerarquía organizacional)
- **Empresa** → Sede → Bloque → Salón

#### 2. **Gestión de Recursos** (Inventario)
- **Categoría** → Elemento → RecursoSalón

#### 3. **Entidad Integradora**
- **RecursoSalón** (Conecta Salón con Elemento)

### Relaciones y Dependencias

```
┌─────────────────────────────────────────────────────────┐
│         GESTIÓN EMPRESARIAL (Estructura Física)         │
├─────────────────────────────────────────────────────────┤
│  Empresa (1) ──→ Sede (*) ──→ Bloque (*) ──→ Salón (*) │
└─────────────────────────────────────────────────────────┘
                              ↓
                      ┌───────────────┐
                      │ RecursoSalón  │ ← Entidad Puente
                      └───────────────┘
                              ↑
┌─────────────────────────────────────────────────────────┐
│          GESTIÓN DE RECURSOS (Inventario)               │
├─────────────────────────────────────────────────────────┤
│         Categoría (1) ──→ Elemento (*) ──→              │
└─────────────────────────────────────────────────────────┘
```

## 📦 Datos Iniciales del Sistema

### Empresa (1 registro)
- **ID: 1** - Corporación Universitaria del Huila - CORHUILA
  - NIT: 900123456-7
  - Dirección: Calle 123

### Sedes (2 registros)
- **ID: 1** - Sede Quirinal (Calle 123 #45-67)
- **ID: 2** - Sede Prado Alto (Carrera 8 #9-10)

### Bloques (7 registros)
**Sede Quirinal:**
- ID: 1 - Bloque A
- ID: 2 - Bloque B
- ID: 3 - Bloque C

**Sede Prado Alto:**
- ID: 4 - Bloque A
- ID: 5 - Bloque B
- ID: 6 - Bloque C
- ID: 7 - Laboratorios

### Salones (4 registros)
- **ID: 1** - Salón 508 (Capacidad: 30, Bloque C)
- **ID: 2** - Salón 411 (Capacidad: 30, Bloque C)
- **ID: 3** - Salón 409 (Capacidad: 30, Bloque C)
- **ID: 4** - Salón 208 (Capacidad: 30, Bloque B)

### Categorías (6 registros)
1. Computadores - Dispositivos electrónicos
2. Muebles - Elementos de mobiliario
3. Videobeam - Dispositivos de proyección
4. Aire acondicionado - Dispositivos de climatización
5. Tablero - Elementos de mobiliario
6. Telón de proyección - Elementos de mobiliario

### Elementos (11 registros)
1. Computador HP (Categoría: 1)
2. Computador Dell (Categoría: 1)
3. Computador Mac (Categoría: 1)
4. Silla plástica azul (Categoría: 2)
5. Mesa madera (Categoría: 2)
6. Computador HP (Categoría: 1)
7. Silla plástica negra (Categoría: 2)
8. Proyector Epson (Categoría: 3)
9. Aire acondicionado LG (Categoría: 4)
10. Tablero blanco (Categoría: 5)
11. Telón de proyección (Categoría: 6)

### Recursos por Salón (7 asignaciones)
**Salón 508:**
1. 30 Computadores HP (Elemento ID: 6)
2. 30 Sillas plásticas negras (Elemento ID: 7)
3. 31 Mesas de madera (Elemento ID: 5)
4. 1 Proyector Epson (Elemento ID: 8)
5. 1 Aire acondicionado LG (Elemento ID: 9)
6. 1 Tablero blanco (Elemento ID: 10)
7. 1 Telón de proyección (Elemento ID: 11)

## 🎯 Funcionalidades

### Navegación por Entidades
- ✅ **Dashboard**: Vista general con estadísticas
- ✅ **Empresa**: Información institucional
- ✅ **Sedes**: Listado de campus universitarios
- ✅ **Bloques**: Edificaciones por sede
- ✅ **Salones**: Espacios académicos
- ✅ **Categorías**: Clasificación de recursos
- ✅ **Elementos**: Inventario completo
- ✅ **Recursos por Salón**: Asignaciones específicas

### Visualización de Dependencias
Cada vista HTML muestra:
- **Datos principales** de la entidad
- **Relaciones con otras entidades** (padres e hijos)
- **IDs de referencia** para trazabilidad
- **Enlaces de navegación** entre entidades relacionadas
- **Estadísticas y resúmenes** relevantes

## 🎨 Características de Diseño

- **Responsive Design**: Adaptable a diferentes dispositivos
- **Menú de Navegación**: Con dropdowns para fácil acceso
- **Tarjetas Informativas**: Resumen visual de datos
- **Tablas Detalladas**: Información completa en formato tabular
- **Código de Colores**: Identificación visual por sección
- **Jerarquía Visual**: Clara presentación de dependencias

## 🚀 Cómo Usar

1. Abrir `index.html` en un navegador web
2. Navegar por el menú principal
3. Explorar las diferentes entidades
4. Seguir los enlaces para ver las relaciones entre datos

## 📚 Tecnologías Utilizadas

- **HTML5**: Estructura de las páginas
- **CSS3**: Estilos y diseño responsive
- **Arquitectura MVC**: Separación de vistas y lógica

## 🔍 Notas Importantes

### Relaciones Clave:
- Cada **Elemento** pertenece a una **Categoría** (N:1)
- Cada **Sede** pertenece a una **Empresa** (N:1)
- Cada **Bloque** pertenece a una **Sede** (N:1)
- Cada **Salón** pertenece a un **Bloque** (N:1)
- **RecursoSalón** conecta **Salón** con **Elemento** (N:1:1)

### Integridad de Datos:
- Todos los IDs son únicos por entidad
- Las relaciones mantienen integridad referencial
- Los datos de ejemplo son consistentes con el diagrama UML

## 👨‍💻 Desarrollo

**Proyecto Académico**  
Programación Orientada a Objetos 2025-B-G1  
Corporación Universitaria del Huila - CORHUILA

---

**© 2025 CORHUILA - Todos los derechos reservados**