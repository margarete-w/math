# Discrete Geometrie I

## Week 01

Content: Convex sets, convex hulls, Minkowski sum and Carathéodory's theorem

- "A Course in Convexity" by Alexander Barvinok: Chapter I, §1, §2
- "Lectures on Discrete Geometry": §1.2
- "Convex Polytopes": §2.1 and §2.3
- "Algorithmische Geometrie": §2.3
- "Lectures on Polytopes": §1.6

### Convex sets and convex hull

**Definition (Convex hull):** $\mathrm{conv}(A)$

  * the set that contains all convex combinations from $A$
  * smallest convex set that contains $A$ _[Theorem 2.1, GSM054]_

**Examples of convex sets**

  * convex hull of a set is convex _(exercise)_
  * a ___polyhedron___ $P = \{ x \in \mathbb R^d : \langle c,x \rangle \leq b \}$ is a convex set _(exercise)_
  * prove that the sets are convex _(exercise)_

$$
B = \{ f \in \mathcal C([0,1], \mathbb R) : |f(x)| \leq 1\} \\
K = \{ f \in \mathcal C([0,1], \mathbb R) : |f(x)| \leq 0\} 
$$

**Definition (Minkowski sum):** 
  * $A+B = \{ x+y : x \in A, y \in B\}$
  * $\alpha A$ is called a ***scaling*** and $a+A$ is called ***translation***

**Some properties for convexity**

  * the intersection (denumerable or not) of convex sets is convex _(exercise)_ 

