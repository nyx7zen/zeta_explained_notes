# lec-001 Slides OCR (pymupdf 144dpi + pytesseract)

## Slide 1

Zeta in the Complex Plane

Imaginary

Real

* ¥

¢(s) is a complex function.
It has a pole ats=1

An interesting question is
when does ¢(s) = 0?

It has trivial zeros at negative
even integers, and an infinite
number of nontrivial zeros in
the “critical strip” where

0 < Re(s) <1.

Riemann Hypothesis (1859):
All of the nontrivial zeros are
on the “critical line”

Re(s) = 5

$1 million for proof or disproof


## Slide 2

Zeta in the Complex Plane

believed t
irrational, no
provi

0 be ..

is a complex function.

Ct It has a pole ats=1

> An interesting question is
when does ¢(s) = 0?
It has trivial zeros at negative
even integers, and an infinite
number of nontrivial zeros in

the “critical strip” where
0 < Re(s) <1.

Riemann Hypothesis (1859):
All of the nontrivial zeros are
on the “critical line”

Re(s) = 5

$1 million for proof or disproof


## Slide 3

Scope

N

> The Basel problem: 1+ 5+ 5+ 4+:°:°=%
> Following the first chapter of The Riemann Zeta-Function by
Aleksandar lIvié (1985)
> The Euler product formula
Analytic continuation
Laurent series for ¢(s) ats = 1
The functional equation relating ¢(s) to ¢(1 — s)
The Hadamard product formula
The Riemann-Von Mangoldt equation
A statement of the Riemann Hypothesis and the Lindelof
Hypothesis
(Don’t worry if you have no idea what any of these mean-the
point of the video series it to explain them!)

Vvvvvvy

v


## Slide 4

Prerequisites

v

Calculus
You definitely need to know calculus!

A lot of proofs will involve integrals and infinite series—so you
better know calculus!

Complex numbers (z = a+ bi, wherei= /-1) .

It will certainly help if you know complex analysis, which is the
topic of this series. But I'll try to explain things you need to
know.


## Slide 5

The Zeta Function

»

>
>

>

>

The Riemann zeta function is defined for real numbers s > 1 as

| 1 1 1
i=) {~-lt+gte tg?“
n=1

¢((2)=14+54+ 3+%+-:-= 2, a.k.a. the Basel Problem
¢(1) =1+ 5 + 5 + i +--+, a.k.a. the harmonic series, which

diverges.

Plugging in any s < 1 to the right-hand-side also diverges, as
each term is at least as big as the corresponding term for s = 1.
Eventually, we'll extend ¢(s) to a complex function for all
complex values of s other than s = 1.
In this extended function, ¢(—1) = — 5. Recall an infamous
Numberphile video (2014) where they claimed

1

142434+44-.--=-<.
+24+34+4+4+ 7a


## Slide 6

The Basel Problem

> Mengoli (1650):

1 1 1
1+ - — +--+. =???
toh tpt
> Euler (1734-5):
i += ; i: = : + : sh _=
4 9 16 6

> His proof is not considered rigorous by modern standards, but
it's mostly right and has some deep insights.


## Slide 7

Numerical Approximation

> Before proving it, Euler numerically estimated what the answer
should be.

> Adding up the partial sums of 1 + i + é + * +--+ is too
slow-the first 10,000 terms summed together gets you
1.644834..., which is correct to only 3 decimal places!

> So he used a summation technique known as Euler-Maclaurin
summation, where he got 20 decimal places of accuracy:
1.64493406684822643647...

> By 1730, a had been calculated to 100+ digits
> Aha! That's = (??7)


## Slide 8

Euler's proof of the Basel Problem

Taylor series of sin x:

Euler assumed he could factor

sin x as a product of terms

7 i 25 involving i Then h

snk = x — ax + RIX Sr Invo ving its zeros. en e
3! 3! showed the first terms are:

2
i
x 3! 5! = =

The x? term on the left must equal the x* term on the right, so

L_ _¢(2)

30?
Therefore, :

((2) ==


## Slide 9

Euler's proof of the Basel Problem

sinx = 0 if x = 7x, for all integers n
Note the slope at x=0 is 1 (f’(0) = cos(0) = 1)

sin x = 0 if x = Trn, not x = Trnx*


## Slide 10

Euler's proof of the Basel Problem

f(x) = sinx = x — 2° + Gx — +=
31 5

sin x = 0 if x = 7x, for all integers n
Note the slope at x=0 is 1 (f’(0) = cos(0) = 1)

Any series of sin x must start with x + ---

, note.g. 24x +---


## Slide 11

Euler's proof of the Basel Problem

f(x) = sinx = x — 4x3 + 3)x°

sin x = 0 if x = Trn, not x = Trnx*
sinx = 0 if x = 7nx, for all integers n

Note the slope at x=0 is 1 (f’(0) = cos(0) = 1)

Any series of sin x must start with x + --

-, note.g. 24x+---


## Slide 12

Euler's proof of the Basel Problem

vVvvvy

xX >
x(x — 1) >
x(x — 1)(x — 2) >
x(x — 1)(x — 2)(x — 3) >
x(x — 1)(x — 2)(x — 3)(x — 4) >

The coefficient of x is growing like n!

x

—X + se

oy — 3° +

—6x + 11x? — 6x? + x*

24x — 50x? + 35x? — 10x* + x®


## Slide 13

Factorial

For positive integers n, the factorial is defined as

ni'=n(n—1)---2x1

PrP i!=1

ye 2=2k1=—2

P 3I=3x2%1=—6

PrP 44=4x3x2x1=24

This satisfies the functional equation n! = n x (n — 1)! Using this,
we see that 1! = 1 x 0!, which implies 0! = 1.

We'll eventually need to know the “factorial” of a non-integer or
complex number!


## Slide 14

Euler's proof of the Basel Problem

>» aiX

B ax (x — 1)

b aX (x — 1)(x — 2)

m 3x(x — 1)(x — 2)(x —3)

be ux (x —1)(x —2)(x —3)(x —4)

m 5 (x)

"em T(-x+---)
pm 5 (2x+-:--)
b> x (- 6x +---)
mF (24x+---)


## Slide 15

Euler's proof of the Basel Problem

> aiX Pm x

p> x(x —1) Pm —x4+---
m 5,x(x — 1)(x — 2) > xt

m 3x(x — 1)(x — 2)(x — 3) > —-x+---
Pm ax(x—1)(x—2)(x—3)(x—4) P xt.


## Slide 16

Euler's proof of the Basel Problem

x(x — 1) = —x(1— x)
x(x — 1)(x — 2) = x(1 — x)(2 — x)
x(x — 1)(x — 2)(x — 3) = —x(1 — x)(2 — x)(3 — x)
x(x — 1)(x — 2)(x — 3)(x — 4) = x(1 — x)(2 — x)(3 — x)(4 - x)


## Slide 17

Euler's proof of the Basel Problem

Vvv VY
lp Oe Nie ele Ole
x
pod
|
ES
Vv vv YV


## Slide 18

Euler's proof of the Basel Problem

= x(1— x)(2 — x)(3 — x)(4— x)

4!
Lhasd kt
1 1 1 1
=x- 7 (1—x)-5(2—x)- 3(3— x) - 74 — x)

=x(1— x) (1-5) 3] i-7)

