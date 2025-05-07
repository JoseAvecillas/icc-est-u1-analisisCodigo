# Archivo principal o main 
import benchmarking as bm
import metodos_ordenamiento as mO
import matplotlib.pyplot as plt
import copy

if __name__ == "__main__":
    print('Ejecución de todos los métodos')

    bench = bm.Benchmarking()
    metodosO = mO.MetodosOrdenamiento()

    tamanios = [5000, 10000, 10500]
    resultados = []

    metodoso_dic = { 
        'metodo_burbuja': metodosO.sort_bubble, 
        'metodo_burbuja_mejorado': metodosO.sort_burbuja_mejorado_optimizado,
        'metodo_seleccion': metodosO.sort_seleccion, 
        'metodo_shell': metodosO.sort_shell
    }

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)
        for nombre, fun_metodo in metodoso_dic.items():
            arreglo_copia = copy.deepcopy(arreglo_base)  # Asegura que todos usen el mismo arreglo original
            tiempo_resuelto = bench.medir_tiempo(fun_metodo, arreglo_copia)
            resultados.append((tam, nombre, tiempo_resuelto))

    for tam, nombre, tiempo in resultados:
        print(f'Tamaño: {tam}, nombre método: {nombre}, tiempo: {tiempo:.6f} segundos')

    # Preparar datos para graficar
    tiempos_by_metodo = {
        "burbuja": [],
        "burbujaM": [],
        "seleccion": [],
        "shell": []
    }

    nombre_map = {
        "metodo_burbuja": "burbuja",
        "metodo_burbuja_mejorado": "burbujaM",
        "metodo_seleccion": "seleccion",
        "metodo_shell": "shell"
    }

    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre_map[nombre]].append(tiempo)

    # Graficar
    plt.figure(figsize=(10, 6))

    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker="o")

    plt.title("Comparación de tiempo por cada método")
    plt.xlabel("Tamaño de los arreglos")
    plt.ylabel("Tiempo de ejecución")
    plt.legend()
    plt.show()


    # solucionado 