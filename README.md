# Visualización de Datos X-Y (Servidor Flask)

Proyecto desarrollado para la asignatura **Desarrollo de Software para Hardware (DCSH01)** en INACAP.

Esta aplicación implementa un servidor web basado en Flask, diseñado para recibir y procesar flujos de datos de los sensores.

###  Especificaciones Técnicas del Sistema

*   **Protocolo de Comunicación:** REST API sobre HTTP (Mapeo de datos bidimensionales mediante endpoints dedicados).
*   **Procesamiento de Datos:**
    *   **Frecuencia de Muestreo:** Diseñado para soportar flujos continuos de datos en tiempo real (lecturas X e Y provenientes del hardware).
    *   **Formato de Carga (Payload):** Transmisión estructurada en formato **JSON** (ej. `{"x": valor, "y": valor}`).
*   **Entorno de Ejecución:** Servidor local ligero (`localhost` / `127.0.0.1`) corriendo sobre el puerto `5000` mediante el microframework Flask en entorno embebido/Linux.
*   **Modularidad del Frontend:** Renderizado dinámico e interactivo de curvas y coordenadas para el análisis gráfico de las señales.
## Características Principales
* **Página Principal Personal:** Interfaz de desarrollo propio.
* **Simulación de Datos Integrada:** Lógica en segundo plano.
* **Navegación Cruzada:** Menú de navegación integrado.

## Estructura del Proyecto
* `app.py`: Servidor principal.
* `templates/`: Interfaces de usuario.

## Ejecución del Servidor
Para levantar el servidor, ejecuta:

```bash
python3 app.py
```

## Referencias y Créditos
* **Pestaña /javier:** Adaptada desde el repositorio de Javier Salas ([github.com/javier-sb/l401-lecturaxy](https://github.com/javier-sb/l401-lecturaxy)).
* **Pestaña /luis:** Adaptada desde el repositorio de Luis Alberto Viscarra ([github.com/luisviscarrahellie-ux/l401-lecturaxy-jfpc](https://github.com/luisviscarrahellie-ux/l401-lecturaxy-jfpc)).

* ## 📸 Evidencias de Funcionamiento

> **Nota del desarrollador:** Las imágenes del correcto funcionamiento de la interfaz, las pruebas de comunicación y el despliegue de las curvas en tiempo real se encuentran almacenadas de forma ordenada en la carpeta `/capturas` de esta rama (`main`).
