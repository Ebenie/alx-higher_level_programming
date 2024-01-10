#include <Python.h>

/**
 * print_python_string - Print information about Python string object
 * @p: PyObject string pointer
 */
void print_python_string(PyObject *p)
{
    PyASCIIObject *py_ascii_obj;
    PyCompactUnicodeObject *py_compact_unicode_obj;
    PyVarObject *py_var_obj;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    py_var_obj = (PyVarObject *)p;
    py_ascii_obj = (PyASCIIObject *)p;
    py_compact_unicode_obj = (PyCompactUnicodeObject *)p;

    printf("  type: %s\n", py_ascii_obj->state.compact ? "compact unicode object" : "compact ascii");
    printf("  length: %ld\n", py_var_obj->ob_size);

    if (py_ascii_obj->state.compact)
        printf("  value: %s\n", PyUnicode_AsUTF8(p));
    else
        printf("  value: %ls\n", py_compact_unicode_obj->data);

    fflush(stdout);
}

