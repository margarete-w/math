def read(path):
    print("open file")
    file = open(path, "r")
    A = parse(file)
    return A

def parse(file):
    # kommentare rausnehmen 
    file = [s.strip() for s in file if len(s.strip())> 0 and s.strip()[0] != "#" ]
    print("strip file")
    if file == []:
        return []
    isPolyhedron = file[0] =="A"
    print("polyhedron", isPolyhedron)
    if isPolyhedron:
        file = file[1:]
        bIndex = file.index("b")
        print("index von b", bIndex)
    A = []
    if not isPolyhedron:
        for i in range(len(file)):
            A.append([float(s) for s in file[i].split()])
    if isPolyhedron:
        for i in range(bIndex):
            A.append([float(s) for s in file[i].split() if len(s)>0])
        b = file[bIndex +1].split()
        for i in range(len(A)):
            A[i ].append(float(b[i]))
    #Testfunktion, Überprüft die Dimension von A 
    a = len(A[0])
    for i in range(1, len(A)):
        if len(A[i]) != a:
            print("Dimension of A at row {} is {} but should be {}".format(i, len(A[i]), a))
    printmatrix(A)
    return A

def write(A, output_file):
    f = open(output_file, "a")
    s= "A\n"
    w = ""
    for i in range(len(A)):
        s = s+ str(A[i][:-1]).strip("[]").replace(",", "") + "\n"
        w = w + " "+ str(A[i][-1])
    c = s + "b\n"+w.strip()+"\n"
    f.write(c)

#----------------------
# Matrix Operations
#----------------------

def printmatrix(B):
    for i in B:
        print(i)

def multiply(s, B): 
    C = []
    for i in B: 
        C.append( s * i)
    return C 

def add(B,C):
    if len(B) != len(C):
        print("Länge der Vektoren stimmt nicht", len(C), len(B))
    D = []
    for i in range(len(B)):
        D.append(B[i] +C[i])
    return D
def transpose(A): 
    n = len(A)
    m = len(A[0])
    B = []
    for i in range(0,m):
        B.append([])
        for j in range(0,n):
            B[i].append(A[j][i])
    return B 

def transpose_sparse(M):
    return ([(i[0], i[2], i[1]) for i in M[0]], (M[1][1], M[1][0]))

def matrix_vector(C, b):
    # berechnet M*b = c, M gespeichert als Triple: (value, row , column )
    M = C[0]
    Mshape = C[1]
    if M ==[]:
        return []
    print("b", len(b), Mshape)
    assert len(b) == Mshape[1]
    c = [0]* Mshape[0]
    for i in M:
        c[i[1]] = c[i[1]]+ b[i[2]] * i[0]
    return c
def inner_product(a,b):
    assert len(a) == len(b)
    c = 0
    for i in range(len(a)):
        c = c + a[i] * b[i]
    return c
def is_greater(a,b):
    assert len(a) ==len(b)
    for i in range(len(a)):
        if a[i] < b[i]:
            return False
    return True 


#----------------------
# Homework
#----------------------

def dimension_reduction(C):
    print("Beginning dimension reduction...")
    import copy
    if C == []:
        return C
    if len(C[0]) < 2:
        assert False , "EIFOK 42, spaltendimension von A ist zu klein {}".format(C)
    if len(C[0]) == 2:
        return C
    B = []
    A = copy.deepcopy(C)

    print("Normalize last column of A...")
    for i in range(len(A)):
        pivot = A[i][-2]
        if pivot != 0:
            A[i] = multiply(1.0/abs(pivot), A[i])
    M = []
    row = 0 
    cols = len(A)
    print("Linear combination of rows whose last column have different signs...")
    for i in range(len(A)):
        pivot1 = A[i][-2]
        if pivot1 == 0:
            D = A[i][:-2] + [A[i][-1]]
            B.append(D)
            # die i-te zeile von C wird übernommen in B
            M.append((1, row, i))
            row = row +1
        else:
            for j in range(i+1, len(A)):
                pivot2 = A[j][-2]
                if pivot2 != 0:
                    if pivot1 * pivot2 < 0:
                        D = add(A[i][:-2], A[j][:-2])+ [A[i][-1] + A[j][-1]]
                        B.append(D)
                        # die addition der j-ten und i-ten Zeile wird in M gespeichert
                        M.append((abs(1.0/C[i][-2]), row, i))
                        M.append((abs(1.0/C[j][-2]), row, j))
                        row = row +1
    #if B == []:
        #B = [[0,0]]
    return B, (M, (row, cols))



def projection(input_file, k ,output_file):
    #reads input file 
    A = read(input_file)
    A = __proj(A, k)
    print("writing...")
    #write A in output_file
    write(A, output_file)

def __proj(A, k): 
    # empty matrix check
    if len(A)== 0: 
        return A
    n = len(A[0])-1
    #apply dimension reduction n-k times
    for i in range(0, n-k):
        A, _ = dimension_reduction(A)
        print("\nProjection on dimension={}\n".format(n-i-1))
        printmatrix(A)
        print("\n\n")
    return A 

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

