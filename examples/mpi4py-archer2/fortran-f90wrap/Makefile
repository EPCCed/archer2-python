#
#  Fortran from mpi4py via f90wrap
#
#  This requires f90wrap be installed. Briefly,
#
#  IMPORTANT: The C compiler used must be the same as that used to
#  compile mpi4py. If, at run time, you see the error 
#
#  "Attempting to use an MPI routine before initializing MPICH"
#
#  it suggests a mismatch. Use ldd to check exactly which version
#  is involved in mpi4py .so file and the _fortran.so file
#
#  It is likely you need to load the PrgEnv-gnu
#  module load PrgEnv-gnu
#
#


TEST=test1
EXT_MODULE_NAME=fortran

# Compile the extension module
_${EXT_MODULE_NAME}.so:	${TEST}.o f90wrap_${TEST}.f90
	f2py-f90wrap -c --f90exec=ftn -m _${EXT_MODULE_NAME} ${TEST}.o f90wrap_${TEST}.f90

# Generate the module.py and wrapped f90 files
f90wrap_${TEST}.f90: ${TEST}.f90
	f90wrap -m ${EXT_MODULE_NAME} ${TEST}.f90

# Compile the source
${TEST}.o:	${TEST}.f90
	ftn -c -fPIC $^


clean:
	rm -rf ${EXT_MODULE_NAME}.py *.so f90wrap_${TEST}.f90 ${TEST}.o ${TEST}.mod *.pyc
