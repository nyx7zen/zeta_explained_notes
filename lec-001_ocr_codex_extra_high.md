# lec-001 Slides OCR (codex_extra_high)

## Capability Note

The PDF has 26 image-only pages and no extractable text layer. Codex `extra_high` extracted the embedded page images and transcribed the visible English text and formulas from those images. No paid OCR API was used.

## Page 1

### English Text

Title: Zeta in the Complex Plane

Graph labels:

- Imaginary
- Real
- Points labeled approximately:
  - `1/2 + 25.01i`
  - `1/2 + 21.02i`
  - `1/2 + 14.13i`
  - `1/2 - 14.13i`
  - `1/2 - 21.02i`
  - `1/2 - 25.01i`

Bullet text:

- `zeta(s)` is a complex function.
- It has a pole at `s = 1`.
- An interesting question is when does `zeta(s) = 0`?
- It has trivial zeros at negative even integers, and an infinite number of nontrivial zeros in the "critical strip" where `0 < Re(s) < 1`.
- Riemann Hypothesis (1859): All of the nontrivial zeros are on the "critical line" `Re(s) = 1/2`.
- `$1 million for proof or disproof`

### Formulas

1. `inline`

`$\zeta(s)$`

2. `inline`

`$s = 1$`

3. `inline`

`$\zeta(s) = 0$`

4. `inline`

`$0 < \operatorname{Re}(s) < 1$`

5. `display`

$$
\operatorname{Re}(s) = \frac{1}{2}
$$

### Uncertain Items

- Graph shows trivial zeros on the negative real axis, a pole at `s = 1`, and nontrivial zeros on the critical line.

## Page 2

### English Text

Title: Zeta in the Complex Plane

Large red overlay:

- believed to be irrational, not proven*

The rest of the slide repeats Page 1.

### Formulas

Same formulas as Page 1.

### Uncertain Items

- The red overlay appears to correct the claim that the displayed imaginary parts are irrational.

## Page 3

### English Text

Title: Scope

- The Basel problem:
- Following the first chapter of *The Riemann Zeta-Function* by Aleksandar Ivic (1985)
  - The Euler product formula
  - Analytic continuation
  - Laurent series for `zeta(s)` at `s = 1`
  - The functional equation relating `zeta(s)` to `zeta(1 - s)`
  - The Hadamard product formula
  - The Riemann-Von Mangoldt equation
  - A statement of the Riemann Hypothesis and the Lindelof Hypothesis
- (Don't worry if you have no idea what any of these mean--the point of the video series it to explain them!)

### Formulas

1. `inline`

`$1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots = \frac{\pi^2}{6}$`

2. `inline`

`$\zeta(s)$`

3. `inline`

`$s = 1$`

4. `inline`

`$\zeta(s)$`

5. `inline`

`$\zeta(1 - s)$`

### Uncertain Items

- Slide text has "it to explain them"; likely intended "is to explain them."

## Page 4

### English Text

Title: Prerequisites

- Calculus
- You definitely need to know calculus!
- A lot of proofs will involve integrals and infinite series--so you better know calculus!
- Complex numbers `(z = a + bi, where i = sqrt(-1))`.
- It will certainly help if you know complex analysis, which is the topic of this series. But I'll try to explain things you need to know.

### Formulas

1. `inline`

`$z = a + bi$`

2. `inline`

`$i = \sqrt{-1}$`

### Uncertain Items

- None.

## Page 5

### English Text

Title: The Zeta Function

- The Riemann zeta function is defined for real numbers `s > 1` as
- `zeta(2)` is the Basel Problem.
- `zeta(1)` is the harmonic series, which diverges.
- Plugging in any `s < 1` to the right-hand-side also diverges, as each term is at least as big as the corresponding term for `s = 1`.
- Eventually, we'll extend `zeta(s)` to a complex function for all complex values of `s` other than `s = 1`.
- In this extended function, `zeta(-1) = -1/12`. Recall an infamous Numberphile video (2014) where they claimed

### Formulas

1. `display`

$$
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}
= 1 + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s} + \cdots .
$$

2. `display`

$$
\zeta(2) = 1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots
= \frac{\pi^2}{6}
$$

3. `display`

$$
\zeta(1) = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots
$$

4. `inline`

`$s < 1$`

5. `inline`

`$s = 1$`

6. `inline`

`$\zeta(-1) = -\frac{1}{12}$`

