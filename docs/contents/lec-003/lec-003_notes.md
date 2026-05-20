# Analytic Properties of Zeta

> $\zeta(s)$의 부분합(partial sum)이 $\operatorname{Re}(s) \geq 1 + a$인 영역에서 균등 수렴(uniform convergence)함을 증명하고, 균등 극한 정리(uniform limit theorem)를 통해 $\zeta(s)$가 $\operatorname{Re}(s) > 1$에서 해석 함수(analytic function)임을 확립한다.

- **Source**: [Zeta Explained #003](https://youtu.be/BFHXTkVaQAc)
- **Reference**: *The Riemann Zeta-Function* by Aleksandar Ivić (1985)

**Overview**

Riemann 제타 함수를 설명하는 시리즈의 세 번째 강의이다. $\operatorname{Re}(s) > 1$인 복소수 $s$에 대해 $\zeta(s)$가 어떤 해석적(analytic) 성질을 갖는지 규명하는 것이 이 강의의 목표이다. 먼저 균등 수렴과 점별 수렴(pointwise convergence)의 차이를 명확히 한다. 이어서 $x > 1$ 전체 영역에서는 $\zeta(x)$의 부분합이 균등 수렴하지 않음을 반례로 보이고, $a > 0$을 고정하여 영역을 $\operatorname{Re}(s) \geq 1 + a$로 제한하면 균등 수렴이 성립함을 증명한다. 마지막으로 복소 해석학의 균등 극한 정리를 적용하여 $\zeta(s)$가 $\operatorname{Re}(s) > 1$에서 해석 함수임을 결론 내린다. 수강자는 미적분학과 복소수에 대한 기본 지식을 갖추고 있다고 가정하며, 복소 해석학의 관련 개념은 필요에 따라 설명한다.

**Contents**

- 강의 도입: $\operatorname{Re}(s) > 1$에서 $\zeta(s)$의 해석적 성질 개요
- 균등 수렴의 정의 및 직관적 설명
- 점별 수렴과 균등 수렴의 차이: $N$의 선택 순서
- $x > 1$에서 $\zeta(x)$의 부분합이 균등 수렴하지 않음을 보이는 반례
- $\operatorname{Re}(s) \geq 1 + a$에서 부분합의 균등 수렴 증명
- 복소 해석학에서 균등 수렴이 중요한 이유
- 해석 함수의 정의 및 예시
- 균등 극한 정리 적용: $\zeta(s)$가 $\operatorname{Re}(s) > 1$에서 해석 함수임을 결론

---

## 1. 강의 목표와 증명 전략

Riemann 제타 함수는 $\operatorname{Re}(s) > 1$인 복소수 $s$에 대해 다음과 같이 정의된다.

$$
\begin{equation}
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}
\end{equation}
$$

이 강의의 목표는 $\zeta(s)$가 이 영역에서 어떤 해석적 성질을 갖는지 규명하는 것이다. 구체적으로 연속성, 미분 가능성 등을 포함하는 성질들이 탐구된다. 증명은 두 단계로 진행된다.

첫째, $\zeta(s)$의 부분합으로 이루어진 함수열이 $\operatorname{Re}(s) \geq 1 + a$인 영역에서 균등 수렴함을 보인다. 여기서 $a > 0$은 임의로 고정된 양의 실수이다. $s \to 1$일 때 $\zeta(s) \to \infty$이므로 $s = 1$의 특이점(singularity) 근방에서의 발산을 피하기 위해, $a > 0$으로 영역의 경계를 $\operatorname{Re}(s) = 1$에서 멀리 떨어뜨린다.

둘째, 복소 해석학의 균등 극한 정리를 적용하여 $\zeta(s)$가 $\operatorname{Re}(s) > 1$에서 해석 함수임을 결론 내린다. 해석 함수는 단순히 연속이거나 미분 가능한 함수보다 훨씬 강한 조건을 만족하는 함수로, 무한히 미분 가능하며 복소 해석학의 강력한 도구들을 적용할 수 있다.

---

## 2. 점별 수렴과 균등 수렴

### 부분합의 정의

$\zeta(s)$의 $n$번째 부분합을 다음과 같이 정의한다.

