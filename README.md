### Práctica 1: Validar una contraseña

**Objetivo:** Crear un programa que pida al usuario una contraseña y solo lo deje continuar si ingresa la contraseña correcta.

**Pasos a seguir:**

1. Crea una variable llamada `contrasena_correcta` y asígnale una contraseña de tu elección (por ejemplo, `"programacion"`).

2. Crea otra variable, `contrasena_ingresada`, e inicialízala con un valor vacío o incorrecto (por ejemplo, `""`).

3. Usa un bucle `while` cuya condición sea que `contrasena_ingresada` sea diferente a `contrasena_correcta`.

4. Dentro del bucle, pide al usuario que ingrese una contraseña usando `input()`.

5. Asigna la entrada del usuario a la variable `contrasena_ingresada`.

6. Una vez que el bucle termine (es decir, cuando la contraseña sea correcta), imprime un mensaje de bienvenida.

***

### Práctica 2: Generar una secuencia

**Objetivo:** Escribir un programa que genere la siguiente secuencia de números: 2, 4, 6, 8, 10... hasta un límite especificado por el usuario.

**Pasos a seguir:**

1. Pide al usuario que ingrese un número entero que servirá como el límite de la secuencia.

2. Crea una variable llamada `numero_actual` y asígnale el valor inicial de la secuencia, que es 2.

3. Utiliza un bucle `while` para que la condición se cumpla mientras `numero_actual` sea menor o igual al límite que el usuario ingresó.

4. Dentro del bucle, imprime el valor de `numero_actual`.

5. Asegúrate de que la variable `numero_actual` se incremente en 2 en cada iteración para generar los números pares de la secuencia.

***

### Práctica 3: Contador de vocales

**Objetivo:** Crear un programa que cuente la cantidad de vocales en una frase que ingrese el usuario.

**Pasos a seguir:**

1. Pide al usuario que ingrese una frase y guárdala en una variable, por ejemplo en `frase`.

2. Inicializa una variable `contador_vocales` a 0.

3. Inicializa una variable `indice` a 0. Esta variable te ayudará a recorrer la frase.

4. Usa un bucle `while` para que el bucle se ejecute mientras `indice` sea menor que la longitud total de la frase. Para obtener la longitud de la variable `frase`, usamos `len( frase )`

5. Dentro del bucle, obtén el carácter en la posición actual usando `frase[indice]` y conviértelo a minúscula usando `.lower()`. (`frase[0]` regresa el primer caracter, `frase[1]` el segundo caracter y así sucesivamente)

6. Usa una condición `if` para verificar si el carácter es una vocal (`'a'`, `'e'`, `'i'`, `'o'`, `'u'`). Si es una vocal, incrementa el `contador_vocales` en 1.

7. Al final de cada iteración, incrementa la variable `indice` en 1 para pasar al siguiente carácter.

8. Cuando el bucle termine, imprime el resultado final.

### Práctica 4: Calculadora de promedios

**Objetivo:** Crear un programa que calcule el promedio de una serie de números ingresados por el usuario. El programa debe detenerse cuando el usuario ingrese el número cero.

**Pasos a seguir:**

1. Crea dos variables: `suma_total` y `cantidad_numeros`, ambas inicializadas en 0.

2. Usa un bucle `while` que se ejecute mientras una variable de entrada, por ejemplo `numero`, sea diferente de 0. Puedes inicializar `numero` con un valor que no sea cero antes de que comience el bucle.

3. Dentro del bucle, solicita al usuario que ingrese un número.

4. Si el número ingresado no es 0, agrégalo a `suma_total` y aumenta `cantidad_numeros` en 1.

5. Una vez que el bucle termine, verifica si `cantidad_numeros` es mayor que 0 para evitar una división por cero.

6. Si la condición se cumple, calcula el promedio (`suma_total` / `cantidad_numeros`) e imprímelo. Si no, muestra un mensaje indicando que no se ingresaron números.

***

### Práctica 5: Validación de entrada de datos

**Objetivo:** Escribir un programa que pida al usuario que ingrese un número par. El programa debe seguir pidiendo un número hasta que el usuario ingrese un valor que sea par.

**Pasos a seguir:**

1. Crea una variable llamada `es_par` e inicialízala como `False`. Esta variable actuará como una "bandera" o _flag_.

2. Usa un bucle `while` que se ejecute mientras `es_par` sea `False`.

3. Dentro del bucle, pide al usuario que ingrese un número entero.

4. Usa el operador de módulo (`%`) para verificar si el número es par. Un número es par si el residuo de la división por 2 es 0 (`numero % 2 == 0`).

5. Si el número es par, cambia el valor de `es_par` a `True` e imprime un mensaje de confirmación.

6. Si el número no es par, imprime un mensaje pidiéndole al usuario que intente de nuevo.

7. El bucle terminará automáticamente cuando la bandera cambie a `True`.