7. `display`

$$
1 + 2 + 3 + 4 + \cdots = -\frac{1}{12}.
$$

### Uncertain Items

- None.

## Page 6

### English Text

Title: The Basel Problem

- Mengoli (1650):
- Euler (1734-5):
- His proof is not considered rigorous by modern standards, but it's mostly right and has some deep insights.

### Formulas

1. `display`

$$
1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots = ???
$$

2. `display`

$$
1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots = \frac{\pi^2}{6}
$$

### Uncertain Items

- None.

## Page 7

### English Text

Title: Numerical Approximation

- Before proving it, Euler numerically estimated what the answer should be.
- Adding up the partial sums of `1 + 1/4 + 1/9 + 1/16 + ...` is too slow--the first 10,000 terms summed together gets you `1.644834...`, which is correct to only 3 decimal places!
- So he used a summation technique known as Euler-Maclaurin summation, where he got 20 decimal places of accuracy: `1.64493406684822643647...`
- By 1730, `pi` had been calculated to 100+ digits
- Aha! That's `pi^2/6` (???)

### Formulas

1. `inline`

`$1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots$`

2. `inline`

`$\frac{\pi^2}{6}$`

### Uncertain Items

- None.

## Page 8

### English Text

Title: Euler's proof of the Basel Problem

Left heading:

- Taylor series of `sin x`:

Right text:

- Euler assumed he could factor `sin x` as a product of terms involving its zeros. Then he showed the first terms are:
- The `x^2` term on the left must equal the `x^2` term on the right, so
- Therefore,

### Formulas

1. `display`

$$
\sin x = x - \frac{1}{3!}x^3 + \frac{1}{5!}x^5 - \cdots
$$

2. `display`

$$
\frac{\sin x}{x}
= 1 - \frac{1}{3!}x^2 + \frac{1}{5!}x^4 - \cdots
$$

3. `display`

$$
\frac{\sin x}{x}
= 1 - \frac{\zeta(2)}{\pi^2}x^2 + \cdots
$$

4. `display`

$$
-\frac{1}{3!} = -\frac{\zeta(2)}{\pi^2}
$$

5. `display`

$$
\zeta(2) = \frac{\pi^2}{6}
$$

### Uncertain Items

- None.

## Page 9

### English Text

Title: Euler's proof of the Basel Problem

- `sin x = 0` if `x = pi n`, for all integers `n`
- Note the slope at `x = 0` is 1 (`f'(0) = cos(0) = 1`)

Large red correction:

- `sin x = 0 if x = pi n, not x = pi n x*`

### Formulas

1. `display`

$$
f(x) = \sin x = x - \frac{1}{3!}x^3 + \frac{1}{5!}x^5 - \cdots
$$

2. `inline`

`$\sin x = 0$`

3. `inline`

`$x = \pi n$`

4. `inline`

`$f'(0) = \cos(0) = 1$`

### Uncertain Items

- Graph of `sin x`.

## Page 10

### English Text

Title: Euler's proof of the Basel Problem

- `sin x = 0` if `x = pi n`, for all integers `n`
- Note the slope at `x = 0` is 1 (`f'(0) = cos(0) = 1`)
- Any series of `sin x` must start with `x + ...`, not e.g. `24x + ...`.

### Formulas

1. `display`

$$
f(x) = \sin x = x - \frac{1}{3!}x^3 + \frac{1}{5!}x^5 - \cdots
$$

2. `inline`

`$\sin x = 0$`

3. `inline`

`$x = \pi n$`

4. `inline`

`$f'(0) = \cos(0) = 1$`

5. `inline`

`$x + \cdots$`

6. `inline`

`$24x + \cdots$`

### Uncertain Items

- Graph of `sin x`.

## Page 11

### English Text

Title: Euler's proof of the Basel Problem

Large red correction:

- `sin x = 0 if x = pi n, not x = pi n x*`

Other text repeats Page 10:

- `sin x = 0` if `x = pi n`, for all integers `n`
- Note the slope at `x = 0` is 1 (`f'(0) = cos(0) = 1`)
- Any series of `sin x` must start with `x + ...`, not e.g. `24x + ...`.

### Formulas

Same formulas as Page 10.

### Uncertain Items

- Graph of `sin x`.

## Page 12

### English Text

Title: Euler's proof of the Basel Problem

