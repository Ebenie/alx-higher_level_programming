#include <Python.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", Py_SIZE(bytes));
    printf("  trying string: %s\n", PyBytes_AS_STRING(bytes));

    size = Py_SIZE(bytes) + 1;
    if (size > 10)
        size = 10;

    printf("  first %ld bytes:", size);
    for (i = 0; i < size; i++)
    {
        printf(" %02x", (unsigned char)PyBytes_AS_STRING(bytes)[i]);
    }
    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    size = Py_SIZE(list);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GET_ITEM(list, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
    }
}

