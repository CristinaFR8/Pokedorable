
# Pokédorable

Aplicación web desarrollada con **Python y Flask** para consultar información sobre diferentes Pokémon, visualizar sus características, filtrarlos y seleccionar uno para una pantalla de combate.

El proyecto forma parte del módulo **Desarrollo Web en Entorno Servidor (DWES)** y utiliza **Jinja2** para generar las páginas HTML a partir de los datos proporcionados en un fichero JSON.

**Autora:** Cristina Fernández  
**Curso:** 2026/27

## Descripción

La aplicación permite consultar una selección de Pokémon a través de diferentes vistas:

- Página principal de bienvenida.
- Formulario para introducir el nombre del entrenador.
- Listado de Pokémon disponibles.
- Búsqueda por nombre y filtrado por tipo.
- Selección de un Pokémon para la batalla.
- Vista detallada de cada Pokémon.
- Información sobre sus tipos, características y otros datos.
- Clasificación del Pokémon según su peso.
- Representación gráfica de sus estadísticas.
- Listado de sus ataques.
- Pantalla de combate con un rival aleatorio y cuatro ataques del Pokémon elegido.

Los datos de los Pokémon se obtienen del fichero `data/pokemons-cute.json`, que se carga al iniciar la aplicación.

## Tecnologías utilizadas

- Python 3
- Flask
- Jinja2
- HTML5
- CSS3
- JSON

## Estructura del proyecto

```text
Pokedorable/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── pokemons-cute.json
└── app/
    ├── main.py
    ├── static/
    │   ├── css/
    │   │   └── estilos.css
    │   └── img/
    │       ├── pokeball.png
    │       ├── superball.png
    │       ├── ultraball.png
    │       └── masterball.png
    └── templates/
        ├── base.html
        ├── index.html
        ├── pokemons.html
        ├── pokemon.html
        └── batalla.html
```

> El entorno virtual `venv/` se crea localmente y no se incluye en el repositorio.

## Requisitos

Para ejecutar el proyecto es necesario tener instalado:

- Python 3
- Git

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/CristinaFR8/Pokedorable.git
```

### 2. Acceder a la carpeta del proyecto

```bash
cd Pokedorable
```

### 3. Crear el entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

En Windows, desde PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Si utilizas Git Bash:

```bash
source venv/Scripts/activate
```

Una vez activado, aparecerá `(venv)` al principio de la terminal.

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

Las dependencias del proyecto están especificadas en `requirements.txt` para facilitar la configuración del entorno.

## Ejecución

Con el entorno virtual activado, ejecuta:

```bash
python app/main.py
```

La aplicación estará disponible en:

http://127.0.0.1:5038/

Si no se puede activar el entorno virtual, también se puede ejecutar directamente el Python incluido en `venv`:

```powershell
.\venv\Scripts\python.exe app\main.py
```

## Vistas de la aplicación

### Página principal

**Ruta:** `/`

Muestra la bienvenida a la aplicación y permite introducir el nombre del entrenador mediante un formulario POST.

El servidor valida que el nombre tenga entre 3 y 15 caracteres. Si no cumple este requisito, se muestra un mensaje de error. Si es válido, se redirige al listado de Pokémon.

### Listado de Pokémon

**Ruta:** `/pokemons`

Muestra los Pokémon disponibles y el nombre del entrenador.

Incluye dos formularios:

- **Selección de Pokémon:** permite introducir el nombre del Pokémon deseado. El servidor comprueba que exista y, si es válido, redirige a la página de batalla.
- **Filtrado de Pokémon:** permite buscar por nombre y filtrar por tipo.

El listado requiere un nombre de entrenador válido. La información del entrenador se transmite mediante parámetros de la URL, sin utilizar sesiones.

### Detalle de un Pokémon

**Ruta:** `/pokemons/<id>/`

Muestra información detallada del Pokémon seleccionado, incluyendo:

- Nombre e imágenes.
- Altura y peso.
- Tipo.
- Clasificación según el peso.
- Estadísticas representadas gráficamente.
- Ataques y sus características.
- Otros datos disponibles en el JSON.

### Página de batalla

**Ruta:** `/battle`

Muestra el Pokémon elegido por el entrenador frente a un rival aleatorio distinto.

La pantalla incluye:

- Nombre del entrenador.
- Nombres e imágenes de ambos Pokémon.
- Puntos de salud de cada contrincante.
- Cuatro ataques seleccionados aleatoriamente entre los disponibles para el Pokémon elegido.
- Tipo, precisión y potencia de cada ataque.

Esta fase implementa la estructura visual de la batalla. No incluye la lógica de un combate real.

## Datos

Los datos utilizados por la aplicación se encuentran en:

`data/pokemons-cute.json`

El fichero se carga al iniciar el servidor y los datos quedan disponibles para las diferentes rutas de la aplicación.

## Plantillas

Las páginas HTML utilizan **Jinja2**.

Se utiliza una plantilla base, `app/templates/base.html`, sobre la que se construyen las diferentes vistas mediante herencia de plantillas.

Las rutas internas y los recursos estáticos se generan utilizando `url_for`.

## Validación y navegación

Los formularios se validan en el servidor. La aplicación utiliza métodos POST para recibir los datos de los formularios y parámetros de URL para transmitir el nombre del entrenador entre las vistas.

No se utilizan sesiones.

