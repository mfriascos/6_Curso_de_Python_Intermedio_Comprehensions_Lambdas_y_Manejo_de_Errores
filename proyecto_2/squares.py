from functools import reduce


def run():
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = [i for i in my_list if i%2 != 0]

    print(odd)

    #Uso de Filter 
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd = list(filter(lambda x: x%2 !=0, my_list))

    print(odd)
    
    #--------------------------------------------------------------
    my_list2 = [1,2,3,4,5]
    squares = [i**2 for i in my_list2 ]

    print(squares)

    # Uso con maps 
    my_list2 = [1,2,3,4,5]
    squares = list(map(lambda x: x**2, my_list2))

    print(squares)
    
    #----------------------------------------------------------------
    my_list3 = [2,2,2,2,2]
    
    all_multiplied = 1

    for i in my_list3:
        all_multiplied = all_multiplied*i

    print(all_multiplied)
    
    #Uso con Reduce 

    all_multiplied2 = reduce(lambda a,b:a*b,my_list3)

    print(all_multiplied2)


if __name__ == '__main__':
    run()