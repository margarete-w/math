A = [1 6 1; 2 3 2; 4 2 1];b = [1 0 0];[LU,z] = luDecomposition(A);mySolution = solveEq(LU,b, z);matlabSolution = A\b';