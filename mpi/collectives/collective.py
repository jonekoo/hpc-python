# -*- coding: utf-8 -*-
from mpi4py import MPI
import numpy



def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    if rank == 0:
        a = numpy.arange(8)
    else:
        a = numpy.empty(8, dtype=int)
    comm.Bcast(a, root=0)
    if rank == 1:
        print(a)


if __name__ == '__main__':
    main()
