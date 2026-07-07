# Visualización de Datos X-Y (Servidor Flask)

Proyecto desarrollado para la asignatura **Desarrollo de Software para Hardware (DCSH01)** en INACAP.

Esta aplicación implementa un servidor web basado en Flask corriendo sobre AmogOS, diseñado para recibir y procesar flujos de datos de los ejes X e Y provenientes de los sensores de un dispositivo móvil (o mediante simulación local por TCP). El sistema se encarga de procesar los datos en tiempo real y desplegarlos en interfaces visuales dinámicas utilizando plantillas HTML y Jinja2.

## Características Principales
* **Página Principal Personal:** Interfaz de desarrollo propio orientada al control central de la aplicación y el monitoreo prioritario de las variables de los sensores.
* **Simulación de Datos Integrada:** Lógica en segundo plano para garantizar la disponibilidad de datos de los ejes X e Y en cualquier entorno de red.
* **Navegación Cruzada:** Menú de navegación integrado en todas las pestañas para permitir el desplazamiento fluido entre las distintas representaciones visuales del laboratorio.

## Estructura del Proyecto
* `app.py`: Servidor principal en Flask con la lógica de enrutamiento y simulación de datos.
* `templates/`: Carpeta que contiene las interfaces de usuario.
  * `index.html`: Vista de la página principal (Desarrollo personal).
  * `javier.html`: Vista complementaria (Visualización alternativa).
  * `luis.html`: Vista complementaria (Visualización alternativa).

## Ejecución del Servidor

Para levantar el entorno del laboratorio localmente, ejecuta el siguiente comando en la terminal:

```bash
python3 app.py
---

## Referencias y Créditos
En conformidad con los requerimientos de la pauta del laboratorio respecto al trabajo colaborativo, se deja constancia de que las pestañas de visualización secundaria integradas en este repositorio fueron adaptadas a partir de los aportes y diseños originales de los siguientes compañeros de equipo:

* **Pestaña /javier:** Adaptada desde el repositorio de **Javier Salas** (github.com/javier-sb/l401-lecturaxy).
* **Pestaña /luis:** Adaptada desde el repositorio de **Luis Alberto Viscarra Hellie** (github.com/luisviscarrahellie-ux/l401-lecturaxy-jfpc).