>» Remember this is a function with zeros at 0,1,2,3,4, and the
first term of its Taylor series is x (as opposed to e.g. 24x).


## Slide 19

Euler's proof of the Basel Problem

6—9-DO-DO-D

> Remember this is the factorization of a function with zeros at
0,1,2,3,4, and the first term of its Taylor series is x (as
opposed to e.g. 24x).

Pm sinx has zeros at 0,.47,+27,+37,..., and the first term of its
Taylor series is x. Euler concluded that its factorization must be

«(1-5 ) (2+ 5) (tag) + an) a) + a)

> This step is sketchy because you can't just apply a result that
works for finite cases to infinite cases. It was proved much later
that you can indeed factor functions into infinite products based
on their zeros—the Weierstrass Factorization Theorem (1870s).


## Slide 20

Euler's proof of the Basel Problem

> Remember that (a— b)(a+b) = a* — b?. So each pair of terms
can be combined, for example:

2
(1-35) (1+ 35) 1 on

> So the factorization becomes

x? x? x2
sinx =x (1-5) (1- ga) (1-3)

> Dividing both sides by x:

sinx _(,_ *\(,_ *~\(1_ ©)...
x 12 An? O72


## Slide 21

Euler's proof of the Basel Problem

f(x) = sinx


## Slide 22

Euler's proof of the Basel Problem

f(x) = sin x
2

s(x) =x (1- %) (1- #) (1- a) (1- ee)

SS es eS ee Se es ee | ee ee a a a: a a

ee i rr ee

close to sin(x), not:close to pi*


## Slide 23

Euler's proof of the Basel Problem

sinx (,_ *\(,_ ~~ \(,_*)...
x 12 Ar? Or?

> Multiply out the product and collect terms carefully:
> All the 1's multiplied out becomes 1. So
sin x
=1+-
> There can't be an x term, so the next term has to be x*. The
x* term involves selecting a 1 from every term in the product

x2
except one term, where we select the ———; term. Hence
sin x 1 1 1 >
x ( 2 4An2 Or? .)

=1- = 6(2)? +:


## Slide 24

Euler's proof of the Basel Problem

Taylor series of sin x: Euler assumed he could factor
sin x as a product of terms
, 13, 1+, es Then h
sinx = x — ax + ax = involving its zeros. en he

showed the first terms are:

2
7 me gS 4.2
x 3! 5! * 7

The x? term on the left must equal the x? term on the right, so

1 (2)

31s x

Therefore, ;

((2) ==


## Slide 25

Euler's proof of the Basel Problem

> Next time: Analyzing ¢(s) in the complex plane and discussing
convergence.


## Slide 26

Feedback

Let me know if you have feedback!

Was the pacing too fast/too slow?

Was subject too easy/too difficult?

Did | skip over important steps?

Were there parts that didn't make sense or seemed unjustified?
Was it interesting or did it seem pointless?

Did you spot any errors? | probably made some.

What can | do better?

Vvvvvvvyyv iY