$$
\bigcap_{n \in \mathbb N} A_n \text{ is convex}
$$

  * $T(A)$ is convex if $T$ is a linear transformation and $A$ is convex _(exercise_)
  * $A+B$ is convex if $A$ and $B$ are convex
  * $(\alpha + \beta)A = \alpha A + \beta B$ if $A$ and $B$ are convex (this does not hold if $\alpha$ or $\beta$ is negative or if $A$ is not convex)
  * $\mathrm{conv}(\mathrm{conv}(A)) = \mathrm{conv}(A)$ _(exercise)_
  * $A \subset B \implies \mathrm{conv}A \subset \mathrm{conv}B$ _(exercise)_
  * $\mathrm{conv}(A) \cup \mathrm{conv}(B) \subset \mathrm{conv}(A \cup B)$ _(exercise)_
  * $\mathrm{closure}(A)$ and $\mathrm{interior}(A)$ are convex if $A$ is convex (use $\mathrm{closure}(A) = \bigcap_{\lambda > 0}(A + U_{\lambda}(0))$

**Definition (Polytope):** The convex hull of a finite set of points is called a ___polytope___. A polytope is also an polyhedron. A ___bounded polyhedron___ is a ___polytope___.

---

### Carathéodory's Theorem

![](https://www.user.tu-berlin.de//nguyenvi/marktex/img/discrete-geometry-i/caratheodory.png)

Let $S \subset \mathbb R^d$. Then every point $x \in \mathrm{conv}(S)$ can be represented as a convex combination of $d+1$ points from $S$.

_Key idea_

We have a system of linear equations with $d+1$ equations and $m > d+1$ variables. For this system we will find a nontrivial solution that we can scale and add to the convex combination such that a coefficient vanishes.

_Proof._

* Let $x \in \mathrm{conv}(S)$. Let $m > d+1$. Then, $x = \sum^{m}_{i=1} \alpha_i y_i$.
* We would like to find a solution of the _homogeneous_ system of linear equations with $d+1$ equations and $m$ variables:

$$
\begin{pmatrix}
y_{1,1} & ... & y_{m,1} \\
\vdots & . & \vdots \\
y_{1,d} & ... & y_{m,d} \\
1 & ... & 1
\end{pmatrix}
\begin{pmatrix}
\gamma_1 \\ \vdots \\ \gamma_m
\end{pmatrix} = 
\begin{pmatrix}
0 \\ \vdots \\ 0 \\ 0
\end{pmatrix}.
$$

* There exists a _nontrivial_ solution $(\gamma_1,...,\gamma_m)$ for the system above with $\gamma_i > 0$ for some $i \in [m]$, because the columns $y_1,...,y_m$ are linearly dependent. 
* Find smallest $\tau = \min_{i \in [m]}\{\frac{\alpha_i}{\gamma_i} : \gamma(i) > 0\}$. Then, $\tau \gamma$ still solves the homogeneous system.
* Add $-\tau \gamma$ to the solution $\alpha$, and we eliminated a variable $x_{i_0}$. Indeed, $x$ is still a convex combination but only with $m-1$ coefficients $\alpha - \tau \gamma$.

**Show by an example that the constant $d+1$ cannot be improved.**

![](https://www.user.tu-berlin.de/nguyenvi/marktex/img/discrete-geometry-i/counter-example-caratheodory.png)


**Carathéodory's Theorem 2** (Convex Polytopes by Branko Grünbaum)

$$
	A \text{ is compact } \implies \mathrm{conv}(A) \text{ is closed.}
$$

_Key idea._ Use compactness argument that there always exists a convergent subsequence. Use ___Carathéodory's theorem___ to limit the number of coefficients of the convex combination.

_Proof._ The proof can be read on page 15-16. Let $x \in \partial \mathrm{conv}(A)$. We make use of Carathéodory's theorem (it is needed to assure that $x$ is not a convex combination of an infinite number of elements $a_i \in A$).  We want to show that $x \in \mathrm{conv}(A)$. Then, there exists a sequence $(x_n)_{n \in \mathbb N} \subset A$ that converges to $x$. Each $x_n$ can be represented as a convex combination from $A$: $x_n = \sum^{d+1}_{i=1}\lambda_i(n) a_i(n)$. Since $A$ is _compact_, there exists a converging subsequence such that $a_{i}(n_k) \to a_i$ and $\lambda_{i}(n_k) \to \lambda_i$ for $I=i,...,d+1$. Now, it holds $x = \sum^{d+1}_{i=1}\lambda_i a_i$,

**Carathéodory's Theorem for Cones**

Let $X$ be a subset of $\mathbb R^n$. Every nonzero vector from $\mathrm{cone}(X)$ can be represented as a _positive_ linear combination of _linearly independent_ vectors from $X$.

**Radon's Theorem** (Convex Polytopes, §2.3)

![](https://www.user.tu-berlin.de/nguyenvi/marktex/img/discrete-geometry-i/radons-theorem.png)

Consider a set $A \in \mathbb R^d$ with at least $d+2$ points. Then, you can find two disjunct partitions $A_1$ and $A_2$ of $A$ such that their convex hulls intersect.

---

**The convex hull of a compact sets is compact.**

**The convex hull of an open set is open.**

*Proof.* Let $A$ be open and $x \in \mathrm{conv}(A)$. It holds $x = \sum \alpha_i x_i$ and $\sum \alpha_i = 1$. We want to find an open set $U \subset \mathrm{conv}(A)$ that contains $x$.

Define the continuous function 

$$
f(x) = \frac{1}{\alpha_1}(x - \sum_{j=2}^n \alpha_j x_j), \\
f^{-1}(x) = \alpha_1 x + \sum^n_{j=2} \alpha_jx_j.
$$

For our given $x$ the function yields $f(x) = x_1 \in A$ (*key idea*). Thus, $x \in f^{-1}(A)$, which is open, contains $x$ and is a subset of the convex hull of $A$.

**Example for a closed set whose convex hull is not closed.**

Consider $\{\frac{1}{n} : n \in \mathbb N\}$. The convex hull is $(0,1]$.



---



## Week 02

Radon’s theorem, Helly’s theorem and Euler characteristic.

- "A Course in Convexity" by Alexander Barvinok: Chapter I, §4, §7.
- "Lectures on Discrete Geometry": §1.3 and §1.4
- "Convex Polytopes": §2.3

---

### Radon's Theorem

![](https://www.user.tu-berlin.de/nguyenvi/marktex/img/discrete-geometry-i/radons-theorem-2.png)

Let $S \subset \mathbb R^d$ be a set containing at least $d+2$ points. Then, there are two non-intersecting subsets $R \subset S$ and $B \subset S$ such that $S = R \cup B$ and

$$
	\mathrm{conv}(A) \cap \mathrm{conv}(B) \neq \emptyset.
$$

_Proof._

Let $x_1,...,x_m \in S$ with $m \geq d+2$. Consider the following system of linear equations

$$
	\gamma_1 x_1 + ... \gamma_m x_m = 0 \quad \text{and} \quad \gamma_1 + ... + \gamma_m = 0.
$$

Since all points $x_i \in \mathbb R^d$, we obtain a system with $d+1$ equations and $d+2$ variables. Therefore, there exists a nontrivial solution $\gamma_1,...,\gamma_m$. Define

$$
	R = \{ x_i : \gamma_i > 0 \}, \quad \text{and} \quad B = \{ x_i : \gamma_i < 0\}.
$$

Define $\beta = \sum_{\gamma_i > 0}\gamma_i = \sum_{\gamma_i < 0}\gamma_i$. Both are equal because of $\gamma_1 + ... + \gamma_m = 0$. Define the point

$$
	z = \sum_{\gamma_i > 0} \gamma_i \beta^{-1} x_i \sum_{\gamma_i < 0} \gamma_i \beta^{-1}x_i,
$$

and we see that $z$ is a convex combination of points from $R$ and $B$.

**Show by an example that the constant $d+2$ cannot be improved.** Any three points in the plane that forms a triangle.

Here comes one of the most famous results in convexity. It was discovered by E. Helly in 1913.

---

### Helly's Theorem

Let $A_1,...,A_m \subset \mathbb R^d$ be a ___finite___ family of convex sets and $m \geq d+1$. Suppose that every $d+1$ of the sets have a point in common

$$
	A_{i_1} \cap ... \cap A_{i_{d+1}} \neq \emptyset.
$$

Then, all sets have a point in common

$$
	A_{1} \cap ... \cap A_{m} \neq \emptyset.
$$

_Proof by induction on $m$ (due to Radon 1921)._

* Start with $m=d+1$. This is clear.
* Induction step $m \leadsto m+1$. For every $i=1,...,m$ consider the intersection $\bigcap_{i \neq m} A_i$, and let $p_i$ denote the point that lies in the intersection. The point $p_i$ may lie in $A_i$ but we do not know for sure. If two points $p_i$ and $p_j$ are the same for $i \neq j$, then $p_i$ lies in the intersection of all $A_i$, and we are done. Otherwise, there exist $m > d+1$ distinct points, and we can use ___Radon's theorem___. 

* By Radon's theorem, there are two distinct sets $I, J \subset [m]$ with $R = \{ p_i : i \in I \}$ and $B = \{ p_j : j \in J \}$ such that their convex hull intersect in a common point $p$. Each point $p$ from $R$ belongs to $A_i$ forall $i \notin I$; same for $S$. ___Since $A_i$ is convex___, it holds $\mathrm{conv}(R) \subset A_i$ for all $i \notin I$; same for $S$. We see that $p$ is a common point of all $A_i$ because $I$ and $J$ are disjoint.


jnjknj njknjnjnknjnkefe xDddnksnfjkwnfjwnkfnwjnefwnkfnwjnfkj

jinjnknjkn hhxdxdxdxdxdxdxdxxxdxdxdxdxdxdxdxdddxdxdxddxctrftftfztfztfthjbhjbbhjb





jjnjnjknjk

mklkmklmmlmlkmmklmklmmlmkklmkm

mkkmkmmkkm $x^2 ajdnajdnandnandandnadnwkndkqwdqddqdqdqut3ih4ui43htuh3uith3$


$$
nnjn
$$

$
jbhj
$

$$
fefefefef
$$

ef




ffr

kmkmkmlmkmkkkfjnrkfnejfnejknfejnfkjenfkenjfnenjkfnjek
fehbfwjhbfhjwbfh
dsffsfeiwofjeiwjriwejriwjiroiwjiwkfmlwmfklwmfk
dwdqwdqddqwddqwddwhebfhbhbjewbfh
dffsfsdfsdfsdfwefwerwerwrwrwr242342k4m23m4k2m4kl2m4k2mk4m2l42k
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQzNTI1OTgxNCw3MzA5OTgxMTZdfQ==
-->