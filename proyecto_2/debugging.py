#Programa que recibe un número como parametro y retorna una lista con todos los divisores de ese número

def run():
    number = int(input("Type a number: "))
    div = [i for i in range(1,number+1) if number%i == 0]    

    print(div)


if __name__ == '__main__':
    run()