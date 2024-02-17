#define PY_SSIZE_T_CLEAN
#include <Python.h>


static PyObject *spam_system(PyObject *self, PyObject *args) {
    PyInterpreterConfig config = {
        .check_multi_interp_extensions = 1,
        .gil = PyInterpreterConfig_OWN_GIL,
    };
    PyThreadState *tstate = NULL;
    PyStatus status = Py_NewInterpreterFromConfig(&tstate, &config);
    if (PyStatus_Exception(status)) {
        return NULL;
    }

    return PyLong_FromLong(1);



    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command)) {
        return NULL;
    }
    sts = system(command);
    if (sts < 0) {
        PyErr_SetString(PyExc_ValueError, "System command failed");
        return NULL;
    }
    return PyLong_FromLong(sts);
}


static PyMethodDef xxx_methods[] = {
    {"system",  spam_system, METH_VARARGS, "Execute a shell command."},
    {NULL, NULL, 0, NULL},
};


static struct PyModuleDef xxx_module = {
    PyModuleDef_HEAD_INIT,
    .m_name = "backports.interpreters.xxx",
    .m_doc = "",
    .m_size = -1,
    .m_methods = xxx_methods,
};


PyMODINIT_FUNC PyInit_xxx() {
    PyObject *mod;

    mod = PyModule_Create(&xxx_module);
    if (mod == NULL) {
        return NULL;
    }

    return mod;
}