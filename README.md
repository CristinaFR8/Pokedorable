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
- Gestión de la sesión del entrenador y opción para cerrar sesión.

Los datos de los Pokémon se obtienen del fichero `data/pokemons-cute.json`, que es leído por el repositorio de la aplicación.

## Tecnologías utilizadas

- Python 3
- Flask
- Flask-Session
- Flask-WTF
- WTForms
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
    ├── __init__.py
    ├── main.py
    ├── forms/
    │   ├── __init__.py
    │   └── entrenador_form.py
    ├── models/
    │   ├── __init__.py
    │   └── pokemon.py
    ├── repositories/
    │   ├── __init__.py
    │   └── pokemon_repository.py
    ├── routes/
    │   ├── __init__.py
    │   ├── decorators.py
    │   ├── main_routes.py
    │   └── battle_routes.py
    ├── services/
    │   ├── __init__.py
    │   └── pokemon_service.py
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

El entorno virtual `venv/` se crea localmente y no se incluye en el repositorio.

## Arquitectura por capas

El proyecto está organizado siguiendo una arquitectura por capas para separar las responsabilidades de la aplicación.

### Modelos

La carpeta `models/` contiene las clases que representan los elementos del dominio.

El archivo `pokemon.py` define la clase `Pokemon`, que contiene los atributos de cada Pokémon, como su identificador, nombre, altura, peso, estadísticas, imágenes, tipos y ataques.

La representación del modelo se realiza mediante programación orientada a objetos.

### Repositorios

La carpeta `repositories/` contiene las funciones encargadas de acceder a los datos.

El archivo `pokemon_repository.py` lee el fichero JSON, obtiene los datos y crea los objetos `Pokemon` que utiliza el resto de la aplicación.

### Servicios

La carpeta `services/` contiene la lógica de negocio de la aplicación.

El archivo `pokemon_service.py` se encarga de operaciones como:

- Obtener Pokémon.
- Buscar Pokémon por identificador o nombre.
- Filtrar Pokémon por nombre y tipo.
- Traducir los tipos, estadísticas y ataques.
- Obtener los datos necesarios para la Pokédex y el detalle.
- Seleccionar un rival aleatorio.
- Obtener cuatro ataques aleatorios.
- Clasificar los Pokémon según su peso.

### Rutas

La carpeta `routes/` contiene las rutas de Flask, organizadas mediante Blueprints.

Las rutas reciben las peticiones del usuario, utilizan los servicios para obtener los datos necesarios y devuelven las plantillas correspondientes.

También contiene `decorators.py`, que define el decorador `require_entrenador` para proteger las rutas que necesitan un entrenador válido en la sesión.

### Formularios

La carpeta `forms/` contiene los formularios de Flask-WTF.

El archivo `entrenador_form.py` define la clase `EntrenadorForm`, que gestiona el formulario de entrada del entrenador y valida que el nombre tenga entre 3 y 15 caracteres.

### Flujo entre capas

La aplicación sigue este recorrido general:

1. El usuario realiza una petición desde el navegador.
2. La ruta correspondiente recibe la petición.
3. La ruta utiliza el servicio necesario.
4. El servicio solicita los datos al repositorio cuando los necesita.
5. El repositorio lee el JSON y construye los objetos del modelo.
6. El servicio devuelve los datos procesados a la ruta.
7. La ruta envía los datos a la plantilla correspondiente.
8. Jinja2 genera la página HTML que recibe el usuario.

## Blueprints

La aplicación utiliza dos Blueprints, registrados en `main.py`.

### main_bp

Definido en `main_routes.py`.

Se encarga de las rutas relacionadas con la página principal y la gestión del entrenador:

- `/`: página principal y formulario de entrada.
- `/logout`: cierre de sesión.

### battle_bp

Definido en `battle_routes.py`.

Se encarga de las rutas relacionadas con la Pokédex y la selección de Pokémon:

- `/pokemons`: listado y filtrado de Pokémon.
- `/pokemons/<id>/`: detalle de un Pokémon.
- `/battle`: pantalla de combate.

Se han separado en dos Blueprints para organizar las rutas según su responsabilidad: por un lado, la página principal y la gestión del entrenador; por otro, las funcionalidades de consulta de Pokémon y combate.

## Formularios Flask-WTF

La aplicación utiliza Flask-WTF para gestionar el formulario de entrada del entrenador.

El formulario se encuentra definido en `forms/entrenador_form.py` mediante la clase `EntrenadorForm`, que hereda de `FlaskForm`.

Incluye:

- Un campo de texto para introducir el nombre del entrenador.
- Un botón para enviar el formulario.
- Validación mediante `DataRequired` y `Length`.
- Protección CSRF mediante `form.hidden_tag()`.

El nombre debe tener entre 3 y 15 caracteres. Si la validación no se cumple, se muestran los mensajes de error correspondientes.

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

Con el entorno virtual activado, desde la carpeta principal del proyecto ejecuta:

```bash
python -m app.main
```

La aplicación estará disponible en:

http://127.0.0.1:5038/

Si no se puede activar el entorno virtual, también se puede ejecutar directamente el Python incluido en `venv`:

```powershell
.\venv\Scripts\python.exe -m app.main
```

## Vistas de la aplicación

### Página principal

**Ruta:** `/`

Muestra la bienvenida a la aplicación y permite introducir el nombre del entrenador mediante un formulario POST.

El servidor valida que el nombre tenga entre 3 y 15 caracteres. Si no cumple este requisito, se muestra un mensaje de error. Si es válido, el nombre se guarda en la sesión mediante `session["trainer"]` y se redirige al listado de Pokémon.