$$
\begin{equation}
f_n(s) = \sum_{k=1}^{n} \frac{1}{k^s}
\end{equation}
$$

인덱스 변수로 $k$를 사용하는 것은, $n$이 이미 함수열의 인덱스로 쓰이기 때문이다. 처음 몇 항은 다음과 같다.

$$
f_1(s) = 1, \quad
f_2(s) = 1 + \frac{1}{2^s}, \quad
f_3(s) = 1 + \frac{1}{2^s} + \frac{1}{3^s}, \quad
f_4(s) = 1 + \frac{1}{2^s} + \frac{1}{3^s} + \frac{1}{4^s}
$$

목표는 이 함수열 $\{f_n(s)\}$가 어떤 영역에서 $\zeta(s)$로 균등 수렴함을 보이는 것이다. $f_n(s)$는 이 강의 전반에 걸쳐 부분합 함수열로 사용된다.

### 점별 수렴의 정의

점별 수렴은 미적분학에서 흔히 마주치는 수렴 개념이다. 함수열 $f_1, f_2, \ldots$이 $f$로 점별 수렴한다는 것은, 다음 조건이 성립함을 의미한다.

임의의 점 $x$를 먼저 고정한다. 그 후 임의의 $\epsilon > 0$에 대해, $n \geq N$이면 $|f(x) - f_n(x)| < \epsilon$을 만족하는 인덱스 $N$이 존재한다.

핵심은 $N$이 먼저 고정된 점 $x$에 의존할 수 있다는 것이다. 즉, 점 $x$마다 서로 다른 $N$을 선택하는 것이 허용된다.

이전 강의의 적분 판정법을 통해 $x > 1$일 때 $\zeta(x)$가 점별 수렴함은 이미 증명되었다.

### 균등 수렴의 정의

균등 수렴은 점별 수렴보다 강한 개념으로, $\epsilon$과 점의 선택 순서가 역전된다.

복소함수열 $\{f_n\}$이 영역 $A$ 위에서 $f$로 균등 수렴한다는 것은, 다음 조건이 성립함을 의미한다.

임의의 $\epsilon > 0$을 먼저 고정한다 (점을 먼저 고정하지 않는다). 그 후 $n \geq N$이면 영역 $A$ 내의 **모든** 점 $z$에 대해 **동시에** $|f(z) - f_n(z)| < \epsilon$을 만족하는 인덱스 $N$이 존재한다.

핵심적인 차이는 $N$의 선택 방식이다. 균등 수렴에서 $N$은 영역 내의 모든 점에 대해 동시에 유효하여야 하며, 점에 의존할 수 없다. 직관적으로는, 함수열이 영역 전체에서 동일한 속도로 극한함수에 수렴하는 것이 균등 수렴이다.

---

## 3. $x > 1$에서 균등 수렴이 성립하지 않는 반례

$\zeta(x)$의 부분합이 실수 영역 $x > 1$ 전체에서 균등 수렴하지 않음을 반례로 보인다. 여기서는 실수 입력만을 고려한다.

$\epsilon = 0.005$로 고정한다. 우선 $f_n(x)$에 대한 상한을 구한다. $f_n(x) = \sum_{k=1}^n 1/k^x$의 각 항은 $1/k^x \leq 1$이므로, $f_n(x) \leq n$이다.

이제 $x = 1 + \frac{1}{n+1}$로 선택한다. 이전 강의의 적분 판정법 결과에 의해

$$
\zeta\!\left(1 + \frac{1}{n+1}\right) > \frac{1}{\left(1 + \frac{1}{n+1}\right) - 1} = n + 1
$$

이 성립한다. 따라서

$$
|\zeta(x) - f_n(x)| \geq (n+1) - n = 1 > 0.005
$$

이므로, $n \geq N$인 임의의 $n$에 대해 위 부등식을 만족하는 점 $x = 1 + \frac{1}{n+1}$이 항상 존재한다. 즉, 어떤 고정된 $N$을 선택하더라도 균등 수렴의 정의를 만족할 수 없다. 따라서 $f_n$은 $x > 1$ 전체에서 균등 수렴하지 않는다.

