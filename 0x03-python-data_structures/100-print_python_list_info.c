#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - it prints some basic info about
 * python
 *
 * @p: struct containing python objects
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;
	PyListObject *list;

	size = PyList_Size(p);  /* gets the length of list object */
	printf("[*] Size of the Python List = %ld\n", size);

	list = (PyListObject *)p; /* typecast pyobject to get the memory alloc */
	printf("[*] Allocated = %ld\n", list->allocated);

	i = 0;
	while (i < size)
	{
		item = PyList_GetItem(p, i);    /* gets the object at position i */
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
	}
}
