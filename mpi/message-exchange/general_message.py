from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    msg = {'rank': rank}
    if rank == 0:
        comm.send(msg, dest=1)
        buff = comm.recv(source=1)
    elif rank == 1:
        buff = comm.recv(source=0)
        comm.send(msg, dest=0)
    print('Rank', rank, 'received', buff)


if __name__ == '__main__':
    main()