이 반례의 핵심 원인은 $x = 1$에서의 특이점이다. $x$를 $1$에 임의로 가깝게 선택하면 $\zeta(x)$의 값을 임의로 크게 만들 수 있으므로, $f_n$이 $\zeta$를 영역 전체에서 균일하게 근사하는 것이 불가능하다. 바꾸어 말하면, 특이점에서 멀어질수록 $\zeta(x)$가 빠르게 안정되므로, 특이점 근방을 영역에서 배제하면 균등 수렴이 회복될 수 있다.

![$y = \zeta(x)$와 $y = f_2(x)$의 그래프 비교](images/fig-003-001.png)

**Figure 1.** $y = \zeta(x)$와 $y = f_2(x) = 1 + 1/2^x$의 그래프 비교

실수 $x > 1$에서 $y = \zeta(x)$ (적색)와 $y = f_2(x) = 1 + 1/2^x$ (청색)를 함께 나타낸 그래프이다. $x \to 1^+$일 때 $\zeta(x)$가 발산하여 $f_2(x)$와의 차이가 무한히 커지는 반면, $x$가 충분히 크면 두 함수의 차이는 작아진다. 이 그래프는 $x > 1$ 전체에서 부분합이 균등 수렴하지 않음을 시각적으로 보여준다. $x = 1$의 특이점 근방에서 임의로 큰 오차가 발생하므로, 모든 $x > 1$에 대해 균일하게 유효한 $N$을 선택하는 것은 불가능하다. $a > 0$을 먼저 고정하고 영역을 $x \geq 1 + a$로 제한하면 이 문제가 해결됨을 다음 섹션에서 증명한다.

---

## 4. $\operatorname{Re}(s) \geq 1 + a$에서의 균등 수렴 증명

### Step 1. 꼬리 합의 정의

균등 수렴을 보이기 위해, $f$와 $f_n$의 차이에 해당하는 꼬리 합(tail sum) $R_n(s)$을 정의한다.

$$
\begin{equation}
R_n(s) = \zeta(s) - f_n(s) = \sum_{k=n+1}^{\infty} \frac{1}{k^s}
\end{equation}
$$

$R_n(s)$는 $\zeta(s)$의 무한급수에서 처음 $n$개의 항을 제거한 나머지 합이다. 균등 수렴의 정의에서 $|f(z) - f_n(z)|$에 해당하는 양이 바로 $|R_n(s)|$이다. 따라서 임의의 $\epsilon > 0$에 대해 $\operatorname{Re}(s) \geq 1 + a$인 모든 $s$에 대해 동시에 $|R_n(s)| < \epsilon$을 만족하는 $N$이 존재함을 보이면 충분하다.

표준 표기에 따라 $s = \sigma + it$ ($\sigma = \operatorname{Re}(s)$, $t = \operatorname{Im}(s)$)로 쓴다. 이 강의에서 $\log$는 자연로그 $\log_e$를 의미한다.

### Step 2. $|R_n(\sigma + it)| \leq R_n(\sigma)$

$s = \sigma + it$를 대입하고 이전 강의와 동일한 지수 전개를 적용한다.

$$
\begin{align*}
R_n(s)
= \sum_{k=n+1}^{\infty} \frac{1}{k^{\sigma+it}}
= \sum_{k=n+1}^{\infty} \frac{1}{k^{\sigma}} \cdot \frac{1}{k^{it}}
= \sum_{k=n+1}^{\infty} \frac{1}{k^{\sigma}} \cdot \left(e^{\log k}\right)^{-it}
= \sum_{k=n+1}^{\infty} \frac{1}{k^{\sigma}} e^{-it(\log k)}
\end{align*}
$$

이제 삼각 부등식과 $|e^{-it(\log k)}| = 1$을 이용한다.

$$
\begin{align*}
|R_n(\sigma + it)|
&= \left|\sum_{k=n+1}^{\infty} \frac{1}{k^{\sigma}} e^{-it(\log k)}\right| \\
&\leq \sum_{k=n+1}^{\infty} \left|\frac{1}{k^{\sigma}} e^{-it(\log k)}\right|
\qquad \text{(삼각 부등식)} \\
&= \sum_{k=n+1}^{\infty} \left|\frac{1}{k^{\sigma}}\right| \cdot \left|e^{-it(\log k)}\right|
\qquad \text{($|zw| = |z||w|$)} \\
&= \sum_{k=n+1}^{\infty} \frac{1}{k^{\sigma}}
\qquad \left(\left|e^{-it(\log k)}\right| = 1\right)
\end{align*}
$$

