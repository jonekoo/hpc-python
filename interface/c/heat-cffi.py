from __future__ import print_function
import numpy as np
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from cffi import FFI

ffi = FFI()
lib = ffi.dlopen("evolve.dll")
ffi.cdef("""
         void evolve(double *u, double *u_previous, int nx, int ny,
                     double a, double dt, double dx2, double dy2);
         """)

# Set the colormap
plt.rcParams['image.cmap'] = 'BrBG'

# Basic parameters
a = 0.5                # Diffusion constant
timesteps = 200        # Number of time-steps to evolve system
image_interval = 4000  # Write frequency for png files

# Grid spacings
dx = 0.01
dy = 0.01
dx2 = dx**2
dy2 = dy**2

# For stability, this is the largest interval possible
# for the size of the time-step:
dt = dx2*dy2 / ( 2*a*(dx2+dy2) )

def init_fields(filename):
    # Read the initial temperature field from file
    field = np.loadtxt(filename)
    field0 = field.copy() # Array for field of previous time step
    return field, field0

def write_field(field, step):
    plt.gca().clear()
    plt.imshow(field)
    plt.axis('off')
    plt.savefig('heat_{0:03d}.png'.format(step))

def iterate(field, field0, timesteps, image_interval):
    field_ptr = ffi.cast("double *", ffi.from_buffer(field))
    field0_ptr = ffi.cast("double *", ffi.from_buffer(field0))
    nx, ny = field.shape
    for m in range(1, timesteps+1):
        lib.evolve(field_ptr, field0_ptr, nx, ny, a, dt, dx2, dy2)
        if m % image_interval == 0:
            write_field(field, m)


def main():
    # Initialise the temperature field
    field, field0 = init_fields('bottle.dat')
    # Plot/save initial field
    write_field(field, 0)
    # Iterate
    t0 = time.time()
    iterate(field, field0, timesteps, image_interval)
    t1 = time.time()
    # Plot/save final field
    write_field(field, timesteps)

    print("Running time: {0}".format(t1-t0))

if __name__ == '__main__':
    main()