- The coefficient of `x` is growing like `n!`.

### Formulas

1. `display`

$$
x
$$

2. `display`

$$
x(x - 1)
$$

3. `display`

$$
x(x - 1)(x - 2)
$$

4. `display`

$$
x(x - 1)(x - 2)(x - 3)
$$

5. `display`

$$
x(x - 1)(x - 2)(x - 3)(x - 4)
$$

6. `display`

$$
x
$$

7. `display`

$$
-x + x^2
$$

8. `display`

$$
2x - 3x^2 + x^3
$$

9. `display`

$$
-6x + 11x^2 - 6x^3 + x^4
$$

10. `display`

$$
24x - 50x^2 + 35x^3 - 10x^4 + x^5
$$

11. `inline`

`$n!$`

### Uncertain Items

- None.

## Page 13

### English Text

Title: Factorial

- For positive integers `n`, the factorial is defined as
- This satisfies the functional equation `n! = n x (n - 1)!` Using this, we see that `1! = 1 x 0!`, which implies `0! = 1`.
- We'll eventually need to know the "factorial" of a non-integer or complex number!

### Formulas

1. `display`

$$
n! = n(n - 1)\cdots 2 \times 1
$$

2. `display`

$$
1! = 1
$$

3. `display`

$$
2! = 2 \times 1 = 2
$$

4. `display`

$$
3! = 3 \times 2 \times 1 = 6
$$

5. `display`

$$
4! = 4 \times 3 \times 2 \times 1 = 24
$$

6. `inline`

`$n! = n \times (n - 1)!$`

7. `inline`

`$1! = 1 \times 0!$`

8. `inline`

`$0! = 1$`

### Uncertain Items

- None.

## Page 14

### English Text

Title: Euler's proof of the Basel Problem

### Formulas

1. `display`

$$
\frac{1}{0!}x
$$

2. `display`

$$
\frac{1}{1!}x(x - 1)
$$

3. `display`

$$
\frac{1}{2!}x(x - 1)(x - 2)
$$

4. `display`

$$
\frac{1}{3!}x(x - 1)(x - 2)(x - 3)
$$

5. `display`

$$
\frac{1}{4!}x(x - 1)(x - 2)(x - 3)(x - 4)
$$

6. `display`

$$
\frac{1}{0!}(x)
$$

7. `display`

$$
\frac{1}{1!}(-x + \cdots)
$$

8. `display`

$$
\frac{1}{2!}(2x + \cdots)
$$

9. `display`

$$
\frac{1}{3!}(-6x + \cdots)
$$

10. `display`

$$
\frac{1}{4!}(24x + \cdots)
$$

### Uncertain Items

- None.

## Page 15

### English Text

Title: Euler's proof of the Basel Problem

### Formulas

1. `display`

$$
\frac{1}{0!}x
$$

2. `display`

$$
\frac{1}{1!}x(x - 1)
$$

3. `display`

$$
\frac{1}{2!}x(x - 1)(x - 2)
$$

4. `display`

$$
\frac{1}{3!}x(x - 1)(x - 2)(x - 3)
$$

5. `display`

$$
\frac{1}{4!}x(x - 1)(x - 2)(x - 3)(x - 4)
$$

6. `display`

$$
x
$$

7. `display`

$$
-x + \cdots
$$

8. `display`

$$
x + \cdots
$$

9. `display`

$$
-x + \cdots
$$

10. `display`

$$
x + \cdots
$$

### Uncertain Items

- None.

## Page 16

### English Text

Title: Euler's proof of the Basel Problem

### Formulas

1. `display`

$$
x = x
$$

2. `display`

$$
x(x - 1) = -x(1 - x)
$$

3. `display`

$$
x(x - 1)(x - 2) = x(1 - x)(2 - x)
$$

4. `display`

$$
x(x - 1)(x - 2)(x - 3) = -x(1 - x)(2 - x)(3 - x)
$$

5. `display`

$$
x(x - 1)(x - 2)(x - 3)(x - 4)
= x(1 - x)(2 - x)(3 - x)(4 - x)
$$

### Uncertain Items

- None.

## Page 17

### English Text

Title: Euler's proof of the Basel Problem

### Formulas

1. `display`

$$
\frac{1}{0!}x
$$

2. `display`

$$
\frac{1}{1!}x(1 - x)
$$

3. `display`

$$
\frac{1}{2!}x(1 - x)(2 - x)
$$

