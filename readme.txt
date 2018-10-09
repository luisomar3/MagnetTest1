Prueba Magnet para el cargo desarrollador Python
Prueba 1 Magnet

En este documento se explica el funcionamiento del programa. Como fue solicitado el programa verifica si una formula matemática está correctamente formada, la condicion para estar correctamente formada es que por cada parentesis que abre, existe uno correspondiente que lo cierra y que además no cierra un paréntesis antes de abrirlo. Por ejemplo:

    • “(2+4)-3*(2+(4-5))” es una fórmula bien formada. 
    • “(2+5)-)(3))” no lo es.
    • “((2*3))” es una fórmula bien formada.
    • “((“ no lo es.
Se creó una solucion pensando en la estructura de datos conocida como pila, ya que es ideal para este tipo de casos donde debemos extraer datos en una forma específica.

Se inicia el programa usando, python MagnetFilter1.py , donde enseguida se solicitará la expresión, al  introducirla, el programa arrojará un booleano, siendo True para bien formado y False para mal formado.

La lógica del programa está basada en una pila a la cual se agregan los parentesis de apertura, y por cada coincidencia con un parentesis de clausura, voy extrayendo los parentesis de apertura, sí, al final del ciclo, mi pila está vacia significa que la formula está bien formada, caso contrario estariamos en presencia de un error en la formula.

La entrega del programa incluye lo solicitado, más unas pruebas unitarias de rutina que incluí más que todo porque me estoy esforzando por adoptar metodologias como TDD, en el archivo requirements.txt está la librería usada para las pruebas. Si se quiere realizar las pruebas se ejecuta el comando python -m pytest --verbose (luego de instalada la librería) en la carpeta donde se encuentra los archivos y se ejecutaran las pruebas.
