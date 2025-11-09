# 📊 Sistema de Gestión de Países

## 📝 Descripción del Programa

**Sistema de Gestión de Países** es una aplicación de consola desarrollada en Python que permite administrar y analizar información de países de todo el mundo. El programa trabaja con datos almacenados en formato CSV y ofrece funcionalidades completas de CRUD (Crear, Leer, Actualizar) junto con herramientas avanzadas de análisis y visualización.

### ✨ Características Principales

- **Gestión de Datos**: Carga, agrega y actualiza información de países desde archivos CSV
- **Búsqueda y Filtrado**: Localiza países por nombre, continente, población o superficie
- **Algoritmos de Ordenamiento**: Implementación manual de métodos de ordenamiento:
  - Método Burbuja (Bubble Sort)
  - Método Inserción (Insertion Sort)
- **Análisis Estadístico**: Calcula promedios, extremos y distribución por continentes
- **Interfaz Intuitiva**: Menú interactivo con validaciones exhaustivas
- **Persistencia de Datos**: Guarda cambios permanentemente en archivo CSV

### 🗂️ Estructura de Datos

Cada país se almacena con los siguientes atributos:
- **Nombre**: Identificador único del país
- **Población**: Número de habitantes (entero positivo)
- **Superficie**: Área territorial en km² (entero positivo)
- **Continente**: América, Europa, Asia, África, Oceanía o Antártida

---

## 🚀 Instrucciones de Uso

### Requisitos Previos

- **Python 3.x** instalado en el sistema
- Archivo `paises.csv` en la carpeta `data/` con el formato:
  ```csv
  nombre,poblacion,superficie,continente
  Argentina,45000000,2780400,America
  España,47000000,505990,Europa
  ```

### Ejecución del Programa

1. Abre una terminal o consola en el directorio del proyecto
2. Ejecuta el comando:
   ```bash
   python main.py
   ```
3. Sigue las instrucciones en pantalla

### 📋 Menú Principal

El programa presenta las siguientes opciones:

```
1. Cargar/recargar archivo CSV
2. Agregar un pais
3. Actualizar datos de un pais
4. Buscar un pais
5. Filtrar paises
6. Ordenar paises
7. Mostrar estadisticas
8. Guardar cambios en el CSV
9. Salir del programa
```

### 🔧 Funcionalidades Detalladas

#### 1️⃣ Cargar/Recargar Archivo CSV
- Carga los datos desde `data/paises.csv`
- Muestra todos los países en formato tabla
- Debe ejecutarse antes de cualquier otra operación

#### 2️⃣ Agregar un País
- Solicita: nombre, población, superficie y continente
- Valida que el nombre no exista previamente
- Valida que población y superficie sean números positivos
- Los cambios no son permanentes hasta guardar (opción 8)

#### 3️⃣ Actualizar Datos de un País
- Busca el país por nombre exacto
- Permite modificar población, superficie (no continente ni nombre)
- Mantiene valores actuales si se deja en blanco

#### 4️⃣ Buscar un País
- Búsqueda por coincidencia parcial o exacta
- No distingue mayúsculas/minúsculas
- Muestra todos los resultados coincidentes

#### 5️⃣ Filtrar Países
Tres tipos de filtros disponibles:
- **Por continente**: Lista países de un continente específico
- **Por rango de población**: Establece mínimo y máximo de habitantes
- **Por rango de superficie**: Establece mínimo y máximo de km²

#### 6️⃣ Ordenar Países
- Elige el campo: nombre, población o superficie
- Selecciona algoritmo: burbuja o inserción
- Define orden: ascendente o descendente
- Muestra resultado sin modificar datos originales

#### 7️⃣ Mostrar Estadísticas
Calcula y visualiza:
- País con mayor y menor población
- Promedios de población y superficie
- Distribución de países por continente

#### 8️⃣ Guardar Cambios
- Guarda todos los cambios realizados en el archivo CSV
- Solicita confirmación antes de guardar
- Sobrescribe el archivo original

#### 9️⃣ Salir del Programa
- Cierra la aplicación
- **⚠️ ADVERTENCIA**: Cambios no guardados se perderán

---

## 💡 Ejemplos de Entradas y Salidas

### Ejemplo 1: Agregar un País

**Entrada del Usuario:**
```
Opción del menú: 2
Nombre del pais: Japón
Poblacion: 125000000
Superficie (km2): 377975
Continente: Asia
```

**Salida del Programa:**
```
OK: El pais 'Japón' ha sido agregado correctamente.
ADVERTENCIA: Recuerda guardar los cambios en el CSV (opcion 8).
```

---

### Ejemplo 2: Buscar un País

**Entrada del Usuario:**
```
Opción del menú: 4
Ingresa el nombre o parte del nombre: arg
```

**Salida del Programa:**
```
================================================================================
  Resultados de busqueda: 'arg'
================================================================================
Nombre               Poblacion       Superficie (km2)     Continente     
--------------------------------------------------------------------------------
Argentina            45,000,000      2,780,400            America        
--------------------------------------------------------------------------------
Total: 1 pais(es)
================================================================================
```

---

### Ejemplo 3: Filtrar por Rango de Población

**Entrada del Usuario:**
```
Opción del menú: 5
Selecciona una opcion: 2
Poblacion minima: 40000000
Poblacion maxima: 50000000
```

**Salida del Programa:**
```
================================================================================
  Paises con poblacion entre 40,000,000 y 50,000,000
================================================================================
Nombre               Poblacion       Superficie (km2)     Continente     
--------------------------------------------------------------------------------
Argentina            45,000,000      2,780,400            America        
España               47,000,000      505,990              Europa         
--------------------------------------------------------------------------------
Total: 2 pais(es)
================================================================================
```

