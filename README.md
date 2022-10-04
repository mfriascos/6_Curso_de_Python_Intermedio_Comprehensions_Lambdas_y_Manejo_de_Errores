# 6_Curso_de_Python_Intermedio_Comprehensions_Lambdas_y_Manejo_de_Errores

**Curso intermedio de Python**

<p align="center"><img width=35% src="./Pictures/python_logo.png"></p>

**List**

- [El Zen de Python](#el-zen-de-python)
- [¿Qué es la Documentación?](#¿qué-es-la-documentación)
- [¿Qué es un Entorno Virtual?](#¿qué-es-un-entorno-virtual)
- [El Priner Paso Profesional: Creación de un entorno Virtual](#el-primer-paso-profesional-creación-de-un-entorno-virtual)
- [Instalación de Dependencias con PIP (Package Installer for Python)](#instalación-de-dependencias-con-pip-package-installer-for-python)
    - [Módulos Populares](#módulos-populares)
    - [Resumen PIP](#resumen-pip)
- [List Comprehensions](#list-comprehensions)
- [Dictionary Comprehensions](#dictionary-comprehensions)
- [Funciones Anónimas (Lambda Functions)](#funciones-anónimas-lambda-functions)
- [High Order Functions: Filter, map y reduce](#high-order-functions-filter-map-y-reduce)
    - [Uso con list comprehensions Filter](#uso-con-list-comprehensions-filter)
    - [Uso con Filter](#uso-con-filter)
    - [Uso con List Comprehensions map](#uso-con-list-comprehensions-map)
    - [Uso con Map](#uso-con-map)
    - [Uso con for reduce](#uso-con-for-reduce)
    - [Uso con Reduce](#uso-con-reduce)
- [Proyecto: Filtrando Datos](#proyecto-filtrando-datos)
- [Los Errores en el Código](#los-errores-en-el-código)
    - [Tipos de Errores](#tipos-de-errores)
- [Debugging](#debugging)
- [Manejo de Excepciones](#manejo-de-excepciones)
- [Assert Statements (Afirmaciones en Python)](#assert-statements-afirmaciones-en-python)




# El Zen de Python 

El Zen de Python se compone por los principios para escribir tu código de manera clara, sencilla y precisa. Estos son:

* **Bello es mejor que feo:**
Pyhton es estéticamente superior a cualquier otro lenguaje de programación. Al momento de escribir código, es mejor que sea de manera limpia y estética.
* **Explícito es mejor que implícito:**
Hacer más fácil que las otras personas entiendan el código.
* **Simple es mejor que complejo:**
Es mejor tener una implementación simple, que ocupe pocas lineas de código y sea entendible, a que sea una larga y complicada.
* **Complejo es mejor que complicado:**
Si tenemos que extendernos en la implementación y hacerla más compleja para que el código si se entienda, esto es mejor que hacerlo simple y mal.
* **Plano es mejor que anidado:**
El anidamiento es cuando tenemos un bloque de código dentro de otro bloque de código (dependiendo de este). Esto se nota en Python por la identación, nos quedarían estos bloques muy corridos a la derecha.
Es mejor evitar el anidamiento, y hacer las cosas de manera plana.
* **Espaciado es mejor que denso:**
Por la identación de Python (sus sangrías), este principio se nos hace imposible de esquivar. El código inevitablemente es espaciado.
* **La legibilidad es importante:**
Es importante que otros programadores puedan entender lo que estamos escribiendo. Esto hace más fáciles las cosas cuando trabajemos con otros en los proyectos.
* **Los casos especiales no son lo suficientemente especiales cpmo para romper las reglas (sin embargo, la practicidad le gana a la pureza):**
Siempre que podamos respetar estas reglas que nos plantea Python, es mejor así. Sin embargo, si por el hecho de hacer un código muy puro o muy ‘Pythonista’, este pierde legibilidad, es mejor ser más prácticos y romper o saltearnos algunas de estas reglas para que el código sea más eficiente. Por lo tanto, llegado el momento debermos decidir si es mejor hacer las cosas de manera pura o práctica.
* **Los errores nunca deberían pasar silenciosamente (a menos que se silencien explícitamente):**
Manejar los erroes es fundamental. Cada error nos dice algo y hay que prestarle atención. A menos que seas capaz de silenciar un error explícitamente, aunque para esto hay que tener criterio.
* **Frente a la ambiguedad, evitar la tentación de adivinar:**
Nuestro código debería solamente tener una interpretación. Si en un contexto significa algo, y en otro otra cosa, es mejor que lo revisemos y busquemos una solución.
* **Debería haber una, y preferiblemente sola, una manera obvia de hacerlo. (A pesar de que esa manera no sea obvia a menos que seas holandés):**
Esto hace referencia al creador de Python ''Guido van Rossum", que de manera muy inteligente encontrar las soluciones precisas a los problemas, y deberíamos imitarlo.
* **Ahora es mejor que nunca:**
Es mejor desarrollar nuestra solución cuánto antes, no dejarlo para mañana o para mas adelante.
* **A pesar de que nunca es muchas veces mejor que ahora mismo:**
Si por hacer las cosas ya y tenemos poco tiempo, si es mejor dejarlo para después y no hacerlo apurado y mal.
* **Si la implementación es díficil de explicar, es una mala idea, y si es fácil de explicar, es una buena idea:**
Si somos capaces de explicar nuestra implementación a otros desarrolladores paso a paso, es una buena idea. En cambio si no podemos hacerlo, significa que ni nosotros entendemos la implementación y deberíamos repensar nuestra forma de encarar la solución.
* **Los espacios de nombres son una gran idea, ¡Tengamos más de esos! (namespaces):**
Es el nombre que se ha indicado luego de la palabra import, es decir la ruta (namespace) del módulo. (Lo veremos a profundidad más adelante).

# ¿Qué es la Documentación? 

**La documentación es la biblia de cualquier programador.**

No puedes aspirar a aprender un lenguaje si no lees documentación. Sé que muchas personas se saltan eso porque piensan “ufff, es mucho texto, se ve feo”, etc. Pero es la documentación quien nos va a decir exactamente cómo funciona el lenguaje (y cualquier tecnología). No hay un solo desarrollador profesional que no lea documentación.

¡Y claro!, con esto no quiero decir que tengas que estar metido en la documentación siempre, pero quiero que sepas que la vas a consultar muchas veces cuando tengas problemas ❤️.

En ese paso de programador novato a programador profesional se encuentra aprender a consultar documentación, da el paso, no le temas a la documentación, es tu mejor amiga 😄.

[Documentación-Python](https://platzi.com/clases/2255-python-intermedio/36457-que-es-la-documentacion/)

# ¿Qué es un Entorno Virtual? 

* **Módulo**: Es código escrito por otra persona que sirve para resolver un problema de manera rápida. 

<p align="center"><img width=50% src="./Pictures/entorno_virtual.png"></p>

Se debería tener una versión única de Python funcionando en cada proyecto, por lo tanto, al actualizar los módulos se puede elegir en que proyecto actualizarlo y en cuál no. 

El concepto de entorno virtual se reduce a tener python funcionando independientemente a cada proyecto. 

<p align="center"><img width=50% src="./Pictures/entorno_virtual_2.png"></p>

la idea es sencilla, de hecho el concepto es similar al de los contenedores de Docker, como profesional empezarás a requerir de trabajar diversos proyectos que trabajen con diferentes versiones, ya sea del lenguaje o de algún módulo.

Sería una catástrofe tener que instalar y actualizar módulos para cada proyecto cuidando que ninguno se rompa, porque fácilmente podrías actualizar un módulo que, para un proyecto funcione, pero para otro deje de funcionar, es por eso que se crea el concepto de entornos virtuales.

Este concepto lo tienen muchos lenguajes, y lo genial es que soluciona muy bien el problema de la compatibilidad entre proyectos, porque cada entorno virtual es independiente y funciona con las versiones que se les hayan instalado ahí mismo.

# El Primer Paso Profesional: Creación de un Entorno Virtual 

* Se crea una carpeta y se ingresa a ella **$ mkdir proyecto_ejemplo && cd proyecto_ejemplo**
* Se inicializa un sistema de control de versiones (GIT) **$ git init** Es recomendable hacerlo para ser un buen desarrollador
* Se procede a crear un ambiente virtual **$ python3 -m venv nombre_venv** 
    * Usualmente nombre_venv es **venv** o **env**
* Se ingresa a la carpeta venv **$ cd venv**
* Activación del ambiente virtual:
    * Windows: **.\venv\Scripts\activate**
    * Unix o MacOs: **source venv/bin/activate**
    * Para mayotr facilidad se crea un alias. *alias avenv='source venv/bin/activate'*
* Desactivar el ambiente virtual:
    * **deactivate**

# Instalación de Dependencias con PIP (Package Installer for Python)
Básicamente, pip es como el npm de JavaScript, y el archivo requeriments.txt es como el package.json de JavaScript.

Es importante recordar que esto se debe correr con el entorno virtual activado (avenv), de esta manera todas las dependencias que instalemos se guardaran para este entorno virtual (de lo contrario se guardarían de manera global, que es justo lo que no queremos).

Algo importante, si estás manejando git, es bueno siempre ignorar la carpeta venv, esto porque realmente no nos importa subir todo eso al repositorio, puedes mirarlo como que venv es el node_modules de JavaScript, a fin de cuentas, cualquier otro programador que trabaje con nuestro código creará su propio entorno virtual e instalará las dependencias que dejamos en nuestro requeriments.txt.

Y un dato curioso es que, el operador **>** en la terminal es algo especial de UNIX, ya que este operador lo que hace es redirigir la salida de cualquier comando hacia donde lo mandes, por defecto la salida es en la terminal, pero al usar **>** le dijimos a la terminal que, en lugar de que la salida sea en la terminal, que se redirija al archivo requeriments.txt. Si quieren jugar con ello, pueden hacerlo con este ejemplo: 
```bash
ls -al > test.txt
```
eso creará un archivo llamado test.txt, y si lo abren verán cómo es que ese comando funciona

## Módulos Populares 

* **Requests y BeautifulSoup4** Son módulos utilizados para Web Scraping
* **Pandas y Numpy** Que se utilizan en la ciencia de datos 
* **Pytest** Utilizado para realizar Testing 

## Resumen PIP 

Pip (package installer for python) Nos permite descargar paquetes de terceros para utilizarlos en nuestro enviroment, ademas se puede definir una versión especifica del paquete.

+ **pip install < paquete >** instala el paquete(pandas , matplotlib, bokeh, etc) que se especifique

+ **pip freeze** muestra todos los paquetes instalados en tu ambiente virtual

Si quisiéramos que alguien mas pueda ejecutar nuestro proyecto es importante compartir que librería y versión hemos empleado; eso se realiza con el comando:
```bash
pip freeze > requirements.txt
```

El resultado de pip freeze se escribe en requirements.txt (puedes usar otro nombre pero el mostrado es una buena practica)

para instalar paquetes desde un archivo como requirements.txt ejecutamos:
```bash
pip install -r requirements.txt 
```

# List Comprehensions 

<p align="center"><img width=50% src="./Pictures/list_comprehensions.png"></p>

<p align="center"><img width=50% src="./Pictures/list_comprehensions.gif"></p>

# Dictionary Comprehensions 

<p align="center"><img width=80% src="./Pictures/dictionary_comprehension.webp"></p>

# Funciones Anónimas (Lambda Functions)

Son funciones que no tienen un identificador, tienen una serie de características especiales y su 
estructura es: 

```Python
lambda argumentos: expresión
```
Puede tener únicamente una línea de código 

Ejemplo en palindromo 

```Python 
#Identificador      Argumento       Expresión
palindrome     =    lambda string : string == string[::-1]
print(palindrome('ana'))

>>>solución = True

```
Entonces, cuando se cree una lambda function es necesario recordar que es una función anónima, pero el nombre 
que va a tener esta función es la variable que va a guardar el objeto de tipo función que esta expresión retorna

# High Order Functions: Filter, map y reduce 

Una función de orden superior es una función que recibe como parámetro a otra función. 

Existe una lista de números aleatorios, de los cuales se obtendrán únicamente los números impares 

 ## Uso con list comprehensions Filter

```Python
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = [i for i in my_list if i%2 != 0]

print(odd)
```
## Uso con Filter
```Python
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = list(filter(lambda x: x%2 !=0, my_list))

print(odd)
```
Existe una lista y se requiere el cuadrado de sus valores 

## Uso con List Comprehensions map
```Python
my_list2 = [1,2,3,4,5]
squares = [i**2 for i in my_list2 ]

print(squares)
```
## Uso con Map 
```Python
my_list2 = [1,2,3,4,5]
squares = list(map(lambda x: x**2, my_list2))

print(squares)
```

## Uso con for reduce 
```Python
my_list3 = [2,2,2,2,2]
    
all_multiplied = 1

for i in my_list3:
    all_multiplied = all_multiplied*i

print(all_multiplied)
```    
## Uso con Reduce 
```Python 
from functools import reduce

my_list3 = [2,2,2,2,2]
all_multiplied = reduce(lambda a,b:a*b,my_list3)

print(all_multiplied)
```

# Proyecto: Filtrando Datos 

Una lista de diccionarios 
```Python
DATA = [
    {
        'name' : 'Facundo',
        'age' : 72
        'organization' : 'Platzi',
        'position' : 'Technical Coach',
        'language' : 'Python',
    },
    {
        'name' : 'Luisana',
        'age' : 33
        'organization' : 'Globant',
        'position' : 'UX Designer',
        'language' : 'Javascript',
    }
]
```

# Los Errores en el Código 

## Tipos de errores 

* SyntaxError: Cuando se está escribiendo código y hay una palabra clave mal escrita, entonces, python detiene el código e informa el error que se está presentando por medio del traceback

* Exception: Sucede en algún punto de nuestro programa, haciendo que se rompa la lógica, por lo tanto, el programa se detiene en el punto donde se presenta el error, algunas excepciones comunes son: 

    * KeyboardInterrupt: Sucede cuando se pulsa **ctrl + c**
    * KeyError: Se intenta acceder a una llave que no existe en un diccionario 
    * IndexError: Sucede cuando se trabaja con listas y se intenta acceder a un índice que no existe 
    * FileNotFoundError: Cuando se intente abrir un archivo que no exista 
    * ZeroDivisionError: Dividir un número entre 0 
    * ImportError: Cuando se intenta importar un módulo y este presenta un error

**Lectura de un traceback**

* La manera correcta de leer un traceback es iniciar por el final, en el caso de un error de sintaxis nos indicará en qué línea se encuentra dicho error.
* En el caso de excepciones la última línea nos indicará el tipo de exepcion que se generó (generalmente son autoexplicativas pero si no entienedes que paso puedes buscar este error)
* La penúltima línea nos indicará dende se encuentra el error (archivo y línea)
* La antepenúltima línea nos muestra “most recent call last” lo que significa que la llamada más reciente es la última (el programa se cerró después de esa llamada, se genero un error)

**Elevar una excepción**

Cuando tenemos una excepción en python lo que sucede es que se crea un objeto de tipo exception que se va moviendo a través de los bloques de código hasta llegar al bloque principal si es que no se maneja dicha excepción en algún bloque intermedio el programa se interrumpe y genera el traceback

# Debugging 

Cuando se presenta un error en el código a excepción de Syntax y Exception, se utiliza depuración, es una herramienta que traen los editores de código. 

# Manejo de Excepciones

* **Try, except**: se utiliza únicamente para las excepciones de tipo TypeError

<p align="center"><img width=45% src="./Pictures/try_except.png"></p>
<p align="center"><img width=45% src="./Pictures/try_except2.png"></p>

* **Raise**: Se utiliza cuando el error no es detectado por python, pero sí por nuestra percepción.

<p align="center"><img width=45% src="./Pictures/raise.png"></p>
<p align="center"><img width=45% src="./Pictures/raise2.png"></p>

* **Finally**: Independientemente del error, se maneja para cerrar archivos, o código. 

<p align="center"><img width=45% src="./Pictures/finally.png"></p>

# Assert Statements (Afirmaciones en Python)

La función de assert es confirmar si ls condición es correcta, de lo contrario, envía un mensaje de error 

```Python
assert condicion, Mensaje de Error      
```
<p align="center"><img width=45% src="./Pictures/assert.png"></p>








