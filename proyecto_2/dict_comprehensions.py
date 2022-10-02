# Crear un diccionario, cuyas llaves sean los primeros 100 números naturales y cuyos 
# valores sean esos mismos números elevados al cuno 

def run():
# Solución normal 

    # my_dict = {}

    # for i in range(1,101):
    #     if i%3 != 0:
    #         my_dict[i] = i**3

# Solución con Dictionary Comprehensions
    
    # my_dict = { i:i**3 for i in range(1,101) if i%3 != 0}
    # print(my_dict)

# Reto: Crear, con un dictionary Comprehension, un diccionario cuyas llaves sean los 1000 primeros números
# naturales con sus raíces cuadradas como valores. 

    my_dict = {i:i**0.5 for i in range(1,1001)}
    print(my_dict)


if __name__ == '__main__':
    run()