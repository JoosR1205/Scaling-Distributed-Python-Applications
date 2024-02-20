import threading
import time

class TareaDemonio(threading.Thread):
    def __init__(self):
        super().__init__()
        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            print("Tarea en segundo plano ejecutándose...")
            time.sleep(1)

    def detener(self):
        self._stop_event.set()

if __name__ == "__main__":
    tarea_demonio = TareaDemonio()
    tarea_demonio.daemon = True  # Establecer como demonio
    tarea_demonio.start()

    print("Programa principal en ejecución...")

    try:
        # Permitir que el programa principal siga ejecutándose mientras la tarea de demonio se ejecuta en segundo plano
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nDeteniendo la tarea de demonio...")
        tarea_demonio.detener()
        tarea_demonio.join()

    print("Programa principal finalizado.")