### Listado de Pokémon

**Ruta:** `/pokemons`

Muestra los Pokémon disponibles y el nombre del entrenador.

Incluye dos formularios:

- **Selección de Pokémon:** permite introducir el nombre del Pokémon deseado. El servidor comprueba que exista y, si es válido, guarda su identificador en la sesión mediante `session["pokemon"]` y redirige a la página de batalla.
- **Filtrado de Pokémon:** permite buscar por nombre y filtrar por tipo. Los filtros se transmiten mediante parámetros de URL.

Para acceder al listado es necesario tener un entrenador válido guardado en la sesión.

### Detalle de un Pokémon

**Ruta:** `/pokemons/<id>/`

Muestra información detallada del Pokémon, incluyendo:

- Nombre e imágenes.
- Altura y peso.
- Tipo.
- Clasificación según el peso.
- Estadísticas representadas gráficamente.
- Ataques y sus características.
- Otros datos disponibles en el JSON.

La clasificación según el peso se calcula en el servicio y se envía a la plantilla para mostrarla.

Esta vista requiere que exista un entrenador válido en la sesión.

### Página de batalla

**Ruta:** `/battle`

Muestra el Pokémon elegido por el entrenador frente a un rival aleatorio distinto.

La pantalla incluye:

- Nombre del entrenador.
- Nombres e imágenes de ambos Pokémon.
- Puntos de salud de cada contrincante.
- Cuatro ataques seleccionados aleatoriamente entre los disponibles para el Pokémon elegido.
- Tipo, precisión y potencia de cada ataque.

El identificador del Pokémon elegido se guarda en `session["pokemon"]` y se recupera desde la sesión al acceder a esta página.

También se guardan el identificador del rival en `session["pokemon_rival"]` y los cuatro ataques en `session["ataques"]`, para mantener los mismos datos al volver a acceder a la pantalla.

Esta fase implementa la estructura visual de la batalla. No incluye la lógica de un combate real.

### Cierre de sesión

**Ruta:** `/logout`

Permite cerrar la sesión del entrenador mediante un formulario POST y un botón llamado «Cerrar sesión».

Al pulsar el botón, se eliminan los datos guardados en la sesión mediante `session.clear()` y se redirige al usuario a la página principal.

El botón de cierre de sesión se muestra únicamente cuando existe un entrenador guardado en la sesión.

## Flujo de interacción

1. El usuario accede a la página principal e introduce el nombre del entrenador.
2. El servidor valida que el nombre tenga entre 3 y 15 caracteres y, si es válido, lo guarda en la sesión.
3. El usuario accede al listado de Pokémon, donde puede buscar por nombre, filtrar por tipo y consultar detalles.
4. Al seleccionar un Pokémon válido, su identificador se guarda en la sesión.
5. Se accede a la pantalla de batalla, donde se obtiene un rival aleatorio y cuatro ataques del Pokémon elegido.
6. El usuario puede volver a la página principal o a la Pokédex sin perder los datos de la sesión.
7. Al seleccionar otro Pokémon, se sustituye la selección anterior y se eliminan los datos del rival y los ataques anteriores.
8. Al cerrar sesión, se eliminan todos los datos guardados y se vuelve a la página principal.

## Gestión de sesiones

La aplicación utiliza **Flask-Session** para mantener los datos necesarios entre las diferentes peticiones.

La sesión se configura para almacenar los datos en el servidor utilizando el sistema de archivos:

- `SESSION_TYPE`: establece el almacenamiento de sesiones mediante archivos.
- `SESSION_PERMANENT`: se establece en `False` para que la sesión no sea permanente.
- `SESSION_FILE_DIR`: indica el directorio utilizado para almacenar los datos de sesión.

La aplicación utiliza una clave secreta mediante `app.secret_key`, necesaria para la configuración de las sesiones y la protección CSRF de Flask-WTF.

### Datos almacenados en la sesión

Se guardan los siguientes datos:

- `session["trainer"]`: almacena el nombre del entrenador.
- `session["pokemon"]`: almacena el identificador del Pokémon elegido.
- `session["pokemon_rival"]`: almacena el identificador del rival del combate.
- `session["ataques"]`: almacena los cuatro ataques seleccionados para el Pokémon elegido.

Estos datos se almacenan en la sesión para poder recuperarlos en las diferentes rutas sin tener que enviarlos continuamente mediante parámetros de URL.

Los filtros de búsqueda no se guardan en la sesión, ya que se transmiten mediante parámetros de URL.

### Protección de las rutas

El decorador `require_entrenador`, definido en `routes/decorators.py`, comprueba que exista un entrenador válido en la sesión y que su nombre tenga entre 3 y 15 caracteres.

Este decorador protege las rutas del listado, el detalle y la batalla.

Si no existe un entrenador válido en la sesión, se redirige al usuario a la página principal.

La ruta de cierre de sesión utiliza `session.clear()` para eliminar los datos guardados en la sesión.

## Datos

Los datos utilizados por la aplicación se encuentran en:

`data/pokemons-cute.json`

El repositorio `pokemon_repository.py` lee este fichero y construye los objetos `Pokemon` que posteriormente utilizan los servicios.

## Plantillas

Las páginas HTML utilizan **Jinja2**.

Se utiliza una plantilla base, `app/templates/base.html`, sobre la que se construyen las diferentes vistas mediante herencia de plantillas.

Las rutas internas y los recursos estáticos se generan utilizando `url_for`.

La plantilla base contiene la navegación común y muestra el botón de cierre de sesión cuando hay un entrenador guardado en la sesión.