따라서 다음이 성립한다.

$$
\begin{equation}
|R_n(\sigma + it)| \leq R_n(\sigma)
\end{equation}
$$

임의의 복소수 $s = \sigma + it$에서 꼬리 합의 절댓값은, 같은 실수부 $\sigma$를 갖는 실수에서의 꼬리 합 값으로 bound된다. 이 단계는 이전 강의에서 $|\zeta(\sigma + it)| \leq \zeta(\sigma)$를 도출한 논리와 완전히 동일한 구조이며, 합산의 시작 인덱스만 $n + 1$로 바뀐 것이다.

### Step 3. $R_n(\sigma) \leq R_n(1 + a)$

$\sigma \geq 1 + a$인 실수 $\sigma$에 대해 $R_n(\sigma)$와 $R_n(1 + a)$의 각 항을 비교한다.

$$
R_n(1+a) = \frac{1}{(n+1)^{1+a}} + \frac{1}{(n+2)^{1+a}} + \frac{1}{(n+3)^{1+a}} + \cdots
$$

$$
R_n(\sigma)\ = \frac{1}{(n+1)^{\sigma}} + \frac{1}{(n+2)^{\sigma}} + \frac{1}{(n+3)^{\sigma}} + \cdots
$$

$\sigma \geq 1 + a$이면 각 $k \geq n + 1$에 대해 $k^\sigma \geq k^{1+a}$이므로,

$$
\frac{1}{k^{\sigma}} \leq \frac{1}{k^{1+a}}
$$

항별 비교에 의해 다음이 성립한다.

$$
\begin{equation}
R_n(\sigma) \leq R_n(1+a)
\end{equation}
$$

### Step 4. 균등 수렴의 확립

Step 2와 Step 3를 결합하면, $\sigma = \operatorname{Re}(s) \geq 1 + a$인 임의의 복소수 $s = \sigma + it$에 대해

$$
\begin{equation}
|R_n(\sigma + it)| \leq R_n(\sigma) \leq R_n(1 + a)
\end{equation}
$$

이 성립한다. 이제 고정점 $s = 1 + a$에서의 점별 수렴을 이용한다. 이전 강의에서 적분 판정법으로 $\operatorname{Re}(s) > 1$이면 $\zeta(s)$가 점별 수렴함을 보였으므로, 임의의 $\epsilon > 0$에 대해

$$
n \geq N \implies R_n(1+a) < \epsilon
$$

을 만족하는 $N$이 존재한다. 바로 이 $N$을 $\operatorname{Re}(s) \geq 1 + a$인 모든 $s$에 대해 공통으로 사용하면,

$$
n \geq N \implies |R_n(\sigma + it)| \leq R_n(\sigma) \leq R_n(1+a) < \epsilon
$$

이 성립한다. 이 $N$은 특정 점 $s$에 의존하지 않으며, 영역 내의 모든 점에 대해 동시에 유효하다. 따라서 균등 수렴의 정의가 만족된다.

이 논리가 성립하는 이유를 요약하면 다음과 같다. 어떤 점 $\sigma + it$에서 $|R_n(\sigma + it)|$를 통제하고 싶은데, 이 값이 Step 2에 의해 실수 $R_n(\sigma)$로 bound되고, Step 3에 의해 다시 고정점 $R_n(1+a)$로 bound된다. $R_n(1+a)$는 오직 $n$에만 의존하므로, $n$을 충분히 크게 선택하면 영역 내 모든 점에서 꼬리 합을 동시에 $\epsilon$ 미만으로 만들 수 있다.

> **결론**: $a > 0$을 고정하면 함수열 $\{f_n(s)\}$는 $\operatorname{Re}(s) \geq 1 + a$인 영역에서 $\zeta(s)$로 균등 수렴한다.

