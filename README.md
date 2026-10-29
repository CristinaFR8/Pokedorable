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
- Filtrado por el total de estadísticas, mediante un operador de comparación y un valor numérico.
- Selección de un Pokémon para la batalla.
- Vista detallada de cada Pokémon.
- Información sobre sus tipos, características y otros datos.
- Clasificación del Pokémon según su peso.
- Representación gráfica de sus estadísticas.
- Listado de sus ataques.
- Pantalla de combate con un rival aleatorio y cuatro ataques del Pokémon elegido.
- Gestión de la sesión del entrenador y opción para cerrar sesión.

Los datos de los Pokémon se obtienen del fichero `data/pokemons-cute.json`, que se carga al iniciar la aplicación.

## Tecnologías utilizadas

- Python 3
- Flask
- Flask-Session
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

[http://127.0.0.1:5038/](http://127.0.0.1:5038/)

Si no se puede activar el entorno virtual, también se puede ejecutar directamente el Python incluido en `venv`:

```powershell
.\venv\Scripts\python.exe app\main.py
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
- **Filtrado de Pokémon:** permite buscar por nombre, filtrar por tipo y comparar el total de estadísticas mediante los operadores «Igual a», «Mayor que» y «Menor que», introduciendo el valor numérico deseado.

Para acceder al listado es necesario tener un entrenador válido guardado en la sesión. El nombre del entrenador se obtiene de la sesión y no se transmite mediante parámetros de la URL. Los filtros se mantienen mediante parámetros de URL.

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

El identificador del Pokémon elegido se guarda en `session["pokemon"]` y se recupera desde la sesión al acceder a esta página. De esta forma, no es necesario transmitir el identificador mediante un parámetro de URL.

Esta vista requiere que exista un entrenador válido en la sesión. Si no hay un entrenador válido, se redirige al inicio. Si no se encuentra el Pokémon elegido, se redirige al listado.

Esta fase implementa la estructura visual de la batalla. No incluye la lógica de un combate real.

### Cierre de sesión

**Ruta:** `/logout`

Permite cerrar la sesión del entrenador mediante un formulario POST y un botón llamado «Cerrar sesión».

Al pulsar el botón, se eliminan los datos guardados en la sesión mediante `session.clear()` y se redirige al usuario a la página principal.

El botón de cierre de sesión se muestra únicamente cuando existe un entrenador guardado en la sesión.

## Flujo de interacción

1. El usuario accede a la página principal e introduce el nombre del entrenador.
2. El servidor valida que el nombre tenga entre 3 y 15 caracteres y, si es válido, lo guarda en la sesión.
3. El usuario accede al listado de Pokémon, donde puede buscar por nombre, filtrar por tipo, comparar el total de estadísticas y consultar detalles.
4. Al seleccionar un Pokémon válido, su identificador se guarda en la sesión y se accede a la pantalla de batalla con un rival aleatorio y cuatro ataques del Pokémon elegido.
5. Desde la navegación se puede cerrar la sesión del entrenador mediante el botón correspondiente.
6. Al cerrar sesión, se eliminan los datos de la sesión y se vuelve a la página principal.

## Gestión de sesiones

La aplicación utiliza **Flask-Session** para mantener los datos necesarios entre las diferentes peticiones.

La sesión se configura para almacenar los datos en el servidor utilizando el sistema de archivos:

- `SESSION_TYPE`: establece el almacenamiento de sesiones mediante archivos.
- `SESSION_PERMANENT`: se establece en `False` para que la sesión no sea permanente.
- `SESSION_FILE_DIR`: indica el directorio utilizado para almacenar los datos de sesión.

La aplicación utiliza una clave secreta mediante `app.secret_key`, necesaria para la configuración de las sesiones.

### Datos almacenados en la sesión

Se guardan los siguientes datos:

- `session["trainer"]`: almacena el nombre del entrenador cuando el formulario de inicio contiene un nombre válido.
- `session["pokemon"]`: almacena el identificador del Pokémon elegido para la batalla.

Estos datos se almacenan en la sesión para poder recuperarlos en las diferentes rutas sin tener que enviarlos continuamente mediante parámetros de URL.

Los filtros de búsqueda no se guardan en la sesión, ya que se transmiten mediante parámetros de URL. Esto permite mantener los criterios de búsqueda al recargar el listado.

### Protección de las rutas

Las rutas del listado, el detalle y la batalla recuperan el entrenador mediante `session.get("trainer", "")` y comprueban que su nombre tenga entre 3 y 15 caracteres.

Si no existe un entrenador válido en la sesión, se redirige al usuario a la página principal.

La ruta de cierre de sesión utiliza `session.clear()` para eliminar los datos guardados en la sesión. Después de cerrar sesión, las rutas que requieren un entrenador válido vuelven a redirigir al inicio.

## Datos

Los datos utilizados por la aplicación se encuentran en:

`data/pokemons-cute.json`

El fichero se carga al iniciar el servidor y los datos quedan disponibles para las diferentes rutas de la aplicación.

## Plantillas

Las páginas HTML utilizan **Jinja2**.

Se utiliza una plantilla base, `app/templates/base.html`, sobre la que se construyen las diferentes vistas mediante herencia de plantillas.

Las rutas internas y los recursos estáticos se generan utilizando `url_for`.

La plantilla base contiene la navegación común y muestra el botón de cierre de sesión cuando hay un entrenador guardado en la sesión.

## Validación y navegación

Los formularios se validan en el servidor. La aplicación utiliza métodos POST para recibir los datos de los formularios que modifican el estado y parámetros de URL para transmitir los filtros de búsqueda.

El nombre del entrenador y el identificador del Pokémon elegido para la batalla se guardan en la sesión, por lo que no se transmiten mediante parámetros de URL.

La aplicación comprueba que exista un entrenador válido antes de permitir el acceso al listado, al detalle de un Pokémon y a la pantalla de batalla. Al cerrar sesión, se eliminan los datos guardados y el usuario vuelve a la página principal.
