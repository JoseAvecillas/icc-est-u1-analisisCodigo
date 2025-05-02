# Archivo principal o main 
import benchmarking as bm
import metodos_ordenamiento as mO

if __name__ == "__main__":
    print('Ejecucion de todos los metodos')


    bench= bm.Benchmarking()
    metodosO= mO.MetodosOrdenamiento()

    #tam =10000
    tamanios= [5000, 10000, 10500]
    resultados = []

    for tam in tamanios:
        arreglo_base = bench.build_arreglo(tam)
        metodoso_dic= { 
            'metodo_burbuja': metodosO.sort_bubble, 
            'metodo_burbuja_mejorado': metodosO.sort_burbuja_mejorado_optimizado,
            'metodo_seleccion': metodosO.sort_seleccion, 
            'metodo_shell': metodosO .sort_shell
        }
        for nombre, fun_metodo in metodoso_dic.items():
            tiempo_resueltado= bench.medir_tiempo(fun_metodo, arreglo_base)
            tupla_resultado= (tam, nombre, tiempo_resueltado)
            resultados.append(tupla_resultado)

    for tam, nombre, tiempo in resultados:
        print(f'Tamaño: {tam}, nombre metodo: {nombre}, tiempo: {tiempo:.6F} segundos')