# Leer archivos
def read():
    numbers = []
    with open("./archivos/numbers.txt","r", encoding="utf-8") as f:     #Para leer sin errores, tílde o ñ
        for line in f:
            numbers.append(int(line))
    
    print(numbers)

# Escribir, sobreescribir archivos
def write():
    names = ['Facundo','Mario','Cristian','Pepe','Rocío']
    with open("./archivos/names.txt","a",encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    read()
    write()

if __name__=='__main__':
    run()