![복소평면에서 $\operatorname{Re}(s) \geq 1 + a$ 영역과 균등 수렴 증명 구조](images/fig-003-002.png)

**Figure 2.** $\operatorname{Re}(s) \geq 1 + a$ 영역에서의 균등 수렴 증명 구조

복소평면에서 $\operatorname{Re}(s) \geq 1 + a$인 영역(회색 음영)과 임의의 점 $\sigma + it$를 나타낸다. 가로축은 $\operatorname{Re}(s)$, 세로축은 $\operatorname{Im}(s)$이며, $s = 1$은 $\zeta(s)$의 특이점으로 영역에 포함되지 않는다. 증명의 핵심 구조는 영역 내 임의의 점 $\sigma + it$에서의 $|R_n(\sigma + it)|$를, 먼저 삼각 부등식으로 실수축 위의 $R_n(\sigma)$로, 이어서 항별 비교로 경계선 위의 $R_n(1+a)$로 bound하는 부등식 연쇄이다. 경계선 위의 고정점 $s = 1 + a$에서의 점별 수렴 하나만으로 영역 전체의 균등 수렴을 이끌어낼 수 있으며, 선택된 $N$은 영역 내 모든 $s$에 대해 동시에 유효하다. 이 슬라이드의 부등식 연쇄 $|R_n(\sigma + it)| \leq R_n(\sigma) \leq R_n(1+a) < \epsilon$이 증명의 최종 단계이다.

---

## 5. Weierstrass M-판정법 (보충)

슬라이드에서 Weierstrass M-판정법(Weierstrass M-test)을 보충으로 소개하고 있다.

> **Weierstrass M-판정법**: 영역 $A$ 내의 모든 $n$과 $z$에 대해 $|f_n(z)| \leq M_n$이 성립하고, $\sum_{n=1}^{\infty} M_n$이 수렴하면, $\sum_{n=1}^{\infty} f_n(z)$는 영역 $A$에서 균등 수렴한다.

위의 균등 수렴 증명에서 $M_k = 1/k^{1+a}$로 설정하면 이 판정법을 직접 적용할 수 있다. 각 항 $|1/k^s| = 1/k^{\sigma} \leq 1/k^{1+a} = M_k$이고, $\sum M_k = \zeta(1+a)$가 수렴하므로, $\operatorname{Re}(s) \geq 1 + a$인 영역에서 $\sum_{k=1}^{\infty} 1/k^s$가 균등 수렴함을 한 번에 결론 내릴 수 있다.

강의자는 이 판정법으로 증명을 단축하는 대신, 부등식 연쇄를 직접 구성하는 방식을 택하였다. 그 이유는 복소 해석학의 정리를 연속적으로 인용하기보다, 각 단계의 직관을 먼저 구축하기 위해서이다.

---

## 6. $\zeta(s)$의 해석성(Analyticity)

### 균등 수렴이 중요한 이유

균등 수렴은 단순한 기술적 조건이 아니라, 수학적으로 유용한 연산을 정당화하는 핵심 조건이다. 균등 수렴이 확보되면 급수와 적분의 순서를 교환하거나, 급수와 미분의 순서를 교환하는 것이 허용된다. 이는 이후 강의에서 $\zeta(s)$를 분석할 때 반복적으로 사용되는 도구이다.

더 나아가, 복소 해석학의 강력한 도구들은 함수가 해석적(analytic)이라는 조건을 요구한다. 해석 함수는 단순히 연속이거나 미분 가능한 함수보다 훨씬 강한 조건을 만족한다. 복소 해석학에서 해석 함수는 "매우 잘 행동하는(very well-behaved)" 함수로, 무한히 미분 가능하고 멱급수(power series)로 전개되는 등 풍부한 성질을 갖는다.

### 해석 함수의 예시

다음과 같이 익숙한 함수들이 모두 해석 함수이다.

- 다항식: $z^5 - z^2 + 1$
- $\sin(z)$
- $e^z$
- $n^{-s} = e^{-\sigma(\log n)} \cdot e^{-it(\log n)}$ ($s = \sigma + it$, $\sigma > 1$, $n$은 양의 정수)