---

### Ejemplo 4: Ordenar Países por Población

**Entrada del Usuario:**
```
Opción del menú: 6
Selecciona una opcion: 2
Algoritmo de ordenamiento: 1
Orden: 2
```

**Salida del Programa:**
```
================================================================================
  Paises ordenados por poblacion (Burbuja, Descendente)
================================================================================
Nombre               Poblacion       Superficie (km2)     Continente     
--------------------------------------------------------------------------------
China                1,400,000,000   9,596,961            Asia           
India                1,380,000,000   3,287,263            Asia           
Estados Unidos       331,000,000     9,833,517            America        
...
================================================================================
```

---

### Ejemplo 5: Mostrar Estadísticas

**Entrada del Usuario:**
```
Opción del menú: 7
```

**Salida del Programa:**
```
============================================================
ESTADISTICAS DE LOS PAISES
============================================================

Pais con MAYOR poblacion:
   China: 1,400,000,000 habitantes

Pais con MENOR poblacion:
   Vaticano: 800 habitantes

Promedio de poblacion: 38,000,000 habitantes
Promedio de superficie: 2,500,000 km2

Cantidad de paises por continente:
   America: 35 pais(es)
   Europa: 44 pais(es)
   Asia: 48 pais(es)
   Africa: 54 pais(es)
   Oceania: 14 pais(es)
   Antartida: 0 pais(es)
============================================================
```

---

### Ejemplo 6: Intentar Agregar País Duplicado

**Entrada del Usuario:**
```
Opción del menú: 2
Nombre del pais: Argentina
```

**Salida del Programa:**
```
ERROR: Ya existe un pais con ese nombre.
```

---

### Ejemplo 7: Validación de Datos Inválidos

**Entrada del Usuario:**
```
Opción del menú: 2
Nombre del pais: Brasil
Poblacion: -1000
```

**Salida del Programa:**
```
ERROR: La poblacion debe ser un numero entero positivo.
```

---

## 👥 Participación de los Integrantes

Este proyecto fue desarrollado utilizando la metodología de **Pair Programming** (Programación en Pareja), una práctica ágil donde dos desarrolladores trabajan juntos en la misma estación de trabajo, colaborando en tiempo real.

### 🤝 Equipo de Desarrollo

<table>
<tr>
<td width="50%" align="center">

### 🔍 **Alejandro Daniel Maure**

Responsable de implementar todas las funciones de **búsqueda y filtrado**:
- Búsqueda por nombre con coincidencia parcial
- Filtrado por continente
- Filtrado por rango de población
- Filtrado por rango de superficie
- Validaciones de entrada de datos

</td>
<td width="50%" align="center">

### 📈 **Lautaro Ezequiel Mansilla**

Responsable de desarrollar todos los **métodos de ordenamiento**:
- Algoritmo de Burbuja (Bubble Sort)
- Algoritmo de Inserción (Insertion Sort)
- Ordenamiento por múltiples campos
- Orden ascendente y descendente
- Optimización de rendimiento

</td>
</tr>
</table>

### 🌟 Metodología de Trabajo

Aunque cada desarrollador tuvo áreas de especialización, el trabajo se realizó de manera **colaborativa y sincronizada**:

- **Sesiones conjuntas**: Ambos programadores trabajaron simultáneamente en el código
- **Revisión cruzada**: Cada función fue revisada y mejorada por ambos integrantes
- **Un solo commit**: Todo el código se integró en un único commit consolidado, reflejando la naturaleza unificada del desarrollo
- **Conocimiento compartido**: Ambos desarrolladores comprenden la totalidad del sistema

### 💻 División de Responsabilidades

```
📦 main.py
 ┣ 🔍 Módulo de Filtros          → Alejandro Daniel Maure
 ┃  ┣ buscar_pais_por_nombre()
 ┃  ┣ filtrar_por_continente()
 ┃  ┣ filtrar_por_poblacion()
 ┃  ┗ filtrar_por_superficie()
 ┃
 ┣ 📈 Módulo de Ordenamiento     → Lautaro Ezequiel Mansilla
 ┃  ┣ ordenar_burbuja()
 ┃  ┗ ordenar_insercion()
 ┃
 ┗ 🤝 Módulos Compartidos        → Colaboración conjunta
    ┣ Manejo de archivos CSV
    ┣ Validaciones de datos
    ┣ Interfaz de usuario
    ┣ Estadísticas
    ┗ Menú principal
```

### 🎯 Resultado del Pair Programming

Esta metodología permitió:
- ✅ Código más limpio y mantenible
- ✅ Menos errores y bugs
- ✅ Mejor diseño de soluciones
- ✅ Transferencia de conocimiento continua
- ✅ Mayor calidad del producto final

---

## 📄 Notas Adicionales

- El programa incluye validaciones exhaustivas para prevenir errores de entrada
- Todos los algoritmos de ordenamiento fueron implementados manualmente sin usar funciones predefinidas de Python
- Los cambios realizados en memoria no afectan el archivo CSV hasta ejecutar la opción "Guardar cambios"
- La interfaz utiliza formateo de números con separadores de miles para mejor legibilidad

---

## 📚 Archivos Relacionados

- `main.py` - Código fuente principal
- `data/paises.csv` - Base de datos de países

---

<div align="center">

**Trabajo Práctico Integrador - Programación 1**  
*Noviembre 2025*

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Completado-success.svg)]()

</div>

