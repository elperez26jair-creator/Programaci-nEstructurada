# Actividad 3 — Configuración de un Entorno de Desarrollo Integrado (IDE)

**Alumno:** Perez Lugo Jair  
**Grupo:** 2IRD-G1 
**Fecha:** 16-01-2026
**Unidad:** 1

---

## 1. IDE seleccionado
- **IDE:** Visual Studio Code
- **Versión:** 1.86.x
- **Sistema operativo:** Windows 10 / 11 (64 bits)

---

## 2. Justificación
- **Criterio 1: Multiplataforma y gratuito.** VS Code funciona en Windows, Linux y macOS, sin costo de licencia.
- **Criterio 2: Extensibilidad.** Dispone de un amplio ecosistema de extensiones para múltiples lenguajes y herramientas.
- **Criterio 3: Integración con Git.** Incluye control de versiones integrado, facilitando el uso de Git y GitHub.

---

## 3. Requisitos previos
- **Requisito 1:** Equipo con sistema operativo Windows 10 o superior.
- **Requisito 2:** Conexión a Internet para descarga de software y extensiones.
- **Permisos:** Permisos de administrador para instalar aplicaciones.

---

## 4. Instalación (paso a paso)
1. Acceder al sitio oficial de Visual Studio Code.
2. Descargar el instalador para Windows (64 bits).
3. Ejecutar el instalador y aceptar los términos de licencia.
4. Seleccionar opciones recomendadas (agregar VS Code al PATH).
5. Finalizar la instalación y abrir el IDE.

### 4.1 Verificación
- **¿Cómo comprobé que funciona?**  
  Se ejecutó Visual Studio Code correctamente y se creó un archivo de prueba.
- **Evidencia:**  
  Apertura exitosa del IDE y creación de un archivo `main.txt` sin errores.

---

## 5. Configuración inicial

### 5.1 Ajustes básicos
- Configuración del idioma en español.
- Activación del guardado automático de archivos.

### 5.2 Extensiones / plugins

| Extensión/Plugin | Función | Por qué |
|---|---|---|
| GitLens | Mejora la gestión de Git | Facilita el seguimiento de cambios y commits |
| Markdown All in One | Soporte para Markdown | Mejora la edición del reporte |
| Code Runner | Ejecutar código rápidamente | Permite pruebas rápidas de programas |

### 5.3 Herramientas adicionales
- **Compilador/intérprete:** Git Bash (incluye Git)
- **Prueba:** Ejecución del comando `git --version` desde la terminal integrada.

---

## 6. Configuración de Git y GitHub

1. Instalación de Git desde el sitio oficial.
2. Configuración de usuario:
   ```bash
   git config --global user.name "Perez Lugo Jair"
   git config --global user.email "elperez26jair@gmai.com"


