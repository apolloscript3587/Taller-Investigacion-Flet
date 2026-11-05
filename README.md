# Flet

Es un framework de código abierto para Python que te permite crear interfaces gráficas de usuario (GUI) y aplicaciones interactivas para web, escritorio (Windows, macOS, Linux) y móviles usando únicamente Python, sin necesidad de escribir código en HTML, CSS o JavaScript.

## Instrucciones de Instalación y Ejecución

### Tener Python 3.10 o posterior instalado

Se puede comprobar con el siguiente comando en terminal tanto para Windows como para Linux `python --version`
(En algunas distribuciones de Linux se usa `python3 --version`)

### Instalación

Se puede instalar con el siguiente comando en terminal tanto para Windows como para Linux `pip install flet`
(Se recomienda hacer dentro de la carpeta del proyecto)

### Principales Componentes Gráficos

| Componente |	Función |
| :--- | ---: |
| Text | Mostrar textos en pantalla |
| Button | Crear botones interactivos |
| TextField |	Permitir introducir información |
| Image |	Mostrar imágenes |
| Container |	Agrupar y organizar elementos |
| Row |	Organizar elementos horizontalmente |
| Column | Organizar elementos verticalmente |
| Icon | Mostrar iconos | 
| AlertDialog |	Mostrar ventanas de diálogo |
| SnackBar | Mostrar mensajes temporales |

### Eventos del Usuario

Flet utiliza funciones y métodos que se ejecutan cuando el usuario realiza una acción.
Por ejemplo, un botón puede utilizar la propiedad `on_click` para detectar un clic del mouse.

### Ventajas y Limitaciones Frente a Tkinter

Ventajas de Flet:
- Permite desarrollar aplicaciones multiplataforma.
- Tiene componentes gráficos modernos.
- Facilita la programación orientada a eventos.
- Permite organizar el código utilizando clases y objetos.
- No exige conocimientos de desarrollo frontend.

Limitaciones de Flet:
- Necesita instalar dependencias adicionales.
- Puede consumir más recursos que una interfaz sencilla desarrollada con Tkinter.
- Algunas características dependen de la plataforma donde se ejecute.
- El empaquetado para dispositivos móviles requiere configuraciones adicionales.