4. `display`

$$
\frac{1}{3!}x(1 - x)(2 - x)(3 - x)
$$

5. `display`

$$
\frac{1}{4!}x(1 - x)(2 - x)(3 - x)(4 - x)
$$

6. `display`

$$
x
$$

7. `display`

$$
x + \cdots
$$

8. `display`

$$
x + \cdots
$$

9. `display`

$$
x + \cdots
$$

10. `display`

$$
x + \cdots
$$

### Uncertain Items

- None.

## Page 18

### English Text

Title: Euler's proof of the Basel Problem

- Remember this is a function with zeros at `0, 1, 2, 3, 4`, and the first term of its Taylor series is `x` (as opposed to e.g. `24x`).

### Formulas

1. `display`

$$
\frac{1}{4!}x(1 - x)(2 - x)(3 - x)(4 - x)
$$

2. `display`

$$
= \frac{1}{1}\cdot\frac{1}{2}\cdot\frac{1}{3}\cdot\frac{1}{4}
\cdot x(1 - x)(2 - x)(3 - x)(4 - x)
$$

3. `display`

$$
= x \cdot \frac{1}{1}(1 - x)
\cdot \frac{1}{2}(2 - x)
\cdot \frac{1}{3}(3 - x)
\cdot \frac{1}{4}(4 - x)
$$

4. `display`

$$
= x(1 - x)\cdot\left(1 - \frac{x}{2}\right)
\cdot\left(1 - \frac{x}{3}\right)
\cdot\left(1 - \frac{x}{4}\right)
$$

### Uncertain Items

- The final displayed line visually appears as a product, but multiplication dots between the parenthesized factors are not shown.

## Page 19

### English Text

Title: Euler's proof of the Basel Problem

- Remember this is the factorization of a function with zeros at `0, 1, 2, 3, 4` and the first term of its Taylor series is `x` (as opposed to e.g. `24x`).
- `sin x` has zeros at `0, +- pi, +- 2pi, +- 3pi, ...`, and the first term of its Taylor series is `x`. Euler concluded that its factorization must be
- This step is sketchy because you can't just apply a result that works for finite cases to infinite cases. It was proved much later that you can indeed factor functions into infinite products based on their zeros--the Weierstrass Factorization Theorem (1870s).

### Formulas

1. `display`

$$
x(1 - x)\cdot\left(1 - \frac{x}{2}\right)
\cdot\left(1 - \frac{x}{3}\right)
\cdot\left(1 - \frac{x}{4}\right)
$$

2. `display`

$$
x\left(1 - \frac{x}{\pi}\right)
\left(1 + \frac{x}{\pi}\right)
\left(1 - \frac{x}{2\pi}\right)
\left(1 + \frac{x}{2\pi}\right)
\left(1 - \frac{x}{3\pi}\right)
\left(1 + \frac{x}{3\pi}\right)\cdots
$$

### Uncertain Items

- The product symbols on the slide are written by juxtaposition. In the formula above, adjacent parenthesized terms should be read as multiplied.

## Page 20

### English Text

Title: Euler's proof of the Basel Problem

- Remember that `(a - b)(a + b) = a^2 - b^2`. So each pair of terms can be combined, for example:
- So the factorization becomes
- Dividing both sides by `x`:

### Formulas

1. `display`

$$
x\left(1 - \frac{x}{\pi}\right)
\left(1 + \frac{x}{\pi}\right)
\left(1 - \frac{x}{2\pi}\right)
\left(1 + \frac{x}{2\pi}\right)
\left(1 - \frac{x}{3\pi}\right)
\left(1 + \frac{x}{3\pi}\right)\cdots
$$

2. `inline`

`$(a - b)(a + b) = a^2 - b^2$`

3. `display`

$$
\left(1 - \frac{x}{3\pi}\right)
\left(1 + \frac{x}{3\pi}\right)
= 1 - \frac{x^2}{9\pi^2}
$$

4. `display`

$$
\sin x = x\left(1 - \frac{x^2}{\pi^2}\right)
\left(1 - \frac{x^2}{4\pi^2}\right)
\left(1 - \frac{x^2}{9\pi^2}\right)\cdots
$$

5. `display`

$$
\frac{\sin x}{x}
= \left(1 - \frac{x^2}{\pi^2}\right)
\left(1 - \frac{x^2}{4\pi^2}\right)
\left(1 - \frac{x^2}{9\pi^2}\right)\cdots
$$

