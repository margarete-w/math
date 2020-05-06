# -*- coding: utf-8 -*-
"""
The mod adm1 that implements the Fourier Motzkin elemination.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

def read(path):
    """
    Reads the file located at path.

    :param path: The path to the document that contains Matrix/Polyhedron
    :type path: string
    :returns: The matrix A that is contained in the file path.
    :rtype: A is a list of lists
    """
    #print("Open file...")
    file = open(path, "r")
    A = parse(file)
    return A

def parse(file):
    """
    Constructs a matrix A that contains the values from file.
    :param file: contains the rows and columns of A
    :type file: list of strings
    :returns: A in case of a matrix, A|b in case of a polyhedron
    :rtype: list of lists
     """
    # kommentare rausnehmen
    file = [s.strip() for s in file if len(s.strip())> 0 and s.strip()[0] != "#" ]
    #print("Strip comments from file...")
    if file == []:
        return []
    isPolyhedron = file[0] =="A"
    if isPolyhedron:
        #Remove the first line, because it contains "A".
        file = file[1:]
        # Find the line index of b
        bIndex = file.index("b")
    #A is the constructed matrix.
    A = []
    # In the case that A is not a polyhedron:
    if not isPolyhedron:
        #Iterate through all the lines in file.
        for i in range(len(file)):
            # Construct a list of floats from the current line
            A.append([float(s) for s in file[i].split()])
    # If the matrix contained in file is a polyhedron:
    if isPolyhedron:
        for i in range(bIndex):
            #Construct a list of floats from the current line
            A.append([float(s) for s in file[i].split() if len(s)>0])
        b = file[bIndex +1].split()
        for i in range(len(A)):
            # Construct the vector b and add it to A as a column.
            A[i ].append(float(b[i]))
    #Testfunktion, Ueberprueft die Dimension von A
    a = len(A[0])
    for i in range(1, len(A)):
        if len(A[i]) != a:
            print("Dimension of A at row {} is {} but should be {}".format(i, len(A[i]), a))
    #print("Matrix reads:")
    #print("\n--- MATRIX --------------------")
    #printmatrix(A)
    #print("---------------------------------\n")
    return A

def write(A, output_file):
    """
    Writes the matrix A in the file output_file.
    :param A: a matrix
    :type A: list of list
    :param output_file: Where we will store the output_file
    :type output_file: string
     """
    print("Writing file to {}...".format(output_file))
    f = open(output_file, "w")
    s = "A\n"
    b = ""
    for row in A:
        s += ' '.join(str(float(n)) for n in row[:-1]) + "\n"
        b += str(float(row[-1])) + " "
    content = s + "b\n"+b.strip()+"\n"
    f.write(content)
    print("Writing done!")

#----------------------
# Matrix Operations
#----------------------

def printmatrix(B):
    """Prints the matrix B """
    for i in B:
        print(i)

def multiply(s, B):
    """
    Calculates C = s*B
    :param s: a scalar
    :type s: float
    :param B: a vector
    :type B: list of floats
    :returns: C
    """
    s = float(s)
    C = []
    for i in B:
        C.append( s * float(i))
    return C

def dec_multiply(s, B):
    C = []
    for i in B:
        C.append(s * Fraction(i))
    return C

def add(B,C):
    """
    Calculates D = B+C
    :param B, C: vectors
    :type B,C: lists containing floats
    :return D: D = B+C
    """
    assert len(B) == len(C), "Laenge der Vektoren stimmt nicht. dim(C)={}, dim(B)={}".format(len(C), len(B))
    D = []
    for i in range(len(B)):
        D.append(float(Decimal(B[i]) +Decimal(C[i])))
    return D

def add_dec(B,C):
    """
    Calculates D = B+C
    :param B, C: vectors
    :type B,C: lists containing floats
    :return D: D = B+C
    """
    assert len(B) == len(C), "Laenge der Vektoren stimmt nicht. dim(C)={}, dim(B)={}".format(len(C), len(B))
    D = []
    for i in range(len(B)):
        D.append(Fraction(B[i]) +Fraction(C[i]))
    return D

def transpose(A):
    """
    Transposes the matrix A.
    :param A: matrix
    :type A: list of lists
    """
    n = len(A)
    m = len(A[0])
    B = []
    for i in range(0,m):
        B.append([])
        for j in range(0,n):
            B[i].append(A[j][i])
    return B

def transpose_sparse(M):
    """
    Transposes the sparse matrix M. M is given as a tuple.
    The first component contains a list of triples (values, row, column)
    and the second component contains the shape of M as a tuple.
    :Example: ([(value_1, row_1, colum_1 ),....], (#rows, #columns))
    :param M: sparse matrix
    :returns: M^T
    """
    return ([(i[0], i[2], i[1]) for i in M[0]], (M[1][1], M[1][0]))

def matrix_vector(C, b):
    """
    Calculates c = C*b
    :param C: a sparse matrix
    :param b: a vector
    :type b: list of floats
    :returns: c
    :rtype: c: list of floats
    """
    M = C[0]
    Mshape = C[1]
    if M ==[]:
        return []
    assert len(b) == Mshape[1]
    c = [0]* Mshape[0]
    for i in M:
        c[i[1]] = Fraction(c[i[1]])+ Fraction(b[i[2]]) * Fraction(i[0])
    return c

def inner_product(a,b):
    """
    Returns the inner product a^Tb
    :param a, b: vectors
    :type a, b: lists of floats
    :returns: a^T *b
    :rtype: c: float
    """
    assert len(a) == len(b)
    c = Fraction(0)
    for i in range(len(a)):
        c = c + Fraction(a[i]) * Fraction(b[i])
    return c

def is_greater(a,b):
    """
    Compares if a >= b.
    :param a, b: vectors
    :type a,b: lists of floats
    :return: False if there is a component in b, such that
    b_i > a_i, otherwise True.
    """
    assert len(a) ==len(b)
    for i in range(len(a)):
        if a[i] < b[i]:
            return False
    return True


#----------------------
# Homework
#----------------------
from decimal import *
from fractions import Fraction

def dimension_reduction(C):

    """
    :param C: polyhedron in the form A|b in R^n.
    :type C: list of lists
    :return: B|b', (M, (row, cols)): B|b' is the projection of A|b in R^{n-1},
    M is the sparse matrix such that B|0 = M * A, b' = M* b .
    """
    #print("\tBeginning dimension reduction on A...")
    import copy
    if C == []:
        return [], ()
    assert len(C[0]) >= 2 , "EIFOK 42, spaltendimension von A ist zu klein {}".format(C)
    if len(C[0]) == 2:
        return C, ()
    B = []
    A = copy.deepcopy(C)

    #print("\t\tNormalize last column of A...")
    #for i in range(len(A)):
     #   pivot = A[i][-2]
      #  if pivot != 0:
       #     s = Fraction(abs(pivot))
        #    A[i] = dec_multiply(Fraction(1)/s, A[i])
    M = []
    row = 0
    cols = len(A)
    #print("\t\tRemove last column...")
    # Linear combination of rows whose last column have different signs
    for i in range(len(A)):
        pivot1 = A[i][-2]
        if pivot1 == 0:
            #Add the constraint to B and remove the last column.
            D = [Fraction(v) for v in A[i][:-2]] + [Fraction(A[i][-1])]
            B.append(D)
            # Construct M
            M.append((1, row, i))
            row = row +1
        else:
            for j in range(i+1, len(A)):
                #Look for all constraints where the pivot element has a different sign.
                pivot2 = A[j][-2]
                if pivot2 != 0:
                    if pivot1 * pivot2 < 0:
                        #Add the linear combination of all rows with a different
                        #sign to D
                        D = add_dec(multiply(abs(pivot2),A[i][:-2]), multiply(abs(pivot1),A[j][:-2]))+ [Fraction(abs(pivot2)*A[i][-1]) + Fraction(abs(pivot1)*A[j][-1])]
                        B.append(D)
                        #Construct M
                        M.append((Fraction(abs(pivot2)), row, i))
                        M.append((Fraction(abs(pivot1)), row, j))
                        row = row +1

    #print("\tDimension reduction done!")
    return B, (M, (row, cols))



def projection(input_file, k ,output_file):
    """
    Reads the polyhedron contained in input_file and returns the projection
    of the polyhedron in k-dimensions.
    :param input_file: the path to the file containing a polyhedron
    :type input_file: string
    :param k: the dimension in which the polyhedron is projected
    :type k: int
    :param output_file: the path where the projection is stored
    :type output_file: string
     """
    k = int(k)
    #reads input file
    A = read(input_file)
    A = __proj(A, k)
    #write A in output_file
    write(A, output_file)

def __proj(A, k):
    """
    Projects the matrix A in R^k.
    :param A: matrix
    :type A: list of lists
    :param k:
    :type k: int
    :returns: A: the projection of A in R^k
    :type: A: list of lists
    """
    # empty matrix check
    if len(A)== 0:
        return A
    n = len(A[0])-1
    #print("Start projecting on dimension {}...".format(k))
    #apply dimension reduction n-k times
    for i in range(0, n-k):
        #print("\tProjection on dimension={}".format(n-i-1))
        A, _ = dimension_reduction(A)
        #print("-------- MATRIX -------------------")
        #printmatrix(A)
        #print("-----------------------------------")
        #print("\n")
    return A

def image(input_polyhedron, input_matrix, output_file):
    """
    Computes M*P = {M*x : x in P} and stores it in a file.

    :param input_polyhedron: the path to the polyhedron
    :type input_polyhedron: string
    :param input_matrix: the path to the matrix M
    :type input_matrix: string
    :param output_file: the path where M*P is stored
    :type output_file: string
    """
    A = read(input_polyhedron)
    M = read(input_matrix)
    Qk = __image(A,M)
    write(Qk, output_file)

def __image(A,M):
    """
    A = A'|b
    Calculates M*A = pi_m ({(y,x) in R^m+n | M*x -y= 0 for x in A }) =
    pi_m({ (y, x) in R^{m+n}| |-I   M |   | x |    | 0 | 
                              | I  -M | * |   | >= | 0 | 
                              | 0   A |   | y |    | b | })
    :param A: a polyhedron
    :type A: list of lists
    :param M: a matrix
    :type M: list of lists
    :returns: Q_k: M*A
    :rtype: Q_k: list of lists
     """
    m = len(A)
    if len(M) == 0:
        print("M is empty")
        return None
    n = len(M[0])
    k = len(M)
    # Construct the matrix :
    # |-I   M  0 |
    # | I  -M  0 |
    # | 0   A  b |
    I1= []
    I2 = []
    for i in range(0,k):
        I1.append([])
        I2.append([])
        for j in range(0,k):
            if j ==i :
                I1[i].append(1)
                I2[i].append(-1)
            else:
                I1[i].append(0)
                I2[i].append(0)
    Q1 = []
    Q2 = []
    for i in range(0,k):
        Q1.append(I2[i]+ M[i]+ [0])
        Q2.append(I1[i]+ multiply(-1.0, M[i])+ [0])
    Q3 = []
    for i in range(0,m):
        Q3.append([0]*k+ A[i])

    Q = Q1 +Q2 + Q3
    # Project the constructed matrix
        # |-I   M  0 |
        # | I  -M  0 |
        # | 0   A  b | in k dimensions
    Qk = __proj(Q, k)
    return Qk

def H_representation(input_file, output_file):
    """
    Computes the convex hull of the set of vectors specified in input_file
    and stores the resulting polyhedron in output_file.
    :param input_file: the path where the vectors are stored
    :type input_file: string
    :param output_file: the path to the file where the convex hull is stored
    :type output_file: string
    conv(x_1,...,x_k) = A*P with
    A = (x_1,...,x_k) in R^{n x k}
    and P = { lambda in R^{k}| lambda_i >= 0, sum_{i = 1}^k lambda_i = 1 }
    """
    # load matrix whose rows are the vectors x_1,...,x_k
    A = read(input_file)
    A = transpose(A)
    k = len(A[0])
    #Construct the polyhedron P
    I = []
    I1 = [[1.0]*(k+1)]
    I2 = [[-1.0]*(k+1)]
    for i in range(0,k):
        I.append([])
        for j in range(0,k+1):
            if i == j :
                I[i].append(1.0)
            else:
                I[i].append(0.0)
    P = I + I1 +I2
    #Calculate A*P
    D = __image(P, A)
    write(D, output_file)

def base_case(P):
    """
    P is a polyhedron in R^1, given by P = {x in R^1| a^T*x >=b}, a in R^m.
    Check if P is empty, if so construct y such that y^T*a = 0 and y^T*b>0,
    otherwise return x in P.
    :param P: polyhedron in R^1
    :type P: list of lists
    :return: False, y if is empty, such that y^T*a = 0 and y^T*b > 0,
    otherwise True, x such that x in P.
     """
    import math
    #check if P is empty
    if len(P) ==0:
        return True, [Fraction(0.0)]
    # check for impossible constraint a_i^Tx > b, where a_i = 0 and b positive
    for i in range(len(P)):
        if P[i][0] ==0 and P[i][1] > 0:
            y = [0]* len(P)
            y[i] = 1
            assert abs(inner_product(y, transpose(P)[0])) < 10**(-12)
            assert inner_product(y, transpose(P)[1]) > 0
            # impossible constraint found and return that P is empty
            return False, y
    lowerbound = - math.inf
    upperbound = math.inf
    lbIndex = None
    ubIndex = None
    # calculate lower and upperbound for x
    for i in range(len(P)):
        # find greatest lowerbound
        if P[i][0] > 0 and P[i][1] / P[i][0] > lowerbound:
            lowerbound =   Fraction(P[i][1]) / Fraction(P[i][0])
            lbIndex = i
        # find smallest upperbound
        if P[i][0] < 0 and P[i][1] / P[i][0] < upperbound:
            upperbound = Fraction(P[i][1]) / Fraction(P[i][0])
            ubIndex = i
    # construct y if lowerbound is greater than upperbound
    if lowerbound > upperbound :
        y = [0] *len(P)
        #y[lbIndex] = 1
        #y[ubIndex] = Fraction(P[lbIndex][0]) / Fraction((- P[ubIndex][0]))
        y[lbIndex] = Fraction(-P[ubIndex][0])
        y[ubIndex] = Fraction(P[lbIndex][0])
        #check that y^T*a = 0 and y^T *b > 0.
        assert abs(inner_product(y, transpose(P)[0])) < 10**(-12)
        assert inner_product(y, transpose(P)[1]) > 0
        return False, y
    # return feasible x_1 if lowerbound is smaller than upperbound
    if lowerbound <= upperbound:
        x = lowerbound if lowerbound != -math.inf else upperbound
        if lowerbound != -math.inf and upperbound != math.inf:
            x = lowerbound
        elif lowerbound == -math.inf and upperbound != math.inf:
            x = upperbound 
        elif lowerbound != -math.inf and upperbound == math.inf:
            x = lowerbound 
        elif lowerbound == -math.inf and upperbound == math.inf:
            x = 10000
        # check that a*x >= b
        #assert is_greater(multiply(x, transpose(P)[0]), transpose(P)[1])
        return True, [Fraction(x)]

def compute_x_or_y(input_file):
    """
    P is the polyhedron stored in path input_file. P in R^n, given by
    P = {x in R^n| A*x >=b}, A in R^{m x n}.
    Check if P is empty, if so construct y such that y^T*A = 0 and y^T*b>0,
    otherwise return x in P.
    :param P: polyhedron
    :type P: list of lists
    :return: False, y if is empty, such that y^T*A = 0 and y^T*b > 0,
    otherwise True, x such that x in P.
     """
    P = read(input_file)
    for i in range(0, len(P)):
        P[i] = [Fraction(p) for p in P[i]]

    n = len(P[0])-1
    History = [(P, None)]
    B = P
    #Project P onto R^1
    for i in range(0,n-1):
        B, M= dimension_reduction(B)
        History.append((B,M))
    #Check if the projection onto R^1 is empty
    NotEmpty, z = base_case(History[-1][0])
    History = History[::-1]
    # Construct y in the case that P is empty y_{n}= M^T_{n} y_{n-1}
    if not NotEmpty:
        for Q,M in History[:-1]:
            B = transpose_sparse(M)
            z = matrix_vector( B, z)
            #test3(Q, z)
        #test3(P,z)
        return False, [float(v) for v in z]
    #Construct x in P if P is not empty
    if NotEmpty :
        for Q, _ in History[1:]:
            z = step(Q, z)
            #test4(Q,z)
        return True, [float(v) for v in z]



def step(P, x):
    """
    Calculates a new component of x_{old}, such that x_{new} in P.
    :param P: polyhedron in R^m
    :type P: list of lists
    :param x: a vector in R^{m-1}
    :type x: list of floats
    :return: x_{new}: a vector such that x_{new} in P
    :rtype: x_{new}: list of floats
    """
    import math
    C = []
    #Substitute x_old in P
    for i in range(0, len(P)):
        C.append([Fraction(P[i][-2]), Fraction(P[i][-1])- Fraction(inner_product(x, P[i][:-2]))])
    lowerbound = - math.inf
    upperbound = math.inf
    lbIndex = None
    ubIndex = None
    # calculate lower and upperbound for new component of x_new
    for i in range(len(C)):
        # find greatest lower bound
        if C[i][0] > 0 and Fraction(C[i][1]) / Fraction(C[i][0]) > lowerbound:
            lowerbound =  Fraction(C[i][1]) / Fraction(C[i][0])
            lbIndex = i
        # find smallest upperbound
        if C[i][0] < 0 and Fraction(C[i][1]) / Fraction(C[i][0]) < upperbound:
            upperbound = Fraction(C[i][1]) / Fraction(C[i][0])
            ubIndex = i
    assert upperbound >= lowerbound or abs(lowerbound -upperbound) < 10**(-12)
    if lowerbound != -math.inf and upperbound != math.inf:
        w = [Fraction(lowerbound+upperbound)/2.0]
    elif upperbound != math.inf:
        w = [math.floor(upperbound)]
    elif lowerbound != -math.inf:
        w = [math.ceil(lowerbound)]
    if lowerbound == -math.inf and upperbound == math.inf:
        w = [0.0]
    return x+ w



# TEST INSTANCES

def test():
    file = open("project_instances.dat", "r")
    setup = []
    instance = None # {"k": , "data": ""}
    content = ""
    for line in file:
        if len(line) == 0:
            continue
        if line[0] == "k":
            if instance != None:
                instance["data"] = content
                setup.append(instance)
                content = ""
            kValue = int(line.strip()[-1])
            instance = {"k": kValue, "data": None}
        else:
            content += line

    k = []
    for i in range(len(setup)):
        f = open("test/test{}.dat".format(i),"w")
        content = setup[i]["data"]
        f.write(content)
        f.close()

        k.append(setup[i]["k"])

    for i in range(len(k)):
        projection("test/test{}.dat".format(i), k[i], "test/solution.dat")

    print("done")

# Test if y^TA = 0 and y^Tb > 0
def test3(P, z):
    import numpy as np
    P = np.array(P)
    z = np.array(z)
    b = P[:,-1]
    A = P[:,:-1]
    assert np.allclose(z.transpose().dot(A), np.zeros(A.shape[1]))
    assert z.transpose().dot(b) > 0

# Test if Ax >= b
def test4(P, z):
    import numpy as np
    P = np.array(P)
    print(P, z)
    z = np.array(z)
    A = P[:,:-1]
    b = P[:,-1]
    assert np.count_nonzero(A.dot(z) >= b) == A.shape[0]

def test():
    import numpy as np
    p = [0.5194319805081822, 1.4903577379741426, 1.4151531151338057]
    Ab = np.array(read("outfile.ot"))
    b = np.array(Ab[:,-1])
    A = np.array(Ab[:,:-1])
    print(np.count_nonzero(A.dot(p) >= b) == A.shape[0])
