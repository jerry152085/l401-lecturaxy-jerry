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

*   **API Extensible:** Diseñado con endpoints limpios que permiten la futura integración de sensores reales mediante peticiones HTTP (POST/GET) sin reestructurar el núcleo del servidor.
*   **Despliegue Ligero y Eficiente:** Optimizado para consumir una cantidad mínima de recursos, ideal para entornos educativos, sistemas embebidos o sistemas operativos ligeros (como AmogOS).
*   **Concurrencia Básica:** Capacidad para manejar las peticiones del dashboard de control y la actualización de los flujos de datos de manera simultánea gracias al motor multihilo de Flask en desarrollo.
* **Página Principal Personal:** Interfaz de desarrollo propio.
* **Simulación de Datos Integrada:** Lógica en segundo plano.
* **Navegación Cruzada:** Menú de navegación integrado.

## Estructura del Proyecto
* `app.py`: Servidor principal.
* `templates/`: Interfaces de usuario.

###  Árbol de Directorios y Componentes

```text
l401-lecturaxy-jerry/
├── capturas/          # Almacenamiento de evidencias, pantallazos y gráficas del sistema.
├── templates/         # Vistas y archivos HTML renderizados por el servidor web Flask.
│   ├── index.html     # Dashboard principal para la visualización de datos X-Y.
│   ├── javier.html    # Módulo/Pestaña adaptada de la interfaz de Javier Salas.
│   └── luis.html      # Módulo/Pestaña adaptada de la interfaz de Luis Viscarra.
├── app.py             # Script principal en Python que inicializa el servidor Flask y la API.
└── README.md          # Documentación técnica del proyecto (este archivo).
## Ejecución del Servidor
Para levantar el servidor, ejecuta:

```bash
python3 app.py
```

## Referencias y Créditos
* **Pestaña /javier:** Adaptada desde el repositorio de Javier Salas ([github.com/javier-sb/l401-lecturaxy](https://github.com/javier-sb/l401-lecturaxy)).
* **Pestaña /luis:** Adaptada desde el repositorio de Luis Alberto Viscarra ([github.com/luisviscarrahellie-ux/l401-lecturaxy-jfpc](https://github.com/luisviscarrahellie-ux/l401-lecturaxy-jfpc)).

* ##  Evidencias de Funcionamiento

> **Nota del desarrollador:** Las imágenes del correcto funcionamiento de la interfaz, las pruebas de comunicación y el despliegue de las curvas en tiempo real se encuentran almacenadas de forma ordenada en la carpeta `/capturas` de esta rama (`main`).
