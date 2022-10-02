# Crear un diccionario, cuyas llaves sean los primeros 100 números naturales y cuyos 
# valores sean esos mismos números elevados al cuno 

def run():
# Solución normal 

    # my_dict = {}

    # for i in range(1,101):
    #     if i%3 != 0:
    #         my_dict[i] = i**3

# Solución con Dictionary Comprehensions
    my_dict = { i:i**3 for i in range(1,101) if i%3 != 0}
    print(my_dict)


if __name__ == '__main__':
    run()