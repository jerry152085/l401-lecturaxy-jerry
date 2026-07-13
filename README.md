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

##  Referencias y Créditos

Este repositorio forma parte de un ecosistema de desarrollo colaborativo para la asignatura. La integración de módulos externos tiene como objetivo evaluar la compatibilidad, modularidad e intercambio de datos entre diferentes propuestas de interfaces web.

###  Repositorios Integrados y Co-Autores
*   **Módulo /javier:** Interfaz adaptada y sincronizada desde el repositorio base de **Javier Salas**. Implementa metodologías específicas de captura visual de señales.
    *   *Origen:* [github.com/javier-sb/l401-lecturaxy](https://github.com/javier-sb/l401-lecturaxy)
*   **Módulo /luis:** Componente y lógica de navegación cruzada adaptada desde el repositorio de **Luis Alberto Viscarra**. Aporta robustez al flujo de rutas secundarias.
    *   *Origen:* [github.com/luisviscarrahellie-ux/l401-lecturaxy-jfpc](https://github.com/luisviscarrahellie-ux/l401-lecturaxy-jfpc)

###  Institución y Contexto Académico
*   **Institución:** INACAP (Universidad Tecnológica de Chile).
*   **Asignatura:** Desarrollo de Software para Hardware (DCSH01).
*   **Docente Evaluador:** Integrado en el programa oficial de revisión de código y competencias de sistemas embebidos.

*   ##  Evidencias de Funcionamiento
*   ###  Captura 1: Dashboard Principal
*   <img width="1452" height="618" alt="Captura de pantalla 2026-07-13 035236" src="https://github.com/user-attachments/assets/08ffbbc6-920f-4b51-bfa7-453f2d76fb7e" />

 Captura 2: Módulo de Javier
<img width="1435" height="765" alt="Captura de pantalla 2026-07-13 021143" src="https://github.com/user-attachments/assets/80534e16-125e-443e-9051-e2cb49ce2093" />

###  Captura 3: Módulo de Luis
<img width="1900" height="726" alt="Captura de pantalla 2026-07-13 021228" src="https://github.com/user-attachments/assets/b92de605-23a8-43f6-a854-79d7ed61d70d" />



