import os
import psutil
import signal

def listar_procesos():
    """Lista los procesos activos en el sistema con su PID y nombre."""
    print(f"{'PID':<10} {'Nombre':<30}")
    print("=" * 40)
    for proceso in psutil.process_iter(attrs=['pid', 'name']):
        print(f"{proceso.info['pid']:<10} {proceso.info['name']:<30}")

def eliminar_proceso(pid):
    """Elimina un proceso dado su PID."""
    try:
        os.kill(pid, signal.SIGTERM)  # Intenta terminar el proceso de forma segura
        print(f"Proceso con PID {pid} terminado correctamente.")
    except ProcessLookupError:
        print(f"No se encontró ningún proceso con PID {pid}.")
    except PermissionError:
        print(f"No tienes permisos para eliminar el proceso con PID {pid}.")
    except Exception as e:
        print(f"Error al intentar eliminar el proceso: {e}")

if __name__ == "__main__":
    listar_procesos()
    try:
        pid = int(input("\nIngrese el PID del proceso que desea eliminar: "))
        eliminar_proceso(pid)
    except ValueError:
        print("Debe ingresar un número válido.")