특히 마지막 항목은 $\zeta(s)$를 구성하는 각 항이 해석 함수임을 의미한다. 해석 함수의 유한 합, 곱, 합성 또한 해석 함수이다. 따라서 각 부분합

$$
f_n(s) = \sum_{k=1}^{n} \frac{1}{k^s}
$$

은 유한 개의 해석 함수의 합으로서 $\operatorname{Re}(s) > 1$에서 해석 함수이다.

### 균등 극한 정리와 최종 결론

균등 극한 정리(uniform limit theorem)는 복소 해석학의 핵심 정리 중 하나이다. 이 강의에서는 증명 없이 결과만 인용한다.

> **균등 극한 정리**: 함수열 $\{f_n\}$이 해석 함수들의 수열이고, 어떤 영역(domain) 위에서 $f$로 균등 수렴하면, $f$는 그 영역에서 해석 함수이다.

> **주의**: 이 정리는 증명 없이 인용된다. 극한 함수가 해석 함수가 되는 이유를 엄밀히 이해하려면 복소 해석학 교재를 참고하여야 한다. 이 강의 시리즈에서는 $\zeta(s)$에 직접 관련된 결과는 상세히 증명하되, 복소 해석학의 일반 정리는 결과만 인용하는 방침을 따른다.

이를 $\zeta(s)$에 적용하면 다음과 같이 결론 내릴 수 있다.

- 각 부분합 $f_n(s)$는 $\operatorname{Re}(s) > 1$에서 해석 함수이다.
- 함수열 $\{f_n(s)\}$는 $\operatorname{Re}(s) \geq 1 + a$에서 $\zeta(s)$로 균등 수렴함이 앞에서 증명되었다.
- 균등 극한 정리에 의해 $\zeta(s)$는 $\operatorname{Re}(s) \geq 1 + a$에서 해석 함수이다.

$a > 0$은 임의의 양수이므로 얼마든지 작게 선택할 수 있다. 임의의 점 $s_0$에 대해 $\operatorname{Re}(s_0) > 1$이면, $\operatorname{Re}(s_0) > 1 + a$를 만족하는 $a > 0$이 존재하고, 위 결론에 의해 $s_0$ 근방에서 $\zeta(s)$가 해석 함수이다. 따라서 다음을 얻는다.

$$
\textbf{$\zeta(s)$는 $\operatorname{Re}(s) > 1$인 열린 반평면 전체에서 해석 함수이다.}
$$

![복소평면에서 $\zeta(s)$가 해석적인 영역](images/fig-003-003.png)

**Figure 3.** 복소평면에서 $\zeta(s)$가 해석 함수인 영역 $\operatorname{Re}(s) > 1$

복소평면에서 $\zeta(s)$가 해석 함수인 영역 $\operatorname{Re}(s) > 1$ (녹색 음영)을 나타낸다. 가로축은 $\operatorname{Re}(s)$, 세로축은 $\operatorname{Im}(s)$이며, 경계선 $\operatorname{Re}(s) = 1$은 점선으로 표시되어 있다. $s = 1$은 $\zeta(s)$의 특이점이므로 영역에 포함되지 않는다. 이 강의에서 확립된 해석성은 $\operatorname{Re}(s) > 1$로 제한되며, 이후 강의들에서 해석적 연속을 통해 $\zeta(s)$를 복소평면의 나머지 영역으로 확장하게 된다. Figure 2와 비교하면, $a > 0$을 임의로 작게 취하여 $\operatorname{Re}(s) \geq 1 + a$에서의 결론을 열린 반평면 $\operatorname{Re}(s) > 1$ 전체로 확장하는 과정이 이 최종 결론에 반영되어 있다. 다음 몇 강의에서는 이 영역에서 $\zeta(s)$의 추가적인 성질을 탐구하며, 그 후 복소평면 전체로 확장을 다룬다.

---

## 7. Summary

