# Pokemon Battle Web

Proyecto web desarrollado con Python y Flask para crear una aplicación web sobre batallas Pokémon.

La aplicación permite consultar una selección de Pokémon, ver sus tipos, estadísticas, ataques y otros datos obtenidos de un fichero JSON.

## Tecnologías utilizadas

- Python
- Flask
- Jinja2
- HTML
- CSS

## Funcionalidades

- Página principal de bienvenida.
- Listado de Pokémon disponibles.
- Información básica de cada Pokémon: nombre, imagen y tipo.
- Vista de detalle de cada Pokémon.
- Clasificación de los Pokémon según su peso.
- Estadísticas representadas mediante barras.
- Lista de ataques de cada Pokémon.
- Navegación entre el listado y las vistas de detalle.

## Estructura del proyecto

```text
Pokemon-Battle-Web/
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── pokemons-cute.json
└── app/
    ├── main.py
    ├── static/
    │   └── css/
    │       └── estilos.css
    └── templates/
        ├── index.html
        ├── pokemons.html
        └── pokemon.html
```

El entorno virtual `venv/` se crea localmente y no se incluye en el repositorio.

## Requisitos

- Python 3
- Git

## Instalación y preparación del entorno

### 1. Clonar el repositorio

```bash
git clone https://github.com/CristinaFR8/Pokemon-Battle-Web.git
```

### 2. Acceder a la carpeta del proyecto

```bash
cd Pokemon-Battle-Web
```

### 3. Crear el entorno virtual

```bash
python -m venv venv
```

### 4. Activar el entorno virtual

En Windows:

```bash
.\venv\Scripts\activate
```

Una vez activado, aparecerá `(venv)` al principio de la terminal.

### 5. Instalar las dependencias

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene las versiones de las dependencias utilizadas por el proyecto, permitiendo recrear el mismo entorno en otra máquina.

## Si no se puede activar el entorno virtual

Si por permisos de la máquina no se puede ejecutar `activate`, se pueden utilizar directamente los ejecutables que se encuentran dentro de `venv`.

Por ejemplo:

```bash
.\venv\Scripts\pip install -r requirements.txt
```

También se puede ejecutar `pip` como módulo de Python:

```bash
.\venv\Scripts\python -m pip install flask
```

Otros comandos de `pip` pueden ejecutarse de la misma forma utilizando los ejecutables de `venv`, por ejemplo:

```bash
.\venv\Scripts\pip freeze
.\venv\Scripts\flask --version
```

## Ejecutar la aplicación

Con el entorno virtual activado:

```bash
python app/main.py
```

Si no se puede activar el entorno virtual:

```bash
.\venv\Scripts\python app/main.py
```

La aplicación se ejecutará en:

```text
http://127.0.0.1:5038/
```

Abrir esa dirección en el navegador para acceder a la aplicación.