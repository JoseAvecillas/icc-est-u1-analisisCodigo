
from metodos_ordenamiento import MetodosOrdenamiento
import random
import time

class Benchmarking:

    # public Benchmarking
    def __init__(self):
        print('Benchmarking instanciado')
        self.mO= MetodosOrdenamiento()
        arreglo= self.build_arreglo(10000)
        tarea_burbuja= lambda: self.mO.sort_bubble(arreglo)
        tarea_burbuja_mejorado= lambda: self.mO.sort_burbuja_mejorado_optimizado(arreglo)
        tarea_seleccion= lambda: self.mO.sort_seleccion(arreglo)

        #BURBUJA NORMAL
        tiempo_mili_segundos= self.contar_con_current_time_milles(tarea_burbuja)
        tiempo_nano_segundos= self.contar_con_nano_time(tarea_burbuja)
        # print(f'Tiempo con el tiempo en milisegundo: {tiempo_mili_segundos}')
        # print(f'Tiempo  con tiempo en nanosegundos: {tiempo_nano_segundos}')

        #BURBUJA MEJORADO y SELECCION
        tiempo_nA= self.contar_con_nano_time(tarea_burbuja_mejorado)
        tiempo_nAs= self.contar_con_nano_time(tarea_seleccion)

        print(f'Tiempo Burbuja: {tiempo_nano_segundos:.6f} segundos')
        print(f'Tiempo Bubble Mejorado: {tiempo_nA:.6f} segundos')
        print(f'Tiempo Selección:    {tiempo_nAs:.6f} segundos')

        
    def build_arreglo(self, tamano):
        arreglo= []
        for _ in range(tamano):
            numero= random.randint(0, 99999)
            arreglo.append(numero)
        return arreglo
    
    def contar_con_current_time_milles(self, tarea):
        inicio= time.time()
        tarea()
        fin= time.time()
        return (fin - inicio)
    
    def contar_con_nano_time(self, tarea):
        inicio= time.time_ns()
        tarea()
        fin= time.time_ns()
        return (fin - inicio)/1_000_000_000.0
    