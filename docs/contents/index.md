# Introduction

Riemann zeta function의 수학적 구조를 단계별로 학습하는 개인 학습 노트이다.

---

## About This Course

이 시리즈는 총 78개 강의로 구성된다. Basel problem $\zeta(2) = \pi^2/6$의
증명을 출발점으로 삼아, Riemann zeta function의 수학적 구조를 체계적으로 탐구하며,
최종적으로 critical strip 내 zeros의 개수를 $O(T \log T)$로 추정하는
Riemann–von Mangoldt equation에 이른다.

수강자는 calculus와 complex numbers에 대한 기본 지식을 갖추고 있다고 가정한다.
Complex analysis의 일반적인 결과는 증명 없이 인용하고, zeta function에 직접
관련된 결과만 상세히 증명하므로, complex analysis를 사전에 학습하지 않아도
수강이 가능하다.

주요 주제는 다음과 같다.

- Euler product formula와 analytic continuation
- Laurent series, functional equation $\zeta(s) = \zeta(1-s)$
- Hadamard product formula와 nontrivial zeros의 분포
- Riemann–von Mangoldt formula
- Classical zero-free region과 Prime number theorem
- Riemann–Siegel formula와 Hardy Z-function
- Dirichlet series, Möbius function, Mertens conjecture
- Mean value theorems와 omega results
- Riemann hypothesis와 Lindelöf hypothesis

---

## Lecture List

| No. | Title | Notes |
|----:|-------|-------|
| 001 | Intro and the Basel Problem | {doc}`lec-001/lec-001_notes` |
| 002 | Zeta in the Complex Plane | |
| 003 | Analytic Properties of Zeta | |
| 004 | The Euler Product Formula | |
| 005 | Proof that Zeta has No Zeros with Re(s) > 1 | |
| 006 | The Logarithmic Derivative and the Von Mangoldt Function | |
| 007 | Intro to Analytic Continuation | |
| 008 | The Dirichlet Eta Function | |
| 009 | Riemann–Stieltjes Integration | |
| 010 | Euler–Maclaurin Summation | |
| 011 | The Laurent Series of the Zeta Function at s=1 | |
| 012 | The Explicit Formula for Zeta at Even Integers | |
| 013 | Proof that the Zeta Function Has No Zeros on the Line Re(s) = 1 | |
| 014 | Intro to the Gamma Function | |
| 015 | Riemann's Functional Equation Connects ζ(s) and ζ(1-s) | |
| 016 | Proof of Riemann's Functional Equation | |
| 017 | Riemann's Xi Function | |
| 018 | Growth Rates of Complex Functions | |
| 019 | Proof that the Number of Zeros in the Critical Strip Is O(T log T) | |
| 020 | Hadamard's Factorization of the Zeta Function | |
| 021 | The Riemann–von Mangoldt Formula | |
| 022 | The Classical Zero-Free Region Inside the Critical Strip | |
| 023 | Intro to Exponential Sums | |
| 024 | An Approximate Functional Equation for Zeta | |
| 025 | The Lindelöf Hypothesis | |
| 026 | The Phragmén–Lindelöf Principle | |
| 027 | The Prime Number Theorem (1/2) | |
| 028 | The Prime Number Theorem (2/2) | |
| 029 | Visualizing the Riemann Hypothesis | |
| 030 | The Riemann–Siegel Z Function | |
| 031 | Dirichlet Series | |
| 032 | Möbius Inversion | |
| 033 | The Mertens Conjecture | |
| 034 | How the Mertens Conjecture was Disproved | |
| 035 | Diophantine Approximation | |
| 036 | Omega Results for Re(s) ≥ 1 | |
| 037 | Zeta Can Get Close to Zero in Re(s) ≥ 1 | |
| 038 | Mean Value Theorems of Zeta | |
| 039 | Riemann's Global Equation for ζ | |
| 040 | Riemann's Proof of the Functional Equation | |
| 041 | Riemann's Second Proof of the Functional Equation | |
| 042 | Riemann's ξ Function and the Origin of the Riemann Hypothesis | |
| 043 | Riemann's Connection Between ζ and Primes | |
| 044 | Primes as Waves | |
| 045 | Von Mangoldt's Explicit Formula for ψ(x) | |
| 046 | Zeta at Zero | |
| 047 | The Truncated Explicit Formula for ψ(x) | |
| 048 | Proof of the Prime Number Theorem | |
| 049 | An Omega Bound on the Prime Number Theorem | |
| 050 | Littlewood's Log Log Log Bound | |
| 051 | Skewes' Number and Gauss's False Conjecture on Primes | |
| 052 | Prime Gaps | |
| 053 | Zeta Gaps (Are ≤12) | |
| 054 | Littlewood's Log Log Log Bound on Zeta Gaps | |
| 055 | S(T) and the Accuracy of the Riemann–von Mangoldt Formula | |
| 056 | S(T) as a Divergent Sum of Prime Waves | |
| 057 | The Duality of Primes and Zeta Zeros | |
| 058 | The Riemann–Siegel Z and θ Functions | |
| 059 | Gram Points and Gram's Law | |
| 060 | Hardy's Proof of Infinitely Many Zeros on Critical Line | |
| 061 | The Hardy–Littlewood Approximate Functional Equation | |
| 062 | The Cosine Sum on the Critical Line | |
| 063 | The Riemann–Siegel Formula | |
| 064 | Computational Methods for Zeta | |
| 065 | Example Computations and How to Find a Zero | |
| 066 | Edwards' Speculation on the Riemann Hypothesis | |
| 067 | Historical Verification of the Riemann Hypothesis | |
| 068 | Turing's Method of Verifying the Riemann Hypothesis | |
| 069 | Deep Dive into Gamma (Weierstrass Product Formula) | |
| 070 | Proving Gamma Formulas | |
| 071 | Laplace's Method for Stirling's Approximation | |
| 072 | The Saddle-Point Method for Stirling's Approximation | |
| 073 | The Riemann–Siegel Formula via Saddle-Point Method | |
| 074 | Titchmarsh's Proof of Infinitely Many Zeros on Critical Line | |
| 075 | The Visible Grid Problem | |
| 076 | Euler's Totient Function and its Dirichlet Series | |
| 077 | Square-Free and k-Free Numbers | |
| 078 | Powerful Numbers | |

---

## Reference

- Ivić, A. (1985). *The Riemann Zeta-Function*. John Wiley & Sons, New York.
- Titchmarsh, E. C. (1986). *The Theory of the Riemann Zeta-Function* (2nd ed., revised by D. R. Heath-Brown). Oxford University Press, Oxford.
- Edwards, H. M. (1974). *Riemann's Zeta Function*. Academic Press, New York.
- Davenport, H. (2000). *Multiplicative Number Theory* (3rd ed.). Springer, New York.
- Euler, L. (1740). De summis serierum reciprocarum. *Commentarii academiae scientiarum Petropolitanae*, 7, 123–134.
- Riemann, B. (1859). Über die Anzahl der Primzahlen unter einer gegebenen Grösse. *Monatsberichte der Berliner Akademie*.
- YouTube: [Zeta Explained](https://youtube.com/playlist?list=PLTcPERDxgHxm7TzJ9W92S-l5pGRuhZz10)
