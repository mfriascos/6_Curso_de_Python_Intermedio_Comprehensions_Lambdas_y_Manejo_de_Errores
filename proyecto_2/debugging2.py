def divisor(number):
    div = [i for i in range(1,number+1) if number%i == 0] 
    return div

def run():
    try:
        number = int(input("Type a number: "))
        try:
            if number <= 0:
                raise ValueError("Únicamente números  positivos") 
            print(divisor(number))
        except ValueError as ve:
            print(ve)
            return False
    except ValueError:
        print("Debes ingresar un número")


if __name__ == '__main__':
    run()