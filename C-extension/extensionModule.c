#include </usr/local/Cellar/python3/3.5.1/Frameworks/Python.framework/Versions/3.5/include/python3.5m/Python.h>

//TODO: median

static PyObject* exmod_median(PyObject *self, PyObject * args){

    int length;

    PyObject * listObj;
    PyObject * valObj;
    long value;
    float fvalue;
    float temp;

    if (! PyArg_ParseTuple( args, "O", &listObj)) return NULL;
    length = PyList_Size(listObj);

    float x[length];
    /* should raise an error here. */
    if (length < 0)   return NULL; /* Not a list */

    for (int i=0; i<length; i++) {

        /* grab the integer object from the next element of the list */
        valObj = PyList_GetItem(listObj, i);
        value = PyLong_AsLong(valObj);
        fvalue = (float) value;
        x[i] = fvalue;
    }

    for(int i=0; i<length-1; i++) {
        for(int j=i+1; j<length; j++) {
            if(x[j] < x[i]) {
                // swap elements
                temp = x[i];
                x[i] = x[j];
                x[j] = temp;
            }
        }
    }

    if(length%2==0) {
        // if there is an even number of elements, return mean of the two elements in the middle
        return Py_BuildValue("d",((x[length/2] + x[length/2 - 1]) / 2.0));
    } else {
        // else return the element in the middle
        return Py_BuildValue("d", x[length/2]);
    }

}

//TODO: mean

static PyObject* exmod_mean(PyObject *self, PyObject * args){

    int length;

    PyObject * listObj;
    PyObject * valObj;
    long value;
    float fvalue;
    float sum = 0.0;

    if (! PyArg_ParseTuple( args, "O", &listObj)) return NULL;
    length = PyList_Size(listObj);

    float x[length];
    /* should raise an error here. */
    if (length < 0)   return NULL; /* Not a list */

    for (int i=0; i<length; i++) {

        /* grab the integer object from the next element of the list */
        valObj = PyList_GetItem(listObj, i);
        value = PyLong_AsLong(valObj);
        fvalue = (float) value;
        x[i] = fvalue;
        sum = sum + fvalue;
    }

    return Py_BuildValue("f", (sum/length));


}

static PyObject* exmod_variance(PyObject *self, PyObject * args){

    int length;       /* how many lines we passed for parsing */

    PyObject * listObj; /* the list of integers */
    PyObject * valObj;
    long value;
    float fvalue;
    float mean, var, dev, sum = 0.0, sdev = 0.0;
    /* the O parses for a Python object (listObj) */
    if (! PyArg_ParseTuple( args, "O", &listObj)) return NULL;

    /* get the number of lines passed to us */
    length = PyList_Size(listObj);
    float x[length];
    /* should raise an error here. */
    if (length < 0)   return NULL; /* Not a list */

    for (int i=0; i<length; i++) {

        /* grab the integer object from the next element of the list */
        valObj = PyList_GetItem(listObj, i);
        value = PyLong_AsLong(valObj);
        fvalue = (float) value;
        x[i] = fvalue;
        sum = sum + fvalue;
    }
    mean = sum/length;

    for (int i = 0; i<length; i++) {
        dev = (x[i] - mean)*(x[i] - mean);
        sdev = sdev + dev;
    }
    var = sdev/length;

    return Py_BuildValue("f", var);
}

static PyMethodDef exmod_methods[] = {
    {"var", exmod_variance, METH_VARARGS, "Get variance of a list of arguments"},
    {"mean", exmod_mean, METH_VARARGS, "Get mean of a list of arguments"},
    {"median", exmod_median, METH_VARARGS, "Get median of a list of arguments"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef extensionModule =
        {
                PyModuleDef_HEAD_INIT,
                "extensionModule", /* name of module */
                "",          /* module documentation, may be NULL */
                -1,          /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
                exmod_methods
        };

PyMODINIT_FUNC PyInit_exmod(void){
    return PyModule_Create(&extensionModule);

}

int main(){
    printf("This code runs without errors");
}
