import java.util.Random;

public class Benchmarking {
    

    private MetodosOrdenamiento metodosordenamiento;
    public Benchmarking(){
        long currentMillis = System.currentTimeMillis(); /// sacar la fecha desde la fecha de 1970
        long currentNano= System.nanoTime();

        System.out.println(currentMillis);
        System.out.println(currentNano);

        metodosordenamiento= new MetodosOrdenamiento();
        int[] arreglo = generarArregloAleatorio(1000000);

        Runnable tarea=()-> metodosordenamiento.burbujaTradicional(arreglo);
        double tiempoDuracionMillis = medirConCuTime(tarea);
        double tiempoDuracionNano= medirConNanoTime(tarea);

        System.out.println("Tiempo en milisegundos: " + tiempoDuracionMillis);
        System.out.println("Tiempo en nanosegundos: " + tiempoDuracionNano);
    }

    private int[] generarArregloAleatorio(int tamano){
        int[] array = new int[tamano];
        Random random= new Random();
        for(int i=0; i<tamano; i++){
            array[i]= random.nextInt(100_000);
        }
        return array;
    }

    public double medirConCuTime(Runnable tarea){
        long inicio = System.currentTimeMillis();
        tarea.run();
        long fin = System.currentTimeMillis();
        double tiempoSegundos= (fin-inicio)/1000.0;
        return tiempoSegundos;
    }

    public double medirConNanoTime(Runnable tarea){
        long inicio =System.nanoTime();
        tarea.run();
        long fin = System.nanoTime();
        return  (fin-inicio)/1_000_000_000.0;
    }
}
