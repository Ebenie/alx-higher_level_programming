#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_integers = 0
    
    try:
        i = 0
        while printed_integers < x:
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end="")
                printed_integers += 1
            i += 1
    except IndexError:
        pass
    
    print()
    return printed_integers

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, 7)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, 10)
    print("nb_print: {:d}".format(nb_print))
