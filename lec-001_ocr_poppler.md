# lec-001 Slides OCR (poppler 300dpi + pytesseract)

## Slide 1

Zeta in the Complex Plane

Imaginary

+ + 25.01i
+ + 21.02i

5 + 14.13i

Real

\

C(s) is a complex function.
it has a pole ats=1

An interesting question is
when does ¢(s) = 0?

It has trivial zeros at negative
even integers, and an infinite
number of nontrivial zeros in
the “critical strip’ where

0 < Re(s) <1.

Riemann Hypothesis (1859):
All of the nontrivial zeros are
on the “critical line’

Re(s) = 5

$1 million for proof or disproof


## Slide 2

Zeta in the Complex Plane

believed to De ¢(s) is a complex function.
irrationz 7 nor It has a pole at s= 1

> An interesting question is

1

rov Sie when does ¢(s) = 0?
[) ” > It has trivial zeros at negative
. even integers, and an infinite
7 Real = number of nontrivial zeros in
| the “critical strip’ where
. 0 < Re(s) <1.
+ — 14.13/ | ¢ :, .
| > Riemann Hypothesis (1859):
1 _ 91.02i | e All of the nontrivial zeros are
2 — 25.01i | @ on the “critical line”

Re(s) = 5

> $1 million for proof or disproof


## Slide 3

Scope

> The Basel problem: 1+}4+3444...==

> Following the first chapter of The Riemann Zeta-Function by
Aleksandar lIvié (1985)

The Euler product formula

Analytic continuation

Laurent series for ¢(s) ats = 1

The functional equation relating ¢(s) to ¢(1 — s)

The Hadamard product formula

The Riemann-Von Mangoldt equation

A statement of the Riemann Hypothesis and the Lindelof

Hypothesis

(Don't worry if you have no idea what any of these mean-the

point of the video series it to explain them!)

VvvvvvyY

Vv


## Slide 4

Prerequisites

v

Calculus
You definitely need to know calculus!

A lot of proofs will involve integrals and infinite series—so you
better know calculus!

Complex numbers (z = a+ bi, where / = /—1)

It will certainly help if you know complex analysis, which is the
topic of this series. But I'll try to explain things you need to
know.


## Slide 5

The Zeta Function

a

VV

The Riemann zeta function is defined for real numbers s > 1 as

