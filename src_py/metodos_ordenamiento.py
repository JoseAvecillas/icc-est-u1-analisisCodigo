class MetodosOrdenamiento:
    def sort_bubble(self, array):
        arreglo= array.copy()
        n= len(arreglo)
        for i in range(n):
            for j in range(i +1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j]= arreglo[j], arreglo[j]
        return arreglo
    

    # Programar cada metodo
    # medir tiempo con Nano
    # Imprimir 3 resultados indicando cual es el mejor
    def sort_burbuja_mejorado_optimizado(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arreglo[j] > arreglo[j + 1]:
                    arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]
        return arreglo

    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            min_index = i  
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_index]:
                    min_index = j 
            if min_index != i:
                arreglo[i], arreglo[min_index] = arreglo[min_index], arreglo[i]
        return arreglo
