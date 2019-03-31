// MPI 12.11.2018

pretty_print_default(True)
var('x_1,x_2,t')

X = 1 + x_1^2+x_2^2 + (1 - x_1^2 - x_2^2)*cos(t) - 2*x_2*sin(t)
Phi1(t,x_1,x_2) = 2*x_1 / X
Phi1

Phi2(t,x_1,x_2) = (2*x_2*cos(t) + (1-x_1^1-x_2^2)*sin(t)) /X
Phi2

// vecrtor field
V1(x_1,x_2) = diff(Phi1, t)(0,x_1,x_2)
V2(x_1,x_2) = diff(Phi2, t)(0,x_1,x_2)

N = 2
plot1 = plot_vector_field([V1,V2], (x_1,-N, N), (x_2,-N,N))


sol = desolve_odeint([V1,V2], ics=[1,1], times = srange(0,1,0.1), dvars=[x_1,x_2])
plot1 + list_plot(sol)