OO
1 1 ] ]
((s)= ) =itastatat
n=1
((2)=14+4+ j+4+°:'= 7 aka, the Basel Problem

((1)=14+5+ : +%+---, a.k.a. the harmonic series, which
diverges.

Plugging in any s < 1 to the right-hand-side also diverges, as
each term is at least as big as the corresponding term for s = 1.
Eventually, we'll extend ¢(s) to a complex function for all
complex values of s other than s = 1.

In this extended function, ¢(—1) = — i. Recall an infamous
Numberphile video (2014) where they claimed
i
14+24+34+44---=-

12 “


## Slide 6

The Basel Problem

> Mengoli (1650):

1 1 1
ie a i Be TP?
tctet. +t

> Euler (1734-5):
eee pe
4° 9 16 «6

> His proof is not considered rigorous by modern standards, but
it's mostly right and has some deep insights.


## Slide 7

Numerical Approximation

> Before proving it, Euler numerically estimated what the answer
Should be.

> Adding up the partial sums of 1 + ; + 5 + fre +--+ is too
slow-the first 10,000 terms summed together gets you
1.644834..., which is correct to only 3 decimal places!

> So he used a summation technique known as Euler-Maclaurin
Summation, where he got 20 decimal places of accuracy:
1.64493406684822643647...

> By 1730, m had been calculated to 100+ digits

> Aha! That's = (77?)


## Slide 8

Euler's proof of the Basel Problem

S| [Sn
Taylor series of sin x: Euler assumed he could factor
sin xX as a product of terms
sinx =x — 2x + oa =: involving its zeros. Then he
a t Then h
s 9} showed the first terms are:
sin x Ls ta sin x _| (2) »
—— oe ] es —— Se ees
x 3! 5! = at

The x? term on the left must equal the x? term on the right, so

oe eC,

3! 1?

Therefore, :

(2) = =


## Slide 9

Euler's proof of the Basel Problem

f(x) = sinx = x — 3x? +

sin x = 0 if x = m7nx, for all integers n
Note the slope at x=0 is 1 (f'(0) = cos(0) = 1)

sin x = 0 if x = Trn, not x = Trnx*


## Slide 10

Euler's proof of the Basel Problem

f(x) = sinx =x — #x2 + yx°----

sinx = 0 if x = 7x, for all integers n
Note the slope at x=0 is 1 (f’(0) = cos(0) = 1)

Any series of sinx must start with x +---, note.g. 24x +.---


## Slide 11

Euler's proof of the Basel Problem

f(x) = sinx =x — ¥x?+ yx? -

sin x = 0 if x = Tin, not x = Tnx”
sin x = 0 if x = 7x, for all integers n
Note the slope at x=0 is 1 (f’(0) = cos(0) = 1)

Any series of sinx must start with x +---, note.g. 24x+---


## Slide 12

Euler's proof of the Basel Problem

Vvvv iy

xX b>
x(x — 1) >
x(x — 1)(x — 2) a
x(x — 1)(x — 2)(x — 3) >
x(x — 1)(x — 2)(x — 3)(x — 4) b>

The coefficient of x is growing like n!

x

—X + a

2x — 3x*+ x?

—6% + 11 — 6° 4+

24x — 50x? + 35x? — 10x* + x?


## Slide 13

Factorial

For positive integers n, the factorial is defined as

ni!'=n(n—-1)---2x1

> i!=1

> 2J=2xk1=2

yr 3=3x2x%1=—6

re 44=4x3xK2x1=24

This satisfies the functional equation n! = n x (n— 1)! Using this,
we see that 1! = 1 x 0!, which implies 0! = 1.

We'll eventually need to know the “factorial” of a non-integer or
complex number!


## Slide 14

Euler's proof of the Basel Problem

> ax > (0

> x(x Bote)
Pm 3,x(x — 1)(x — 2) m 5 (2x+---)

Pm 2x(x — 1)(x — 2)(x — 3) Pp + (-6x+---)
m Bx(x-1)(x—2)(x-3)(x—4) B24 4+)


## Slide 15

Euler's proof of the Basel Problem

Vv vv Vv
Bhi Wi Nie S| Sl

x

x(x — 1)

(x(x — 1)(x — 2)

(x(x — 1)(x — 2)(x — 3)
(

x(x —1)(x —2)(x —3)(x—4)

VvVvV VY

—X +-:--:-

—xX-+-:-:-


## Slide 16

Euler's proof of the Basel Problem

x(x — 1) = —x(1 — x)
x(x — 1)(x — 2) = x(1 — x)(2 — x)
x(x — 1)(x — 2)(x — 3) = —x(1 — x)(2 — x)(3 — x)
x(x — 1)(x — 2)(x — 3)(x — 4) = x(1 — x)(2 — x)(3 — x)(4 — x)


## Slide 17

Euler's proof of the Basel Problem

Vvv Vv iY

aX

=;x(1 — x)

5 x(1 — x)(2 — x)

3x(1 — x)(2 — x)(3 — x)
aX(1—x)(2—x)(3—x)(4—x)

VvvVvV VY

a oe
SG Be cas
ap eke se
56 hen wo


## Slide 18

Euler's proof of the Basel Problem

Mp
— -_—™

a x(1 — x)(2 — x)(3 — x)(4 — x)

1 1 i 1
=x + 7(1 — x) 5(2— x) 3(3— x) 74 —%)

=x) (1-3) (0-3) 0-3

> Remember this is a function with zeros at 0,1,2,3,4, and the
first term of its Taylor series is x (as opposed to e.g. 24x).


## Slide 19

Euler's proof of the Basel Problem

(1) (1-5) (1-3) (1-4)

> Remember this is the factorization of a function with zeros at
0,1,2,3,4, and the first term of its Taylor series is x (as
opposed to e.g. 24x).

> sinx has zeros at 0,7,+27,+37,..., and the first term of its
Taylor series is x. Euler concluded that its factorization must be

(1-5) (142) (1 ae) (1+ ae) hae) (tae)

> This step is sketchy because you can't just apply a result that
works for finite cases to infinite cases. It was proved much later
that you can indeed factor functions into infinite products based
on their zeros—the Weierstrass Factorization Theorem (1870s).


## Slide 20

Euler's proof of the Basel Problem

(1-5) (142) (1 ag) (8+ ae) (> ge) tae)

> Remember that (a— b)(a+ b) = a* — b*. So each pair of terms
can be combined, for example:

2
(1 35) (2+ ge) <1 on

> So the factorization becomes

2 2 2
; X Xx xX

> Dividing both sides by x:

sin x 2 x? 1 x2 1 x
x 1? Ar? On?


## Slide 21

Euler's proof of the Basel Problem

f(x) = sin x


## Slide 22

Euler's proof of the Basel Problem

f(x) = sin x

Oh

a = = = = - = _ = = —_ = . = = Se = = =. * om = = = = 7. = = = — = a . = = = + = a a a

close to sin(x), not:close to pi*


## Slide 23

Euler's proof of the Basel Problem

sinx = (, x \(,_*\(,_*)...
x 1? Ar? Or

> Multiply out the product and collect terms carefully:

> All the 1’s multiplied out becomes 1. So
a i has
x

> There can't be an x term, so the next term has to be x*. The
x* term involves selecting a 1 from every term in the product
2
except one term, where we select the —-5 term. Hence

1 1 i
1 9


## Slide 24

Euler's proof of the Basel Problem

LT Se ae
Taylor series of sin x: Euler assumed he could factor
sin x as a product of terms
| 1, 14, veld
sinx = x-— 2x + =i” =r involving its zeros. Then he
3! showed the first terms are:
sin x 2
sinx _ lola... =1- S24.
x 3! 5! a *

The x? term on the left must equal the x? term on the right, so

12)

3b

Therefore, ;

((2)= >


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

Were there parts that didn't make sense or seemed unjustified ?
Was it interesting or did it seem pointless?

Did you spot any errors? | probably made some.

What can | do better?

Vvvv vv Vv Y