def image(input_polyhedron, input_matrix, output_file):
    A = read(input_polyhedron)
    M = read(input_matrix)
    Qk = __image(A,M)
    write(Qk, output_file)

def __image(A,M):
    m = len(A)
    if len(M) == 0:
        print("M is empty")
        return None
    n = len(M[0])
    k = len(M)
    print(k , "die länge von M ")
    # kxk Einheitsmatrix
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
        Q2.append(I1[i]+ multiply(-1, M[i])+ [0])
    Q3 = []
    for i in range(0,m):
        Q3.append([0]*k+ A[i])

    Q = Q1 +Q2 + Q3
    #print("Q")
    #printmatrix(Q)
    Qk = __proj(Q, k)
    return Qk

def H_representation(input_file, output_file):
    X = read(input_file)
    X = transpose(X)
    k = len(X[0])
    I = []
    I1 = [[1]*(k+1)]
    I2 = [[-1]*(k+1)]
    for i in range(0,k):
        I.append([])
        for j in range(0,k+1):
            if i == j : 
                I[i].append(1)
            else:
                I[i].append(0)
    Q = I + I1 +I2

    D = __image(Q, X)

    write(D, output_file)

def base_case(P):
    import math 
    #check if P is empty 
    if len(P) ==0:
        return True, [42]
    # check for impossible constrain 0 > b, b positive 
    for i in range(len(P)):
        if P[i][0] ==0 and P[i][1] > 0:
            y = [0]* len(P)
            y[i] = 1
            assert abs(inner_product(y, transpose(P)[0])) < 10**(-12) 
            assert inner_product(y, transpose(P)[1]) > 0
            return False, y
    lowerbound = - math.inf 
    upperbound = math.inf 
    lbIndex = None 
    ubIndex = None 
    # calculate lower and upperbound for x 
    for i in range(len(P)): 
        # improve lowerbound 
        if P[i][0] > 0 and P[i][1] / P[i][0] > lowerbound:
            lowerbound =   P[i][1] / P[i][0] 
            lbIndex = i 
        # correct upperbound 
        if P[i][0] < 0 and P[i][1] / P[i][0] < upperbound: 
            upperbound = P[i][1] / P[i][0]
            ubIndex = i 
    # construct y if lowerbound is greater than upperbound 
    if lowerbound > upperbound : 
        y = [0] *len(P)
        y[lbIndex] = 1
        y[ubIndex] = P[lbIndex][0] / (- P[ubIndex][0])
        assert abs(inner_product(y, transpose(P)[0])) < 10**(-12) 
        assert inner_product(y, transpose(P)[1]) > 0
        return False, y
    # return feasible x_1 if lowerbound is smaller than upperbound
    if lowerbound <= upperbound: 
        x = lowerbound if lowerbound != -math.inf else upperbound 
        if lowerbound == -math.inf and upperbound == math.inf:
            x = 42
        assert is_greater(multiply(x, transpose(P)[0]), transpose(P)[1])
        return True, [x]

def compute_x_or_y(input_file): 
    P = read(input_file)
    n = len(P[0])-1
    History = [(P, None)]
    B = P
    for i in range(0,n-1):
        B, M= dimension_reduction(B)
        History.append((B,M))
    NotEmpty, z = base_case(History[-1][0])
    History = History[::-1]
    if not NotEmpty: 
        for Q,M in History[:-1]:
            B = transpose_sparse(M)
            z = matrix_vector( B, z)
            #test3(Q, z)
        test3(P,z)
        return False, z 
    if NotEmpty : 
        for Q, _ in History[1:]: 
            z = step(Q, z)
            #test4(Q,z)
        return True, z 



def step(P, x):
    import math
    C = []
    for i in range(0, len(P)): 
        C.append([P[i][-2], P[i][-1]- inner_product(x, P[i][:-2])])
    lowerbound = - math.inf 
    upperbound = math.inf 
    lbIndex = None 
    ubIndex = None 
    # calculate lower and upperbound for x 
    for i in range(len(C)): 
        # improve lowerbound 
        if C[i][0] > 0 and C[i][1] / C[i][0] > lowerbound:
            lowerbound =   C[i][1] / C[i][0] 
            lbIndex = i 
        # correct upperbound 
        if C[i][0] < 0 and C[i][1] / C[i][0] < upperbound: 
            upperbound = C[i][1] / C[i][0]
            ubIndex = i 
    print(lowerbound, upperbound)
    assert upperbound >= lowerbound or abs(lowerbound -upperbound) < 10**(-12)
    w= [lowerbound if lowerbound != -math.inf else upperbound ]
    if lowerbound == -math.inf and upperbound == math.inf:
        w = [42]
    return x+w


def test3(P, z): 
    import numpy as np
    P = np.array(P)
    z = np.array(z)
    b = P[:,-1]
    A = P[:,:-1]
    assert np.allclose(z.transpose().dot(A), np.zeros(A.shape[1]))
    assert z.transpose().dot(b) > 0

def test4(P, z):
    import numpy as np
    P = np.array(P)
    print(P, z)
    z = np.array(z)
    A = P[:,:-1]
    b = P[:,-1]
    assert np.count_nonzero(A.dot(z) >= b) == A.shape[0]




        




 






