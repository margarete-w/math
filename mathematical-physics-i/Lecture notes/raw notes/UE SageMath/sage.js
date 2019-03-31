// MPI 12.11.2018
// Jupyter is the graphical interface

// create a symbolic variable
var('x')

// access and do computations
x^2+1

// print
pretty_print(x^2+1)

// default print
pretty_print_default(True)
var('x')



// Does the map contain any periodic orbits?

// symbolic stuff
pretty_print_default(True)
var('x, y, alpha')

// define the function
f(x,y) = (x / (alpha*x -1), (y+ alpha*x*(x-y)/alpha*x-1))
// this prints the expression
f
// print
f(x,y)

// unpacking
// thats just a composition
f(*f(x,y))


// You can simplify expressions
// expressions are objects
(x^2+1).full_simplify() // nothing will happen


f(*f(x,y))[0].full_simplify()
f(*f(x,y))[1].full_simplify()

// some pretty closure stuff is happening!
f(*f(x,y)).apply_map(lambda x:x.full_simplify())



///
//  2. Exercise
///

var('x_1,y_1')
X1 = (x_1-x)  == alpha*(x_1*y+x*y_1)
X1 // print

X2 = (y_1 - y) == -2 * x * x_1
X2 // print

// solve
L1, L2 = solve([X1,X2], x_1,y_1)
L1, L2

// Function of the dynamical system
// flow
g(x,y) = (X2.rhs(), Y2.rhs())
g

// Is F an invariant?
F(x,y) = (x^2 + alpha*y^2 / (1+alpha*x^2))
F

// Evaluate whether it is true
bool(F(*g(x,y)).full_simplify() == F(x,y))


// visualize
A = (alpha == 2.)
N = 2
plot1 = contour_plot(F.subs(A), (x,-N,N), (y,-N,N))


def gN(x_0,y_0,N):
  values = [(x_0,y_0)]
  for _ in range(N):
    x_0, y_0 = g.subs(A)(x_0,y_0)
    values.append((x0, y_0))
  return values

// iteration
gN(1,1,10)

plot1 + list_plot(gn(1,1,10), zorder =10)
