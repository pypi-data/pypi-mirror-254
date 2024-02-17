#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <stdio.h>
#include <math.h>

/**
 * Compute the resulting strain and stress fields for edge dislocations.
 */
void edge(
    double poisson,
    double core_2,
    double cst_stress,
    double cst_strain,
    double* d_x,
    double* d_y,
    signed char* senses,
    double* m_x,
    double* m_y,
    signed char* keep,
    double* stress_xx,
    double* stress_yy,
    double* stress_zz,
    double* stress_xy,
    double* stress_yz,
    double* stress_zx,
    double* strain_xx,
    double* strain_yy,
    double* strain_zz,
    double* strain_xy,
    double* strain_yz,
    double* strain_zx,
    unsigned long long index,
    size_t number
)
{
    double r_x;
    double r_y;
    double x_2;
    double y_2;
    double r_2;
    double r_4;
    double temp_strain_xx = 0;
    double temp_strain_yy = 0;
    double temp_stress_xx = 0;
    double temp_stress_yy = 0;
    double temp_xy = 0;
    double c_1 = 2 * (1 - poisson);
    double c_2;
    double c_3;
    double c_4;
    for(size_t i=0; i<number; i++)
    {
        r_x = d_x[i] - m_x[index];
        r_y = d_y[i] - m_y[index];
        x_2 = r_x * r_x;
        y_2 = r_y * r_y;
        r_2 = x_2 + y_2;
        if (r_2 < core_2)
        {
            return;
        }
        r_4 = r_2 * r_2;
        c_2 = x_2 - y_2;
        c_3 = 3 * x_2 + y_2;
        c_4 = r_y / r_2;
        temp_strain_xx -= senses[i] * c_4 * (c_2 / r_2 + c_1);
        temp_strain_yy += senses[i] * c_4 * (c_3 / r_2 - c_1);
        temp_stress_xx -= senses[i] * r_y * c_3 / r_4;
        temp_stress_yy += senses[i] * r_y * c_2 / r_4;
        temp_xy += senses[i] * r_x * c_2 / r_4;
    }
    stress_xx[index] = cst_stress * temp_stress_xx;
    stress_yy[index] = cst_stress * temp_stress_yy;
    stress_xy[index] = cst_stress * temp_xy;
    stress_zz[index] = poisson * (stress_xx[index] + stress_yy[index]);
    strain_xx[index] = cst_strain * temp_strain_xx;
    strain_yy[index] = cst_strain * temp_strain_yy;
    strain_xy[index] = cst_strain * temp_xy;
    keep[index] = 1;
}

/**
 * Compute the resulting strain and stress fields for screw dislocations.
 */
void screw(
    double core_2,
    double cst_stress,
    double cst_strain,
    double* d_x,
    double* d_y,
    signed char* senses,
    double* m_x,
    double* m_y,
    signed char* keep,
    double* stress_xx,
    double* stress_yy,
    double* stress_zz,
    double* stress_xy,
    double* stress_yz,
    double* stress_zx,
    double* strain_xx,
    double* strain_yy,
    double* strain_zz,
    double* strain_xy,
    double* strain_yz,
    double* strain_zx,
    unsigned long long index,
    size_t number
)
{
    double r_x;
    double r_y;
    double r_2;
    double temp_yz = 0;
    double temp_zx = 0;
    for(size_t i=0; i<number; i++)
    {
        r_x = d_x[i] - m_x[index];
        r_y = d_y[i] - m_y[index];
        r_2 = r_x*r_x + r_y*r_y;
        if (r_2 < core_2)
        {
            return;
        }
        temp_yz += senses[i] * r_x / r_2;
        temp_zx -= senses[i] * r_y / r_2;
    }
    stress_yz[index] = cst_stress * temp_yz;
    stress_zx[index] = cst_stress * temp_zx;
    strain_yz[index] = cst_strain * temp_yz;
    strain_zx[index] = cst_strain * temp_zx;
    keep[index] = 1;
}

/**
 * Python edge wrapper function.
 *
 * @param PyObject
 * @param args
 * @return the strain energy density.
 */
