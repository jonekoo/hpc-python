from mpi4py import MPI


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    print("The comm size is ", size, "My rank is ", rank)
 

if __name__ == '__main__':
    main()
