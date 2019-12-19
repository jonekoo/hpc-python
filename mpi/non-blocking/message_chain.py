# -*- coding: utf-8 -*-
"""Every task with a rank less than ntasks-1 sends a message to task myid+1.
For example, task 0 sends a message to task 1.

The message content is an integer array where each element is initialized
to myid.

The sender prints out the number of elements it sends.

All tasks with rank ≥ 1 receive messages.
Each receiver prints out their myid, and the first element in the received
array."""
from mpi4py import MPI
import numpy


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    msgsize = 100
    data = numpy.full(msgsize, rank, dtype=int)
    buff = numpy.empty(msgsize, dtype=int)

    dest = rank + 1
    src = rank - 1
    # These take care of boundaries
    if rank == size - 1:
        dest = MPI.PROC_NULL
    if rank == 0:
        src == MPI.PROC_NULL

    if rank < size - 1:
        print('Rank', rank, 'sending', len(data), 'elements.')
    sendreq = comm.Isend(data, dest=dest)
    recvreq = comm.Irecv(buff, source=src)
    recvreq.wait()
    if rank > 0:
        print('Rank', rank, 'received array with first element', buff[0])
    sendreq.wait()


if __name__ == '__main__':
    main()
