# Pokédorable

Aplicación web desarrollada con Python y Flask para consultar una selección de Pokémon, buscar y filtrar la Pokédex, ver fichas detalladas y preparar una pantalla de combate.

**Autora:** Cristina Fernández  
**Módulo:** Desarrollo Web en Entorno Servidor (DWES)  
**Curso:** 2026/27

## Funcionalidades

- Página de bienvenida con un formulario para introducir el nombre del entrenador.
- Validación del nombre: entre 3 y 15 caracteres.
- Listado de Pokémon con búsqueda por nombre y filtro por tipo.
- Ficha individual con imágenes, altura, peso, tipos, estadísticas y ataques.
- Selección de un Pokémon y pantalla de combate con un rival distinto elegido aleatoriamente y cuatro ataques del Pokémon seleccionado.
- Sesión para conservar el entrenador y el Pokémon elegido durante la navegación.
- Cierre de sesión mediante una petición POST.

La pantalla de combate es una representación visual: no implementa las reglas de un combate real.

## Tecnologías

- Python 3
- Flask
- Flask-Session
- Flask-WTF y WTForms
- Jinja2
- HTML5 y CSS3
- JSON

## Estructura del proyecto

```text
Pokedorable/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── forms/
│   │   ├── __init__.py
│   │   └── entrenador_form.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── pokemon.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── pokemon_repository.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── decorators.py
│   │   ├── main_routes.py
│   │   └── battle_routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── pokemon_service.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── pokemons.html
│   │   ├── pokemon.html
│   │   └── batalla.html
│   └── static/
│       ├── css/
│       │   └── estilos.css
│       └── img/
│           ├── pokeball.png
│           ├── superball.png
│           ├── ultraball.png
│           └── masterball.png
├── data/
│   └── pokemons-cute.json
├── requirements.txt
└── README.md
```

El entorno virtual (`venv/`) y los archivos temporales de sesión no se incluyen en el repositorio.

## Arquitectura por capas

El proyecto separa las responsabilidades para que las rutas no tengan que leer directamente el JSON ni concentrar toda la lógica:

- **Presentación — `app/routes/` y `app/templates/`:** las rutas reciben las peticiones, llaman a los servicios y seleccionan la plantilla que se devuelve. Las plantillas Jinja muestran los datos.
- **Negocio — `app/services/pokemon_service.py`:** busca Pokémon, aplica los filtros por nombre y tipo y prepara las traducciones y selecciones necesarias para las vistas.
- **Persistencia — `app/repositories/pokemon_repository.py`:** lee el fichero JSON y construye los objetos `Pokemon`. El acceso al fichero queda aislado en el repositorio.
- **Dominio — `app/models/pokemon.py`:** la clase `Pokemon` representa cada Pokémon como un objeto, tal como exige el enunciado.
- **Formularios — `app/forms/`:** `EntrenadorForm` define el formulario de entrada mediante Flask-WTF, con validadores y token CSRF.

El flujo habitual es **ruta → servicio → repositorio/modelo**. El repositorio no renderiza plantillas y el servicio no depende de Flask ni gestiona peticiones HTTP. Si en el futuro cambiase el formato de los datos, el punto principal que habría que adaptar sería el repositorio.

El JSON se carga una vez cuando se importa el repositorio durante el arranque de la aplicación. La ruta del archivo se calcula a partir de la ubicación del propio módulo, por lo que no depende del directorio actual de la terminal.

## Blueprints y organización de las rutas

Se utilizan dos blueprints, registrados en `app/main.py`:

- **`main_bp` — `app/routes/main_routes.py`:** contiene la página de inicio (`/`) y el cierre de sesión (`/logout`). Son las rutas relacionadas con la entrada y la sesión general del entrenador.
- **`battle_bp` — `app/routes/battle_routes.py`:** contiene el listado (`/pokemons`), el detalle (`/pokemons/<int:id>/`) y la pantalla de batalla (`/battle`). Estas rutas forman el flujo de consulta y selección de Pokémon.

Esta separación mantiene juntas las rutas que cumplen funciones relacionadas y satisface el requisito de disponer, como mínimo, de dos blueprints. Para construir las URL internas se utiliza `url_for`, incluyendo el nombre del blueprint en el endpoint, por ejemplo `battle.listado_pokemons`.

