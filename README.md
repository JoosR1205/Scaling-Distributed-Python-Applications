# Ejemplos de Concurrencia en Python

Este repositorio contiene ejemplos de programas en Python que ilustran el uso de concurrencia mediante el uso de hilos y demonios.

## Archivos de Ejemplo

1. **ejemplo_hilos.py**: Este archivo contiene un ejemplo básico de cómo utilizar hilos y procesos en Python para realizar tareas concurrentes. El programa crea un hilo que ejecuta una tarea en segundo plano mientras el programa principal sigue ejecutándose.

2. **ejemplo_demonios.py**: En este archivo se muestra cómo crear y utilizar un demonio en Python para ejecutar una tarea en segundo plano. El programa principal continúa ejecutándose mientras la tarea demonio se ejecuta en segundo plano. Además, el demonio se detiene correctamente cuando el programa principal lo indica.

## Hilos y procesos (ejemplo_hilos.py)

Este programa calcula los números primos en un rango dado de manera paralela utilizando tanto hilos como procesos. La función es_primo() se utiliza para verificar si un número es primo. Luego, la función encontrar_primos_rango() se ejecuta en múltiples hilos o procesos para buscar los números primos en un rango dado y se almacenan en una lista compartida. Finalmente, se imprimen los resultados y los tiempos de ejecución para comparar el rendimiento de los hilos y los procesos.

## Daemons (ejemplo_demonios.py)

Este programa muestra cómo puedes usar un hilo demonio para ejecutar una tarea en segundo plano mientras el programa principal sigue ejecutándose y cómo puedes detener el hilo demonio correctamente cuando sea necesario.
