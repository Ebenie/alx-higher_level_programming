#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    
    try:
        while printed_elements < x:
            print("{}".format(my_list[printed_elements]), end="")
            printed_elements += 1
    except IndexError:
        pass
    
    print()
    return printed_elements

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    
    nb_print = safe_print_list(my_list, 5)
    print("nb_print: {:d}".format(nb_print))
    
    nb_print = safe_print_list(my_list, 7)
    print("nb_print: {:d}".format(nb_print))
