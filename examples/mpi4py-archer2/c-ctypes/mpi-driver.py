# Requires invocation by python interpreter on back end.
# MUST HAVE mpi4py >= v2.0.0; there is no (easy) way to
# obtain the type of the MPI_Comm handle in 1.3.1

import ctypes
import sys

from mpi4py import MPI

def main(argv):
    rank = MPI.COMM_WORLD.rank
    size = MPI.COMM_WORLD.size
    sys.stdout.write("Hello from rank {:2d} of {:2d}\n".format(rank, size))

    if rank == 0:
        print("mpi4py version is: ", MPI.Get_version())
        print("Size of int", ctypes.sizeof(ctypes.c_int))
        print("Size of void *", ctypes.sizeof(ctypes.c_void_p))

    # No checking
    lib = ctypes.CDLL("./test1.so")

   # Work out the type of the MPI_Comm opaque handle

    if MPI._sizeof(MPI.Comm) == ctypes.sizeof(ctypes.c_int):
        handle_ctype = ctypes.c_int
    else:
        handle_ctype = ctypes.c_void_p

    lib.mpi_c_operation.argtypes = [handle_ctype]
    lib.mpi_c_operation.restype  = ctypes.c_int

    ptr = MPI._addressof(MPI.COMM_WORLD)
    comm = handle_ctype.from_address(ptr)

    lib.mpi_c_operation(comm)

    return 0


# Execute

if __name__ == "__main__":
    main(sys.argv[1:])