- $\zeta(s)$의 $n$번째 부분합을 $f_n(s) = \sum_{k=1}^n k^{-s}$로 정의하며, $\zeta(s)$는 이 함수열의 극한이다.
- 점별 수렴에서는 $N$이 먼저 고정된 점에 의존할 수 있으나, 균등 수렴에서는 영역 내의 모든 점에 대해 동시에 유효한 $N$을 $\epsilon$만으로 결정하여야 한다.
- $x > 1$ 전체에서는 균등 수렴이 성립하지 않는다. $x = 1 + \frac{1}{n+1}$로 선택하면 $\zeta(x) > n + 1$이지만 $f_n(x) \leq n$이므로 $|R_n(x)| > 1$이 항상 성립하여, 어떤 $N$을 선택하더라도 균등 수렴의 조건을 만족할 수 없다.
- $a > 0$을 고정하고 영역을 $\operatorname{Re}(s) \geq 1 + a$로 제한하면, 꼬리 합에 대한 부등식 연쇄 $|R_n(\sigma+it)| \leq R_n(\sigma) \leq R_n(1+a)$를 통해 균등 수렴이 성립함을 증명하였다. 핵심은 고정점 $s = 1 + a$에서의 점별 수렴 하나가 영역 전체의 균등 수렴을 함의한다는 것이다.
- Weierstrass M-판정법에서 $M_k = 1/k^{1+a}$로 설정하면 위의 균등 수렴을 더 간결하게 도출할 수 있다.
- 균등 수렴은 급수와 적분, 급수와 미분의 순서를 교환하는 등의 연산을 정당화하며, 복소 해석학의 강력한 도구를 적용하기 위한 해석성의 조건을 확보하는 데 필수적이다.
- 각 부분합 $f_n(s)$는 해석 함수이고, 균등 극한 정리에 의해 그 균등 극한인 $\zeta(s)$도 $\operatorname{Re}(s) \geq 1 + a$에서 해석 함수이다.
- $a > 0$이 임의로 작을 수 있으므로, $\zeta(s)$는 $\operatorname{Re}(s) > 1$인 열린 반평면 전체에서 해석 함수이다.

---

## 8. Review Questions

1. 점별 수렴과 균등 수렴의 정의를 각각 서술하고, 두 개념의 핵심적인 차이를 $\epsilon$과 점의 선택 순서를 중심으로 설명하라.
2. $f_n(s)$가 $\operatorname{Re}(s) > 1$에서 점별 수렴함은 이전 강의에서 어떤 도구를 사용하여 보였는가? 그 논리의 핵심을 간략히 서술하라.
3. $\zeta(x)$의 부분합이 $x > 1$ 전체에서 균등 수렴하지 않음을 보이는 반례를 구성하라. $x = 1 + \frac{1}{n+1}$을 선택하면 왜 $|R_n(x)| > 1$이 성립하는가?
4. 꼬리 합 $R_n(s)$를 정의하고, 균등 수렴을 보이기 위해 이 개념을 도입하는 이유를 설명하라.
5. $|R_n(\sigma + it)| \leq R_n(\sigma)$를 삼각 부등식과 $|e^{-it(\log k)}| = 1$을 이용하여 증명하라.
6. $\sigma \geq 1 + a$일 때 $R_n(\sigma) \leq R_n(1 + a)$가 성립함을 항별 비교를 통해 서술하라.
7. 부등식 연쇄 $|R_n(\sigma+it)| \leq R_n(\sigma) \leq R_n(1+a)$를 이용하여 $\operatorname{Re}(s) \geq 1 + a$에서의 균등 수렴 증명을 완성하라. 고정점 $s = 1 + a$에서의 점별 수렴이 어떤 역할을 하는가?
8. Weierstrass M-판정법을 서술하고, $M_k = 1/k^{1+a}$로 설정하여 $\zeta(s)$의 균등 수렴에 이 판정법을 직접 적용하라.
9. 균등 극한 정리를 서술하고, 이를 $\zeta(s)$에 적용하여 $\zeta(s)$가 $\operatorname{Re}(s) > 1$에서 해석 함수임을 결론 짓는 논리를 서술하라.
10. $a > 0$이 증명에서 임의로 선택 가능하다는 사실이, $\zeta(s)$가 닫힌 반평면 $\operatorname{Re}(s) \geq 1 + a$가 아닌 열린 영역 $\operatorname{Re}(s) > 1$ 전체에서 해석 함수임을 함의하는 이유를 설명하라.