#
#  Fortran from mpi4py via f2py
#
#  TO compile on the front-end, you need:
#
#  module restore PrgEnv-gnu
#  module load cray-python
#
#  make
#
#
#  IMPORTANT: The compiler used must be the same as that used to
#  compile mpi4py. If, at run time, you see the error 
#
#  "Attempting to use an MPI routine before initializing MPICH"
#
#  it suggests a mismatch. Use ldd to check exactly which version
#  is involved in mpi4py .so file and the wrapper.so file

FC = ftn

fortran.so: test.pyf
	f2py --f90exec=${FC} -c test.pyf test.f90

test.pyf: test.f90
	f2py test.f90 -m fortran -h test.pyf

clean:
	rm -rf fortran.*.so test.pyf