static PyObject *py_edge(
    PyObject *self,
    PyObject *args
)
{
    double poisson;
    double core;
    double cst_stress;
    double cst_strain;
    PyObject *obj_d_x; Py_buffer buf_d_x;
    PyObject *obj_d_y; Py_buffer buf_d_y;
    PyObject *obj_senses; Py_buffer buf_senses;
    PyObject *obj_m_x; Py_buffer buf_m_x;
    PyObject *obj_m_y; Py_buffer buf_m_y;
    PyObject *obj_keep; Py_buffer buf_keep;
    PyObject *obj_stress_xx; Py_buffer buf_stress_xx;
    PyObject *obj_stress_yy; Py_buffer buf_stress_yy;
    PyObject *obj_stress_zz; Py_buffer buf_stress_zz;
    PyObject *obj_stress_xy; Py_buffer buf_stress_xy;
    PyObject *obj_stress_yz; Py_buffer buf_stress_yz;
    PyObject *obj_stress_zx; Py_buffer buf_stress_zx;
    PyObject *obj_strain_xx; Py_buffer buf_strain_xx;
    PyObject *obj_strain_yy; Py_buffer buf_strain_yy;
    PyObject *obj_strain_zz; Py_buffer buf_strain_zz;
    PyObject *obj_strain_xy; Py_buffer buf_strain_xy;
    PyObject *obj_strain_yz; Py_buffer buf_strain_yz;
    PyObject *obj_strain_zx; Py_buffer buf_strain_zx;
    unsigned long long index;
    if (!PyArg_ParseTuple(
        args,
        "ddddOOOOOOOOOOOOOOOOOOK",
        &poisson,
        &core,
        &cst_stress,
        &cst_strain,
        &obj_d_x,
        &obj_d_y,
        &obj_senses,
        &obj_m_x,
        &obj_m_y,
        &obj_keep,
        &obj_stress_xx,
        &obj_stress_yy,
        &obj_stress_zz,
        &obj_stress_xy,
        &obj_stress_yz,
        &obj_stress_zx,
        &obj_strain_xx,
        &obj_strain_yy,
        &obj_strain_zz,
        &obj_strain_xy,
        &obj_strain_yz,
        &obj_strain_zx,
        &index
    ))
    {
        return NULL;
    }
    if (PyObject_GetBuffer(obj_d_x, &buf_d_x, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_d_y, &buf_d_y, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_senses, &buf_senses, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_m_x, &buf_m_x, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_m_y, &buf_m_y, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_keep, &buf_keep, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_xx, &buf_stress_xx, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_yy, &buf_stress_yy, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_zz, &buf_stress_zz, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_xy, &buf_stress_xy, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_yz, &buf_stress_yz, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_zx, &buf_stress_zx, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_xx, &buf_strain_xx, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_yy, &buf_strain_yy, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_zz, &buf_strain_zz, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_xy, &buf_strain_xy, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_yz, &buf_strain_yz, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_zx, &buf_strain_zx, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    edge(
        poisson,
        core*core,
        cst_stress,
        cst_strain,
        buf_d_x.buf,
        buf_d_y.buf,
        buf_senses.buf,
        buf_m_x.buf,
        buf_m_y.buf,
        buf_keep.buf,
        buf_stress_xx.buf,
        buf_stress_yy.buf,
        buf_stress_zz.buf,
        buf_stress_xy.buf,
        buf_stress_yz.buf,
        buf_stress_zx.buf,
        buf_strain_xx.buf,
        buf_strain_yy.buf,
        buf_strain_zz.buf,
        buf_strain_xy.buf,
        buf_strain_yz.buf,
        buf_strain_zx.buf,
        index,
        buf_senses.shape[0]
    );
    return Py_None;
}

/**
 * Python screw wrapper function.
 *
 * @param PyObject
 * @param args
 * @return the strain energy density.
 */
static PyObject *py_screw(
    PyObject *self,
    PyObject *args
)
{
    double core;
    double cst_stress;
    double cst_strain;
    PyObject *obj_d_x; Py_buffer buf_d_x;
    PyObject *obj_d_y; Py_buffer buf_d_y;
    PyObject *obj_senses; Py_buffer buf_senses;
    PyObject *obj_m_x; Py_buffer buf_m_x;
    PyObject *obj_m_y; Py_buffer buf_m_y;
    PyObject *obj_keep; Py_buffer buf_keep;
    PyObject *obj_stress_xx; Py_buffer buf_stress_xx;
    PyObject *obj_stress_yy; Py_buffer buf_stress_yy;
    PyObject *obj_stress_zz; Py_buffer buf_stress_zz;
    PyObject *obj_stress_xy; Py_buffer buf_stress_xy;
    PyObject *obj_stress_yz; Py_buffer buf_stress_yz;
    PyObject *obj_stress_zx; Py_buffer buf_stress_zx;
    PyObject *obj_strain_xx; Py_buffer buf_strain_xx;
    PyObject *obj_strain_yy; Py_buffer buf_strain_yy;
    PyObject *obj_strain_zz; Py_buffer buf_strain_zz;
    PyObject *obj_strain_xy; Py_buffer buf_strain_xy;
    PyObject *obj_strain_yz; Py_buffer buf_strain_yz;
    PyObject *obj_strain_zx; Py_buffer buf_strain_zx;
    unsigned long long index;
    if (!PyArg_ParseTuple(
        args,
        "dddOOOOOOOOOOOOOOOOOOK",
        &core,
        &cst_stress,
        &cst_strain,
        &obj_d_x,
        &obj_d_y,
        &obj_senses,
        &obj_m_x,
        &obj_m_y,
        &obj_keep,
        &obj_stress_xx,
        &obj_stress_yy,
        &obj_stress_zz,
        &obj_stress_xy,
        &obj_stress_yz,
        &obj_stress_zx,
        &obj_strain_xx,
        &obj_strain_yy,
        &obj_strain_zz,
        &obj_strain_xy,
        &obj_strain_yz,
        &obj_strain_zx,
        &index
    ))
    {
        return NULL;
    }
    if (PyObject_GetBuffer(obj_d_x, &buf_d_x, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_d_y, &buf_d_y, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_senses, &buf_senses, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_m_x, &buf_m_x, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_m_y, &buf_m_y, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_keep, &buf_keep, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_xx, &buf_stress_xx, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_yy, &buf_stress_yy, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_zz, &buf_stress_zz, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_xy, &buf_stress_xy, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_yz, &buf_stress_yz, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_stress_zx, &buf_stress_zx, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_xx, &buf_strain_xx, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_yy, &buf_strain_yy, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_zz, &buf_strain_zz, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_xy, &buf_strain_xy, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_yz, &buf_strain_yz, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    if (PyObject_GetBuffer(obj_strain_zx, &buf_strain_zx, PyBUF_ANY_CONTIGUOUS | PyBUF_FORMAT) == -1) {return NULL;}
    screw(
        core*core,
        cst_stress,
        cst_strain,
        buf_d_x.buf,
        buf_d_y.buf,
        buf_senses.buf,
        buf_m_x.buf,
        buf_m_y.buf,
        buf_keep.buf,
        buf_stress_xx.buf,
        buf_stress_yy.buf,
        buf_stress_zz.buf,
        buf_stress_xy.buf,
        buf_stress_yz.buf,
        buf_stress_zx.buf,
        buf_strain_xx.buf,
        buf_strain_yy.buf,
        buf_strain_zz.buf,
        buf_strain_xy.buf,
        buf_strain_yz.buf,
        buf_strain_zx.buf,
        index,
        buf_senses.shape[0]
    );
    return Py_None;
}

static PyMethodDef StrainStressModule[] = {
    {
        "edge",
        py_edge,
        METH_VARARGS,
        "Compute the resulting strain and stress fields for edge dislocations."
    },
    {
        "screw",
        py_screw,
        METH_VARARGS,
        "Compute the resulting strain and stress fields for screw dislocations."
    },
    {
        NULL,
        NULL,
        0,
        NULL
    }
};

static struct PyModuleDef strainstressmodule = {
    PyModuleDef_HEAD_INIT,
    "strainstress", // module name
    NULL,  // module documentation
    -1,
    StrainStressModule
};

PyMODINIT_FUNC PyInit_strainstress(void)
{
    return PyModule_Create(&strainstressmodule);
}
