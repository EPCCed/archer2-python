#
# ctypes coupling for mpi4py to C
#
# Requires, on the front end
#   module load PrgEnv-gnu
#   module load cray-python
#   make
#
# IMPORTANT
# mpi4py v 2.0 is required.

CC = cc
CFLAGS = -fPIC
TEST = test1

# Generate a shared object
module:	${TEST}.o
	${CC} -shared -o ${TEST}.so $<

# Compile the C source
${TEST}.o:	${TEST}.c
	${CC} -c ${CFLAGS} $<

clean:
	${RM} -rf *.o *.so
