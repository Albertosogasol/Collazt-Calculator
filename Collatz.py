import time

def calculate(value):
    if value % 2 == 0:
        value /= 2
    else:
        value = value * 3 + 1
    return int(value)


while True:
    init_value = 0
    final_value = 0
    counter = 0
    option = ""
    option = int(input("¿Que desea calcular? -1. Numero de iteraciones. -2. Maximo de un rango -3. Salir -> "))
    max_iteration = max_iteration_number = 0
    start_time = 0
    if option == 1:
        init_value = int(input("Introduzca el valor a calcular: "))
        value = init_value
        counter = 0
        start_time = time.time()
        while value != 1:
            value = calculate(value)
            counter += 1
        print("Iteraciones: ", counter)
        print("Final: ", value)
        print("--- %s seconds ---" % (time.time() - start_time))
    elif option == 2:
        final_value = int(input("Introduzca el numero hasta el que comprobar el valor: "))
        max_iteration = 0
        max_iteration_number = 0
        start_time = time.time()
        for i in range(2,final_value + 1):
            value = i
            counter = 0
            start_time = time.time()
            while value != 1:
                value = calculate(value)
                counter += 1
                if counter >= max_iteration:
                    max_iteration = counter
                    max_iteration_number = i
            
        print("Numero maxima iteraciones: ",max_iteration_number)
        print("Iteraciones: ", max_iteration)
        print("--- %s seconds ---" % (time.time() - start_time))
                


    