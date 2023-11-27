# compiladorLmmd
Compilador de "laMateriaMasDificil": diseñoDeCompiladores.

/////////////////////////////////////////////////////
DOCUMENTACION DE USUARIO
////////////////////////////////////////////////////

Este es un lenguaje estadistico escrito en Python usando PLY. El lenguaje implementa todos los componentes tradicionales de un lenguaje tipico; variables, operaciones aritmeticas, ciclos, condicionales de flujo, arreglos y funciones estadisticas como la media, moda y varianza.

Instalacion
Es necesario clonar el repositorio con todos los archivos; parser, lexer, virtualMachine, memoryUse, varsTable, etc., así como tener instalada la librería de PLY.

Ejecucion
Se debe de trabajar sobre el archivo "fileToUse.lmmd" y usar el comando "python3 lmmdMainExecution.py" en la raíz.

Ejemplos de codigo
En la carpeta "tests" se encuentran ejemplos del codigo los cuales incluye; fibonacci, facorial, find, sort y funcionesEspeciales.

Tipos soportados para el uso del usuario:
int, float y char.
LMMD también soporta elementos no atomicos hoogeneos de una dimensión; arrays, del mismo tipo que los soportados para el usuario de los atomicos.

=====================================
Asignacion
x = 5 ;
y[1] = 7 * 4;
=====================================


=====================================
Condiciones
if ( x < 3 ) 
{ y = y + 1; }
=====================================


=====================================
if ( y < 3 )
{ x = x + 2; } 
else 
{ x = x - 3; }
=====================================


=====================================
Ciclos
while ( x > 3 ) do { y = x - 1 } ;
=====================================


=====================================
Lectura
read(a);
=====================================


=====================================
Escritura
write(b);
=====================================


=====================================
Modulos / Funciones
function void miFunc()
{}
=====================================


=====================================
Invocacion modulos / funcs
function float calculateFloatValue()
{}

miVarFloat = calculateFloatValue();
=====================================


=====================================
Estadistica

int: miArreglo[10];
float: media, moda, varianza;

media = media(miArreglo);
moda = moda(miArreglo);
varianza = varianza(miArreglo);
=====================================
=====================================
