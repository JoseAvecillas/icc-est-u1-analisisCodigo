import benchmarking as bm
import metodos_ordenamiento as mO
import matplotlib.pyplot as plt
import copy

if __name__ == "__main__":
    print('Ejecución de todos los métodos')

    bench = bm.Benchmarking()
    metodosO = mO.MetodosOrdenamiento()

    # Tamaños exactos solicitados
    tamanios = [5000, 10000, 30000, 50000, 100000]
    resultados = []

    # Genera una sola vez el arreglo de tamaño máximo
    arreglo_base_max = bench.build_arreglo(tamanios[-1])

    metodoso_dic = { 
        'metodo_burbuja': metodosO.sort_bubble, 
        'metodo_burbuja_mejorado': metodosO.sort_burbuja_mejorado_optimizado,
        'metodo_seleccion': metodosO.sort_seleccion, 
        'metodo_shell': metodosO.sort_shell
    }

    for tam in tamanios:
        sub_arreglo = arreglo_base_max[:tam]  # Subarreglo consistente con los anteriores
        for nombre, fun_metodo in metodoso_dic.items():
            arreglo_copia = copy.deepcopy(sub_arreglo)  # Copia por método
            tiempo_resuelto = bench.medir_tiempo(fun_metodo, arreglo_copia)
            resultados.append((tam, nombre, tiempo_resuelto))

    for tam, nombre, tiempo in resultados:
        print(f'Tamaño: {tam}, Algoritmo: {nombre}, Tiempo: {tiempo:.6f} segundos')

    # Graficar resultados
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

    plt.figure(figsize=(10, 6))
    for nombre, tiempos in tiempos_by_metodo.items():
        plt.plot(tamanios, tiempos, label=nombre, marker="o")

    plt.title("Comparación de tiempo por cada método")
    plt.xlabel("Tamaño de los arreglos")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.legend()
    plt.grid(True)
    plt.show()