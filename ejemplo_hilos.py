import threading
import multiprocessing
import time

def es_primo(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def encontrar_primos_rango(rango_inicio, rango_fin, resultado):
    primos = [n for n in range(rango_inicio, rango_fin) if es_primo(n)]
    resultado.extend(primos)

if __name__ == "__main__":
    rango_inicio = 100000
    rango_fin = 200000

    # Usando hilos
    inicio_hilos = time.time()
    resultado_hilos = []
    hilos = []
    for _ in range(4):  # Usar 4 hilos
        hilo = threading.Thread(target=encontrar_primos_rango, args=(rango_inicio, rango_fin, resultado_hilos))
        hilo.start()
        hilos.append(hilo)
    for hilo in hilos:
        hilo.join()
    fin_hilos = time.time()
    print("Usando hilos:")
    print("Cantidad de números primos encontrados:", len(resultado_hilos))
    print("Tiempo tomado:", fin_hilos - inicio_hilos, "segundos")

    # Usando procesos
    inicio_procesos = time.time()
    resultado_procesos = multiprocessing.Manager().list()
    procesos = []
    for _ in range(4):  # Usar 4 procesos
        proceso = multiprocessing.Process(target=encontrar_primos_rango, args=(rango_inicio, rango_fin, resultado_procesos))
        proceso.start()
        procesos.append(proceso)
    for proceso in procesos:
        proceso.join()
    fin_procesos = time.time()
    print("\nUsando procesos:")
    print("Cantidad de números primos encontrados:", len(resultado_procesos))
    print("Tiempo tomado:", fin_procesos - inicio_procesos, "segundos")

