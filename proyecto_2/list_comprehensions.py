## Crear una lista con los primeros 100 números naturales al cuadrado 

def run():
    # natural_numbers=[]
    # for i in range(1,101):
    #     if i%3 != 0:
    #         natural_numbers.append(i**2)
    
    # print(natural_numbers)
## Ejercicio resuelto con list comprehensions

    # squares=[i**2 for i in range(1,101) if i%3 != 0]

    # print(squares)

## Reto: Crear con un list comprehension , una lista de todos los múltiplos de 4 que a la vez también son múltiplos 
## de 6 y de 9, hasta 5 dígitos

    multip_469 = [i for i in range(1,100000) if i%4 == 0 and i%6 == 0 and i%9 == 0]

    print(multip_469)

if __name__ == '__main__':
    run()