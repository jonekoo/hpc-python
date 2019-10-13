from mpi4py import MPI
import numpy


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    data = numpy.full(100000, rank, dtype=int)
    buff = numpy.empty(100000, dtype=int)
    
    # assuming that there are an even number of processes
    if rank % 2 == 0:
        partner = rank + 1
        comm.Send(data, dest = partner)
        comm.Recv(buff, source = partner)
    else:
        partner = rank - 1
        comm.Recv(buff, source = partner)
        comm.Send(data, dest = partner)
    
    if all(buff == partner): 
        print('Rank', rank, 'received array with size', buff.size,
              'full of ', partner)
    else:
        print('Rank', rank, 'failed communication')


if __name__ == '__main__':
    main()
