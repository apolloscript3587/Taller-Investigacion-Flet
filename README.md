# Taller de investigación: Flet

## ¿Qué es Flet?

[Flet](https://flet.dev/) es un framework de Python para crear interfaces gráficas y aplicaciones web, de escritorio y móviles usando controles listos para usar. Permite trabajar desde Python sin tener que programar por separado la interfaz en HTML, CSS o JavaScript.

## Requisitos

- Python 3.10 o una versión posterior.
- Conexión a internet para instalar las dependencias.

Comprueba tu versión:

```bash
python --version
```

En algunas instalaciones de Linux el comando es `python3 --version`.

## Instalación y ejecución

Se recomienda usar un entorno virtual para no mezclar las dependencias del proyecto con las del sistema.

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

### Linux o macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python main.py
```

Si tu distribución de Linux bloquea la instalación global de paquetes, activa el entorno virtual antes de instalar. No es necesario usar `sudo pip` ni forzar la instalación en el Python del sistema.

## Componentes gráficos principales

| Componente | Función |
| --- | --- |
| `Text` | Mostrar texto. |
| `Button` | Crear botones interactivos. |
| `TextField` | Recibir texto del usuario. |
| `Image` | Mostrar imágenes. |
| `Container` | Agrupar y dar formato a otros controles. |
| `Row` | Organizar controles horizontalmente. |
| `Column` | Organizar controles verticalmente. |
| `Icon` | Mostrar iconos. |
| `AlertDialog` | Mostrar ventanas de diálogo. |
| `SnackBar` | Mostrar mensajes temporales. |

## Eventos e interacción

Flet trabaja mediante eventos. Por ejemplo, la propiedad `on_click` de un botón permite asociar una función que se ejecuta cuando el usuario hace clic. En este proyecto, los botones llaman a los métodos `incrementar()`, `disminuir()` y `reiniciar()`.

Después de cambiar el valor de los controles, se llama a `page.update()` para reflejar los cambios en la interfaz.

## Ejemplo desarrollado: contador interactivo

El archivo `main.py` contiene una aplicación que permite:

- Aumentar el contador.
- Disminuir el contador.
- Reiniciar el valor a cero.
- Mostrar un mensaje según la acción realizada.

### ¿Cómo se aplica la programación orientada a objetos?

La clase `ContadorApp` agrupa los datos y el comportamiento de la aplicación:

- **Atributos:** `page` guarda la página de Flet y `contador` almacena el valor actual.
- **Componentes:** los textos y botones se crean como atributos de la clase.
- **Métodos:** `incrementar()`, `disminuir()` y `reiniciar()` modifican el contador.
- **Encapsulamiento:** la lógica y los controles relacionados se mantienen organizados dentro de una misma clase.

La función `main(page)` crea el objeto `ContadorApp` y conecta la clase con la página que proporciona Flet.

## Ventajas y limitaciones frente a Tkinter

**Ventajas de Flet**
- Permite desarrollar aplicaciones para varias plataformas.
- Incluye controles modernos y una estructura visual flexible.
- Facilita la programación orientada a eventos.
- Permite organizar el proyecto con clases y objetos.
- No requiere conocimientos de desarrollo frontend para comenzar.

**Limitaciones de Flet**
- Requiere instalar sus dependencias y, para algunas plataformas, herramientas adicionales.
- Puede consumir más recursos que una interfaz sencilla hecha con Tkinter.
- El empaquetado y la distribución pueden requerir configuración específica según el sistema operativo.

**En comparación:** Tkinter viene incluido habitualmente con las instalaciones estándar de Python y es útil para interfaces de escritorio sencillas. Flet resulta conveniente cuando se busca una interfaz moderna y la posibilidad de llevar la aplicación a web o dispositivos móviles.

## Estructura del proyecto

```text
Taller-Investigacion-Flet/
├── main.py
├── requirements.txt
├── README.md
└── evidencia/
    └── (captura de la aplicación en ejecución)
```

## Publicación en GitHub

1. Crea un repositorio en GitHub.
2. Sube los archivos del proyecto, incluyendo `main.py`, `README.md` y `requirements.txt`.
3. No subas la carpeta `.venv`; contiene dependencias locales y no es necesaria para ejecutar el proyecto.
4. Agrega una captura real de la aplicación funcionando en la carpeta `evidencia/`.

## Fuentes consultadas

- [Documentación oficial de Flet](https://flet.dev/docs/).
- [Instalación de Flet](https://flet.dev/docs/getting-started/installation/).
- [Introducción a Flet](https://flet.dev/docs/).
