
# Fourier Motzkin Elemination

An algorithm that projects any polyhedron in a *n*-dimensional space onto a *n-1* dimensional space.

## How-To

Open your terminal and navigate to the directory that contains the file `fourier-motzkin.sh`. The following commands are possible:

### project

    ./fourier-motzkin.sh project test/A.test 2 test/project.result

Result:

    A
	0.0 -2.0
	2.0 0.0
	-2.0 0.0
	0.0 2.0
	b
	-2.0 -2.0 -2.0 -2.0


### image

    ./fourier-motzkin.sh image test/A.test test/M.test test/image.result

Result:

	A
	-1.0 -1.0
	-0.6666666666666667 -0.6666666666666667
	0.0 -1.0
	-1.0 0.0
	-1.0 -0.5
	-1.0 -1.0
	0.0 0.0
	-1.0 1.0
	-0.6666666666666667 1.3333333333333333
	0.0 1.0
	-1.0 2.0
	-1.0 1.5
	-1.0 1.0
	-1.0 0.0
	-0.6666666666666667 0.3333333333333333
	0.0 0.0
	-1.0 1.0
	-1.0 0.5
	-1.0 0.0
	0.0 0.0
	0.0 -1.0
	0.3333333333333333 -0.6666666666666667
	1.0 -1.0
	0.0 0.0
	0.0 -0.5
	0.0 -1.0
	1.0 -1.0
	0.0 0.0
	0.0 -0.5
	0.0 0.0
	0.0 -1.0
	1.3333333333333333 -0.6666666666666667
	2.0 -1.0
	1.0 0.0
	1.0 -0.5
	1.0 -1.0
	0.3333333333333333 0.3333333333333333
	1.0 0.0
	0.0 1.0
	0.0 0.5
	0.0 0.0
	0.3333333333333333 -0.16666666666666669
	1.0 -0.5
	0.0 0.5
	0.0 0.0
	0.0 -0.5
	0.3333333333333333 0.3333333333333333
	1.0 0.0
	0.0 1.0
	0.0 1.0
	0.0 0.5
	0.0 0.0
	0.0 0.0
	b
	-2.0 -1.3333333333333333 -2.0 -2.0 -2.0 -2.0 0.0 -2.0 -1.3333333333333333 -2.0 -2.0 -2.0 -2.0 -2.0 -1.3333333333333333 -2.0 -2.0 -2.0 -2.0 0.0 -2.0 -1.3333333333333333 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0 -1.3333333333333333 -2.0 -2.0 -2.0 -2.0 -1.3333333333333333 -2.0 -2.0 -2.0 -2.0 -1.3333333333333333 -2.0 -2.0 -2.0 -2.0 -1.3333333333333333 -2.0 -2.0 -2.0 -2.0 -2.0 -2.0

### H_representation
    ./fourier-motzkin.sh H_representation test/A.test test/H_representation.result

### compute_x_or_y
Command:

    ./fourier-motzkin.sh compute_x_or_y

Result:

	--------- RESULT ------------------------------------------------------------
	|
	|  Polyhedron is empty: False
	|  It contains the point x=[-1.0, -1.0, -1.0]
	|
	----------------------------------------------------------------------------

Command:

    ./fourier-motzkin.sh compute_x_or_y


Result:

	--------- RESULT ------------------------------------------------------------
	|
	|  Polyhedron is empty: True
	|  It satisfies y^TA=0 and y^Tb > 0 with point y=[1]
	|
	----------------------------------------------------------------------------
