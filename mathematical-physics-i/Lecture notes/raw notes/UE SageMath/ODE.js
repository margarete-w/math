pretty_print_default(True)
//t, alpha = var('t, alpha')
var('t, alpha')
x = function('x')(t)

DE = diff(x,t) - alpha*x

desolve(DE, x, ivar=t, ics=[0,3])

DE = diff(x,t,2) - 4*diff(x,t) + 2*alpha*x

// forget assumptions, they are remembered
forget()
assume(alpha > 2)
desolve(DE, x, ivar =t, ics=[0,0,pi,0]) // at zero should be zero and at pi shpuld be zero
