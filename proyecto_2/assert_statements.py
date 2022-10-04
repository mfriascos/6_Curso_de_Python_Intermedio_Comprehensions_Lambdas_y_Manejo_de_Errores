
def divisor(number):
    div = [i for i in range(1,number+1) if number%i == 0]
    return div


def run():
    number = input("Type a number: ")
    assert number.isnumeric() and int(number) > 0, "Debes ingresar un número entero positivo"
    print(divisor(int(number)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()