# Actividad: Lectura de Eje X - Eje Y
**Asignatura:** Laboratorio de Programación L401  
**Alumno:** Jerry  
**Institución:** INACAP  

Este proyecto consiste en una aplicación web desarrollada con **Flask** que simula de forma aleatoria la lectura de coordenadas bidimensionales (X, Y) provenientes de un hardware/sensor. La interfaz evalúa matemáticamente el cuadrante activo en base a los signos de los valores generados y renderiza visualmente la información de manera dinámica en una matriz expandida de 4x4 utilizando **Jinja2** y **CSS puro (mediante selectores de ID)**.

---

## ➢ Características de Visualización (Punto 3.4)
* **Matriz Superior 4x4:** Representación expandida completa para mayor precisión de cuadrantes.
* **Estilos Visuales Personalizados:** Diseño ordenado y centrado mediante `border-collapse`, tamaños simétricos de celda (`80px`) y tipografía limpia.
* **Colores por Cuadrante:** Iluminación dinámica utilizando una paleta de colores hexadecimales específica para cada cuadrante activo:
    * Q1 (Verde)
    * Q2 (Rojo)
    * Q3 (Amarillo/Dorado)
    * Q4 (Azul/Cian)

---

## ➢ Estructura del Repositorio (Etapa 1)
El repositorio contiene los siguientes archivos obligatorios modificados para el cumplimiento de la pauta:

* `app.py` -> Lógica del servidor Flask y generación de coordenadas aleatorias.
* `templates/index.html` -> Vista principal con CSS en el <head> e IDs para diseño dinámico (sin clases ni JavaScript).
* `templates/info.html` -> Vista complementaria de información.
* `templates/mensaje.html` -> Vista complementaria de mensajes.
* `capturas/` -> Carpeta con las capturas de pantalla de la visualización.
* `README.md` -> Documentación personalizada del proyecto (Este archivo).

---

## ➢ Instrucciones de Ejecución
1. Navegar a la carpeta del proyecto:
   ```bash
   cd /home/amogos/respaldosgithub/l401-lecturaxy-jerry