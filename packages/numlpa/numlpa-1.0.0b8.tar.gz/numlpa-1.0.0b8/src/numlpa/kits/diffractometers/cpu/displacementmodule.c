#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <math.h>

/**
 * Compute the resulting displacement field.
 *
 * @param m_x Measurement point x-coordinate.
 * @param m_y Measurement point y-coordinate.
 * @param d_x Dislocation x-coordinates.
 * @param d_y Dislocation y-coordinates.
 * @param senses Dislocation Burgers vector senses.
 * @param number Number of dislocations.
 * @param poisson Poisson number.
 * @param u_x Displacement field x-component.
 * @param u_y Displacement field y-component.
 * @param u_z Displacement field z-component.
 */
void displacement(
    double m_x,
    double m_y,
    double* d_x,
    double* d_y,
    signed char* senses,
    size_t number,
    double poisson,
    double* u_x,
    double* u_y,
    double* u_z
)
{
    double r_x;
    double r_y;
    double x_2;
    double y_2;
    double r_2;
    double atan;
    double c_1 = 2 * (1-poisson);
    double c_2 = 1 - 2*poisson;
    for(size_t i=0; i<number; i++)
    {
        r_x = d_x[i] - m_x;
        r_y = d_y[i] - m_y;
        x_2 = r_x * r_x;
        y_2 = r_y * r_y;
        r_2 = x_2 + y_2;
        atan = atan2(r_y, r_x);
        *u_x += senses[i] * (atan + r_x*r_y/(c_1*r_2));
        *u_y += senses[i] * (c_2*log(r_2) - 2*y_2/r_2);
        *u_z += senses[i] * atan;
    }
}

/**
 * Python displacement wrapper function.
 *
 * @param PyObject
 * @param args
 * @return the displacement field z, y and z components.
 */
static PyObject *py_displacement(
    PyObject *self,
    PyObject *args
)
{
    double m_x;
    double m_y;
    PyObject *obj_d_x;
    Py_buffer buf_d_x;
    PyObject *obj_d_y;
    Py_buffer buf_d_y;
    PyObject *obj_senses;
    Py_buffer buf_senses;
    double poisson;
    double u_x = 0;
    double u_y = 0;
    double u_z = 0;
    if (!PyArg_ParseTuple(args, "ddOOOd", &m_x, &m_y, &obj_d_x, &obj_d_y, &obj_senses, &poisson))
    {
        return NULL;
    }
    if (PyObject_GetBuffer(obj_d_x, &buf_d_x, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1)
    {
        return NULL;
    }
    if (PyObject_GetBuffer(obj_d_y, &buf_d_y, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1)
    {
        return NULL;
    }
    if (PyObject_GetBuffer(obj_senses, &buf_senses, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1)
    {
        return NULL;
    }
    displacement(m_x, m_y, buf_d_x.buf, buf_d_y.buf, buf_senses.buf, buf_senses.shape[0], poisson, &u_x, &u_y, &u_z);
    return Py_BuildValue("[ddd]", u_x, u_y, u_z);
}

static PyMethodDef DisplacementModule[] = {
    {
        "displacement",
        py_displacement,
        METH_VARARGS,
        "Compute the resulting displacement field."
    },
    {
        NULL,
        NULL,
        0,
        NULL
    }
};

static struct PyModuleDef displacementmodule = {
    PyModuleDef_HEAD_INIT,
    "displacement", // module name
    NULL,  // module documentation
    -1,
    DisplacementModule
};

PyMODINIT_FUNC PyInit_displacement(void)
{
    return PyModule_Create(&displacementmodule);
}
