# Actividad 2 — Reporte de Buenas Prácticas y Documentación de Código (Java y Python)

**Alumno:** Perez Lugo Jair
**Grupo:** 2IRD-G1
**Fecha:** 14-01-2026  
**Unidad:** 1

---

## 1. Objetivo del reporte
- Aplicar buenas prácticas de codificación enfocadas específicamente en los lenguajes **Java y Python**, considerando legibilidad, mantenibilidad y calidad del software.
- Analizar estándares y herramientas de documentación utilizados comúnmente en Java y Python para producir código profesional.

## 2. Buenas prácticas de codificación

### 2.1 Nombres de variables
**Reglas generales (Java y Python):**
- Usar nombres descriptivos y significativos.
- Evitar abreviaturas ambiguas.
- Mantener consistencia con la convención del lenguaje.

**Convenciones por lenguaje:**
- **Java:** camelCase para variables y métodos, PascalCase para clases.
- **Python:** snake_case para variables y funciones, PascalCase para clases.

**Ejemplo:**
- Java incorrecto: `int x;`
- Java correcto: `int totalAlumnos;`
- Python incorrecto: `x = 0`
- Python correcto: `total_alumnos = 0`

### 2.2 Comentarios
**Cuándo comentar:**
- Para explicar lógica compleja.
- Para documentar métodos, funciones y clases.
- Para describir parámetros y valores de retorno.

**Qué evitar:**
- Comentarios redundantes.
- Comentarios obsoletos.
- Uso excesivo de comentarios en código autoexplicativo.

### 2.3 Estructura del código
**Indentación:**
- Java: bloques definidos por llaves `{}` con indentación consistente.
- Python: la indentación es obligatoria y define los bloques de código.

**Modularidad:**
- Java: uso de métodos y clases.
- Python: uso de funciones y módulos.

**Evitar duplicidad:**
- Aplicar el principio DRY (*Don't Repeat Yourself*) en ambos lenguajes.

## 3. Documentación del código

### 3.1 Estándares
**Estándares elegidos:**
- **Java:** Javadoc.
- **Python:** Docstrings según PEP 257.

**Elementos recomendados:**
- Descripción general.
- Parámetros.
- Valor de retorno.
- Excepciones (Java) o errores esperados (Python).

### 3.2 Herramientas / enfoque
**README / generadores / extensiones:**
- README.md en Markdown.
- **Java:** Javadoc (generación automática de documentación).
- **Python:** Sphinx y pydoc.
- Extensiones de IDE como IntelliJ IDEA y VS Code.

**Ventajas:**
- Mejor comprensión del código.
- Facilitan el mantenimiento.
- Permiten el trabajo colaborativo.

## 4. Ejemplos prácticos

### 4.1 Antes / Después (Ejemplo 1 – Java)

**Antes:**
```txt
int a;
a = b + c;
```

**Después:**
```txt
int sumaCalificaciones;
sumaCalificaciones = calificacionParcial + calificacionFinal;
```

### 4.2 Antes / Después (Ejemplo 2 – Python)

**Antes:**
```txt
if e==1:
 print("ok")
```

**Después:**
```txt
if estado == ACTIVO:
    print("Proceso completado correctamente")
```

### 4.3 Ejemplo de documentación

**Java (Javadoc):**
```txt
/**
 * Calcula el promedio de calificaciones de un alumno.
 *
 * @param sumaCalificaciones Suma total de las calificaciones.
 * @param numeroMaterias Número de materias cursadas.
 * @return Promedio final del alumno.
 */
public double calcularPromedio(double sumaCalificaciones, int numeroMaterias) {
    return sumaCalificaciones / numeroMaterias;
}
```

**Python (Docstring):**
```txt
def calcular_promedio(suma_calificaciones, numero_materias):
    """
    Calcula el promedio de calificaciones de un alumno.

    :param suma_calificaciones: Suma total de las calificaciones.
    :param numero_materias: Número de materias cursadas.
    :return: Promedio final del alumno.
    """
    return suma_calificaciones / numero_materias
```

## 5. Recomendaciones finales
- Respetar siempre las convenciones propias de Java y Python.
- Documentar métodos y funciones desde el inicio del desarrollo.
- Usar herramientas automáticas de documentación.

## 6. Fuentes consultadas
1. Robert C. Martin, *Clean Code*.
2. Documentación oficial de Java – Javadoc.
3. Python Enhancement Proposals (PEP 8 y PEP 257).

---


