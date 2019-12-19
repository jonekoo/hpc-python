from mpi4py import MPI
import numpy

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

assert size == 4, 'Number of MPI tasks has to be 4.'

if rank == 0:
    print('First collective:')

# TODO: create data vector at task 0 and send it to everyone else
#       using collective communication
if rank == 0:
    data = numpy.arange(8)
else:
    data = numpy.empty(8, dtype=int)
comm.Bcast(data, root=0)

print('  Task {0}: {1}'.format(rank, data))
comm.barrier()

# Prepare data vectors ..
data = numpy.arange(rank*8, (rank+1)*8)  # create the data vectors
# .. and receive buffers
buff = numpy.full(8, -1, int)


# ... wait for every rank to finish ...
comm.barrier()
if rank == 0:
    print('')
    print('-' * 32)
    print('')
    print('Data vectors:')
print('  Task {0}: {1}'.format(rank, data))
comm.barrier()
if rank == 0:
    print('')
    print('c)')

# TODO: how to get the desired receive buffer using a single collective
#       communication routine?
comm.Scatter(data, buff[0:2], root=0)

print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('d)')

# TODO: how to get the desired receive buffer using a single collective
#       communication routine?
comm.Gather(data[0:2], buff, root=1)
 
print('  Task {0}: {1}'.format(rank, buff))

# ... wait for every rank to finish ...
buff[:] = -1
comm.barrier()
if rank == 0:
    print('')
    print('e)')

# TODO: how to get the desired receive buffer using a single collective
#       communication routine?
color = rank // 2
local_comm = comm.Split(color)
local_comm.Reduce(data, buff, op=MPI.SUM, root=0)

print('  Task {0}: {1}'.format(rank, buff))

