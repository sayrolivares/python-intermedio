# python-intermedio
Aquí pondré mis notas de lo que vi en el curso de python de platzi, el curso intermedio.

# Zen de python

El Zen de Python se compone por los principios para escribir tu código de manera clara, sencilla y precisa. Estos son:

* Bello es mejor que feo: Pyhton es estéticamente superior a cualquier otro lenguaje de programación. Al momento de escribir código, es mejor que sea de manera limpia y estética.
* Explícito es mejor que implícito: Hacer más fácil que las otras personas entiendan el código.
* Simple es mejor que complejo: Es mejor tener una implementación simple, que ocupe pocas lineas de código y sea entendible, a que sea una larga y complicada.
* Complejo es mejor que complicado: Si tenemos que extendernos en la implementación y hacerla más compleja para que el código si se entienda, esto es mejor que hacerlo simple y mal.
* Plano es mejor que anidado: El anidamiento es cuando tenemos un bloque de código dentro de otro bloque de código (dependiendo de este). Esto se nota en Python por la identación, nos quedarían estos bloques muy corridos a la derecha. Es mejor evitar el anidamiento, y hacer las cosas de manera plana.
* Espaciado es mejor que denso: Por la identación de Python (sus sangrías), este principio se nos hace imposible de esquivar. El código inevitablemente es espaciado.
* La legibilidad es importante: Es importante que otros programadores puedan entender lo que estamos escribiendo. Esto hace más fáciles las cosas cuando trabajemos con otros en los proyectos.
* Los casos especiales no son lo suficientemente especiales cpmo para romper las reglas (sin embargo, la practicidad le gana a la pureza): Siempre que podamos respetar estas reglas que nos plantea Python, es mejor así. Sin embargo, si por el hecho de hacer un código muy puro o muy ‘Pythonista’, este pierde legibilidad, es mejor ser más prácticos y romper o saltearnos algunas de estas reglas para que el código sea más eficiente. Por lo tanto, llegado el momento debermos decidir si es mejor hacer las cosas de manera pura o práctica.
* Los errores nunca deberían pasar silenciosamente (a menos que se silencien explícitamente): Manejar los erroes es fundamental. Cada error nos dice algo y hay que prestarle atención. A menos que seas capaz de silenciar un error explícitamente, aunque para esto hay que tener criterio.
* Frente a la ambiguedad, evitar la tentación de adivinar: Nuestro código debería solamente tener una interpretación. Si en un contexto significa algo, y en otro otra cosa, es mejor que lo revisemos y busquemos una solución.
* Debería haber una, y preferiblemente sola, una manera obvia de hacerlo. (A pesar de que esa manera no sea obvia a menos que seas holandés): Esto hace referencia al creador de Python "Guido van Rossum", que de manera muy inteligente encontrar las soluciones precisas a los problemas, y deberíamos imitarlo.
* Ahora es mejor que nunca: Es mejor desarrollar nuestra solución cuánto antes, no dejarlo para mañana o para mas adelante.
* A pesar de que nunca es muchas veces mejor que ahora mismo: Si por hacer las cosas ya y tenemos poco tiempo, si es mejor dejarlo para después y no hacerlo apurado y mal.
* Si la implementación es díficil de explicar, es una mala idea, y si es fácil de explicar, es una buena idea: Si somos capaces de explicar nuestra implementación a otros desarrolladores paso a paso, es una buena idea. En cambio si no podemos hacerlo, significa que ni nosotros entendemos la implementación y deberíamos repensar nuestra forma de encarar la solución.
* Los espacios de nombres son una gran idea, ¡Tengamos más de esos! (namespaces): Es el nombre que se ha indicado luego de la palabra import, es decir la ruta (namespace) del módulo. (Lo veremos a profundidad más adelante).

# ¿Qué es la documentación?

La documentación es una pieza de información que nos explica cómo funciona un lenguaje, cuáles son las pequeñas partes que hacen que todo funcione como tiene que hacerlo.

## 10 beneficios de leer la documentación de Python

Consultar informacion clara y directa
Tener ejemplo de los mismos desarrolladores
Referencias de todas las caracteristicas y funcionalidades en un solo lugar
Conocer los nuevos features de nuevas actualizaciones
Conocer el modo de empleo de versiones anteriores
Aprender a manejar correctamente las herramientas
Que contienen los modulos integrados dentro de python
Como manejar los modulos
Manejo y uso de frameworks
Ser autodidacta

# ¿Qué es un entorno virtual?

Un entorno virtual es un entorno Python en el que el intérprete Python, las bibliotecas y los scripts instalados en él están aislados de los instalados en otros entornos virtuales, y (por defecto) cualquier biblioteca instalada en un «sistema» Python, es decir, uno que esté instalado como parte de tu sistema operativo.
Un entorno virtual es un árbol de directorios que contiene archivos ejecutables de Python y otros archivos que indican que es un entorno virtual.

Sería una catástrofe tener que instalar y actualizar módulos para cada proyecto cuidando que ninguno se rompa, porque fácilmente podrías actualizar un módulo que, para un proyecto funcione, pero para otro deje de funcionar, es por eso que se crea el concepto de entornos virtuales.

Sin entorno virtual:

![alt text](https://static.platzi.com/media/user_upload/Screenshot%20from%202021-04-06%2015-17-31-98f9a6fa-3e6c-4353-9644-31a4e7208737.jpg "Representación de una computadora sin entorno virtual ejecutando varios proyectos")

Con entorno virtual:

![alt text](https://static.platzi.com/media/user_upload/Screenshot%20from%202021-04-06%2015-10-22-1804c0b6-79d2-40bd-aced-f859f86c5309.jpg "Representación de una computadora con entorno virtual ejecutando un proyecto en varios entornos")

# El primer paso profesional: creación de un entorno virtual

## Creando un ambiente virtual con VENV

Creación de ambiente Virtual:

*python -m venv "nombre_del_ambiente"* (sin comillas)

Usualmente el nombre del ambiente virtual es venv.

## Activación del ambiente virtual:

Unix o MacOS:
source venv/bin/activate

## Desactivar el ambiente virtual:

deactivate

## Crear un alias en linux/mac:

alias nombre-alias="comando"

*alias avenv=“source venv/bin/activate”* para activar el ambiente virtual

# Instalación de dependencias con pip

PIP es Package Installer for Python, este viene de fábrica, esto es un módulo que está pensado para instalar otros módulos que no están dentro de Python.

PIP es una herramienta que va acompañada al entorno virtual y no deberíamos usarla fuera del mismo.

## Módulos populares:

* Requests
* BeautifulSoup4
* Pandas
* Numpy
* Pytest

## Instalando módulos

Una vez en el entorno virtual (ya activado), cuando instalemos dependencias o módulos con PIP no vamos a tener problemas porque estos módulos se van a instalar en este proyecto en particular y no en toda la computadora.

*pip freeze*: muestra los módulos que tienes instalados en determinado entorno virtual.

*pip install pandas*: instalamos pandas, un módulo para ciencias de datos.

*Una vez lo instalemos, un mensaje de advertencia podría aparecer diciendo que pip está desactualizado. Simplemente copiamos el mensaje desde la ocmilla ' hasta la otra ' y pegamos en la terminal, y voilá.*

## Para compartir estas dependencias con alguien más para que pueda correr nuestro proyecto

Colocamos:

pip freeze > requirements.txt

Este archivo guarda tus dependencias para poder compartirlo con otras personas

La otra persona debería ejecutar el comando:

pip install -r requirements.txt

Así las dependencias se instalan auitomáticamente.
