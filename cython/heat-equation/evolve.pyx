import numpy as np
cimport numpy as np
cimport cython


DTYPE = np.double
ctypedef np.double_t DTYPE_t


@cython.boundscheck(False)
@cython.wraparound(False)
@cython.cdivision(True)
def evolve(np.ndarray[DTYPE_t, ndim=2] u, 
           np.ndarray[DTYPE_t, ndim=2] u_previous, double a, double dt,
           double dx2, double dy2):
    """Explicit time evolution.
       u:            new temperature field
       u_previous:   previous field
       a:            diffusion constant
       dt:           time step. """

    cdef int n = u.shape[0]
    cdef int m = u.shape[1]
    cdef int i, j

    cdef double dx2inv = 1. / dx2
    cdef double dy2inv = 1. / dy2

    for i in range(1, n-1):
        for j in range(1, m-1):
            u[i, j] = u_previous[i, j] + a * dt * ( \
             (u_previous[i+1, j] - 2*u_previous[i, j] + \
              u_previous[i-1, j]) * dx2inv + \
             (u_previous[i, j+1] - 2*u_previous[i, j] + \
                 u_previous[i, j-1]) * dy2inv )
    u_previous[:] = u[:]

