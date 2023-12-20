#include <Python.h>
#include <floatobject.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_GET_SIZE(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    size = PyBytes_GET_SIZE(p) < 10 ? PyBytes_GET_SIZE(p) : 10;
    for (i = 0; i < size; i++)
        printf("%02x%c", (unsigned char)PyBytes_AS_STRING(p)[i],
               i < size - 1 ? ' ' : '\n');
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < Py_SIZE(list); i++)
    {
        item = PyList_GET_ITEM(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);

        if (PyBytes_Check(item))
            print_python_bytes(item);
        else if (PyFloat_Check(item))
            print_python_float(item);
        else
            printf("  [ERROR] Invalid %s Object\n", Py_TYPE(item)->tp_name);
    }
}

void print_python_float(PyObject *p)
{
    PyFloatObject *f = (PyFloatObject *)p;

    printf("[.] float object info\n");
    printf("  value: %f\n", f->ob_fval);
}

