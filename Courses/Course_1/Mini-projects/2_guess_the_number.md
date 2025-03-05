## Descripción del Mini-proyecto  🎯🎮📜  
### Un recordatorio sobre el Código de Honor  

En mini-proyectos anteriores, hemos tenido casos de estudiantes que han enviado soluciones copiadas de internet. Recuerda que, si puedes encontrar código en la web para uno de los mini-proyectos, nosotros también podemos encontrarlo. Enviar código copiado viola el Código de Honor de esta clase, así como los Términos de Servicio de Coursera. Escribe tu propio código y evita copiar.  

Si, durante la evaluación por pares, sospechas que un mini-proyecto enviado incluye código copiado, evalúa como de costumbre y envía los detalles de la tarea por correo electrónico a [iipphonorcode@online.rice.edu](mailto:iipphonorcode@online.rice.edu). Investigaremos y tomaremos las medidas adecuadas.  

---  

## Descripción del Mini-proyecto - Juego "Adivina el número"  🔢🎲💡  

Uno de los juegos más simples para dos jugadores es "Adivina el número". El primer jugador piensa en un número secreto dentro de un rango conocido, mientras que el segundo jugador intenta adivinarlo. Después de cada intento, el primer jugador responde con "Más alto", "Más bajo" o "¡Correcto!" dependiendo de si el número secreto es mayor, menor o igual a la suposición.  

En este proyecto, construirás un programa interactivo en Python en el que la computadora asumirá el rol del primer jugador, mientras que tú jugarás como el segundo.  

Cuando hablemos de rangos en este mini-proyecto, seguiremos la convención estándar de Python: el extremo inferior del rango está incluido, mientras que el extremo superior está excluido. Matemáticamente, representamos los rangos con la notación `[bajo, alto)`. Por ejemplo, el rango `[0, 3)` incluye los números 0, 1 y 2, pero no el 3.  

Interactuarás con tu programa mediante un campo de entrada y varios botones. En este proyecto, ignoraremos el lienzo y mostraremos las respuestas de la computadora en la consola. Construir una versión inicial que imprima información en la consola es una estrategia de desarrollo que también deberías usar en proyectos futuros. Enfocarse primero en la lógica del programa antes de mejorar la presentación visual ahorra tiempo, ya que depurar errores lógicos en una interfaz gráfica puede ser complicado.  

---  

## Proceso de Desarrollo del Mini-proyecto  🛠️📌🚀  

Hemos proporcionado una plantilla básica para este mini-proyecto. A continuación, se detalla nuestra estrategia recomendada para desarrollar la versión básica de "Adivina el número". Recuerda ejecutar tu programa después de cada paso para asegurarte de que se implementó correctamente.  

1. Agrega código a la plantilla que cree un marco con un campo de entrada y un controlador de eventos llamado `input_guess`. Este campo de entrada se usará para ingresar las suposiciones.  

2. En el controlador `input_guess(guess)`, convierte la cadena de entrada `guess` en un número entero y muestra un mensaje en la consola con el formato `"La suposición fue 37"` (o el número correspondiente).  

3. En la función `new_game`, inicializa una variable global `secret_number` con un número aleatorio en el rango `[0, 100)`. Asegúrate de incluir la declaración `global`.  

4. En `input_guess`, compara el número ingresado con `secret_number` y muestra un mensaje adecuado como `"Más alto"`, `"Más bajo"` o `"Correcto"`.  

5. Prueba tu código jugando varias partidas con un rango fijo. Puedes usar esta [plantilla de prueba](http://www.codeskulptor.org/#examples-gtn_testing_template.py).  

---  

## Mejoras y Funcionalidades Adicionales  ✨🎛️📈  

Para obtener la calificación completa, deberás realizar dos mejoras:  

1. **Añadir botones para reiniciar el juego sin hacer clic en "Run"**  
   - Agrega dos botones etiquetados como `"Rango es [0,100)"` y `"Rango es [0,1000)"`.  
   - Estos botones permitirán al jugador elegir diferentes rangos para el número secreto.  
   - Al hacer clic en un botón, el juego debe reiniciarse con el nuevo rango y mostrar un mensaje apropiado.  

2. **Limitar el número de intentos**  
   - El programa debe mostrar cuántos intentos quedan después de cada suposición.  
   - Si el jugador se queda sin intentos, pierde la partida y el juego se reinicia automáticamente.  
   - Para `[0, 100)`, se permiten **7 intentos**.  
   - Para `[0, 1000)`, se permiten **10 intentos**.  

---  

## Criterios de Evaluación (11 puntos en total, escala de 100 pts)  📊📋✅  

- **1 pt** — El juego comienza inmediatamente cuando se presiona "Run" en CodeSkulptor.  
- **1 pt** — Siempre hay un juego en curso.  
- **1 pt** — El programa lee la suposición desde el campo de entrada y la muestra correctamente.  
- **3 pts** — El juego funciona correctamente con el rango `[0, 100)` (1 punto por cada juego correcto).  
- **2 pts** — Se incluyen dos botones para seleccionar el rango `[0, 100)` o `[0, 1000)`, y estos funcionan correctamente (1 punto por botón).  
- **2 pts** — El juego limita el número de intentos y termina correctamente cuando se agotan.  
- **1 pt** — El número de intentos varía según el rango: 7 intentos para `[0, 100)` y 10 intentos para `[0, 1000)`.  

Para ver un ejemplo de un proyecto con calificación perfecta, consulta el video de demostración en la lección de "Adivina el número".  

**Nota:** No es necesario validar si el número ingresado está dentro del rango correcto. Es responsabilidad del jugador asegurarse de ingresar números válidos.  

---
### Project links

1. [Mini-project Video](https://www.coursera.org/learn/interactive-python-1/lecture/jcFph/mini-project-video)
2. [Mini-project Description](https://www.coursera.org/learn/interactive-python-1/supplement/zrxfY/mini-project-description)
3. [Practice Mini-project: Magical Octosphere Reloaded (optional)](https://www.coursera.org/learn/interactive-python-1/supplement/bcfU6/practice-mini-project-magical-octosphere-reloaded-optional)
4. [Code Clinic Tips](https://www.coursera.org/learn/interactive-python-1/supplement/H2YsT/code-clinic-tips)
5. [Peer-graded Assignment: "Guess the Number!"](https://www.coursera.org/learn/interactive-python-1/peer/vAZGK/guess-the-number)
6. [Peer-graded Assignment: "Guess the Number!"](https://www.coursera.org/learn/interactive-python-1/peer/vAZGK/guess-the-number/give-feedback)