### Uncertain Items

- The slide uses juxtaposition for multiplication between factors.

## Page 21

### English Text

Title: Euler's proof of the Basel Problem

Graph labels:

- `f(x) = sin x`
- `g(x) = x(1 - x^2/pi^2)(1 - x^2/(4pi^2))(1 - x^2/(9pi^2))(1 - x^2/(16pi^2))`

### Formulas

1. `display`

$$
f(x) = \sin x
$$

2. `display`

$$
g(x) = x
\left(1 - \frac{x^2}{\pi^2}\right)
\left(1 - \frac{x^2}{4\pi^2}\right)
\left(1 - \frac{x^2}{9\pi^2}\right)
\left(1 - \frac{x^2}{16\pi^2}\right)
$$

### Uncertain Items

- Graph compares `f(x)` and `g(x)`.
- The displayed formula uses juxtaposed factors for multiplication.

## Page 22

### English Text

Title: Euler's proof of the Basel Problem

Graph labels repeat Page 21.

Large red correction:

- close to `sin(x)`, not close to `pi`*

### Formulas

Same formulas as Page 21.

### Uncertain Items

- Graph compares `f(x)` and `g(x)`.

## Page 23

### English Text

Title: Euler's proof of the Basel Problem

- Multiply out the product and collect terms carefully:
- All the `1`'s multiplied out becomes `1`. So
- There can't be an `x` term, so the next term has to be `x^2`. The `x^2` term involves selecting a `1` from every term in the product except one term, where we select the `-x^2/(n^2 pi^2)` term. Hence

### Formulas

1. `display`

$$
\frac{\sin x}{x}
= \left(1 - \frac{x^2}{\pi^2}\right)
\left(1 - \frac{x^2}{4\pi^2}\right)
\left(1 - \frac{x^2}{9\pi^2}\right)\cdots
$$

2. `display`

$$
\frac{\sin x}{x} = 1 + \cdots
$$

3. `display`

$$
\frac{\sin x}{x}
= 1 + \left(
-\frac{1}{\pi^2}
-\frac{1}{4\pi^2}
-\frac{1}{9\pi^2}
-\cdots
\right)x^2 + \cdots
$$

4. `display`

$$
= 1 - \frac{1}{\pi^2}
\left(1 + \frac{1}{4} + \frac{1}{9} + \cdots\right)x^2 + \cdots
$$

5. `display`

$$
= 1 - \frac{1}{\pi^2}\zeta(2)x^2 + \cdots
$$

### Uncertain Items

- The product in formula 1 is visually multiplication by juxtaposition.

## Page 24

### English Text

Title: Euler's proof of the Basel Problem

Left heading:

- Taylor series of `sin x`:

Right text:

- Euler assumed he could factor `sin x` as a product of terms involving its zeros. Then he showed the first terms are:
- The `x^2` term on the left must equal the `x^2` term on the right, so
- Therefore,

### Formulas

1. `display`

$$
\sin x = x - \frac{1}{3!}x^3 + \frac{1}{5!}x^5 - \cdots
$$

2. `display`

$$
\frac{\sin x}{x}
= 1 - \frac{1}{3!}x^2 + \frac{1}{5!}x^4 - \cdots
$$

3. `display`

$$
\frac{\sin x}{x}
= 1 - \frac{\zeta(2)}{\pi^2}x^2 + \cdots
$$

4. `display`

$$
-\frac{1}{3!} = -\frac{\zeta(2)}{\pi^2}
$$

5. `display`

$$
\zeta(2) = \frac{\pi^2}{6}
$$

### Uncertain Items

- Slide highlights the matching `x^2` coefficients in green.

## Page 25

### English Text

Title: Euler's proof of the Basel Problem

- Next time: Analyzing `zeta(s)` in the complex plane and discussing convergence.

### Formulas

1. `inline`

`$\zeta(s)$`

### Uncertain Items

- None.

## Page 26

### English Text

Title: Feedback

- Let me know if you have feedback!
- Was the pacing too fast/too slow?
- Was subject too easy/too difficult?
- Did I skip over important steps?
- Were there parts that didn't make sense or seemed unjustified?
- Was it interesting or did it seem pointless?
- Did you spot any errors? I probably made some.
- What can I do better?

### Formulas

None.

### Uncertain Items

- None.