## Instalación y ejecución

Se necesita Python 3 y Git.

1. Clona el repositorio y entra en su carpeta:

   ```bash
   git clone https://github.com/CristinaFR8/Pokedorable.git
   cd Pokedorable
   ```

2. Crea y activa un entorno virtual.

   En Windows PowerShell:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

   En Git Bash:

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   ```

3. Instala las dependencias:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Arranca la aplicación desde la carpeta raíz del proyecto:

   ```bash
   python -m app.main
   ```

5. Abre [http://127.0.0.1:5038/](http://127.0.0.1:5038/) en el navegador.

Se utiliza `python -m app.main` porque el proyecto está organizado como un paquete y usa imports absolutos como `app.routes...`. La aplicación dispone de una clave secreta de desarrollo predeterminada para facilitar las pruebas locales; para un despliegue real debe configurarse `SECRET_KEY` mediante una variable de entorno y no utilizar una clave pública o conocida.

## Vistas y flujo de interacción

### Inicio — `/`

Muestra la bienvenida y dos Pokémon de ejemplo. El formulario envía el campo `trainer` mediante POST. `EntrenadorForm`, definido como una clase de Flask-WTF, comprueba que el campo no esté vacío y que tenga entre 3 y 15 caracteres. La plantilla incluye `form.hidden_tag()` para enviar el token CSRF. Si los datos son válidos, el nombre se guarda en la sesión y se redirige a la Pokédex.

### Listado — `/pokemons`

Requiere que haya un entrenador válido en la sesión. Permite buscar Pokémon por nombre y filtrarlos por tipo. Estos filtros se envían mediante parámetros de URL porque describen la búsqueda actual y resulta útil poder recargarla o compartirla. Otro formulario permite elegir un Pokémon por su nombre; si existe, su identificador se guarda en la sesión y se redirige a la batalla.

### Detalle — `/pokemons/<id>/`

Muestra los datos del Pokémon indicado por su identificador: imágenes, altura, peso, tipos, estadísticas gráficas y ataques. Si no existe ese identificador, la ruta devuelve una respuesta 404. Se necesita una sesión de entrenador para acceder.

### Batalla — `/battle`

Recupera de la sesión el Pokémon seleccionado. Si todavía no hay rival, el servicio elige uno aleatorio distinto y se conserva su identificador para mantener la misma pantalla al recargar. También se seleccionan cuatro ataques aleatorios del Pokémon elegido y se guardan en la sesión. La página muestra los dos Pokémon, sus puntos de salud y los datos de los ataques; no ejecuta un combate real.

### Cierre de sesión — `/logout`

El botón aparece cuando hay un entrenador en la sesión. Envía una petición POST que elimina los datos de sesión mediante `session.clear()` y vuelve a la página principal.

## Gestión de sesión

Se utiliza Flask-Session con almacenamiento en archivos (`SESSION_TYPE = "filesystem"`) y sesiones no permanentes.

- `session["trainer"]`: nombre del entrenador. Se conserva para identificar al usuario durante la navegación y proteger las vistas que requieren haber pasado por el inicio.
- `session["pokemon"]`: identificador del Pokémon seleccionado, necesario para que la batalla recupere la elección sin pasarla por la URL.
- `session["pokemon_rival"]`: identificador del rival elegido, para que no cambie al recargar la pantalla.
- `session["ataques"]`: los cuatro ataques seleccionados, para que la selección se mantenga al recargar la pantalla.

Los filtros no se guardan en la sesión: se envían por parámetros de URL y pueden modificarse desde la propia dirección. Al cerrar sesión, `session.clear()` elimina los datos anteriores.

## Datos y plantillas

Los datos están en `data/pokemons-cute.json`. El repositorio lo lee una vez al arrancar y crea objetos de la clase `Pokemon` a partir de sus campos. Las plantillas usan herencia Jinja: `base.html` contiene la estructura compartida, la navegación y el pie de página; las demás plantillas rellenan sus bloques. Las rutas y los recursos estáticos se generan con `url_for`.

