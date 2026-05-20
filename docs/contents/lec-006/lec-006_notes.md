# The Logarithmic Derivative and the Von Mangoldt Function

> Euler 곱 공식과 연쇄 법칙을 결합하여 $\operatorname{Re}(s) > 1$에서 $\zeta(s)$의 로그 미분을 계산하고, 소수 거듭제곱에 대한 합산 재인덱싱을 통해 그 결과가 von Mangoldt 함수 $\Lambda(n)$을 계수로 갖는 Dirichlet 급수임을 확립한다.

- **Source**: [Zeta Explained #006](https://youtu.be/I0P7DfA17x0)
- **Reference**: *The Riemann Zeta-Function* by Aleksandar Ivić (1985)

**Overview**

Riemann 제타 함수를 설명하는 시리즈의 여섯 번째 강의이다. 이 강의에서는 $\zeta(s)$의 로그 미분(logarithmic derivative)과 정수론에서 등장하는 von Mangoldt 함수를 다룬다. 앞선 강의들에서 확립한 두 결과, 즉 $\operatorname{Re}(s) > 1$에서 $\zeta(s) \neq 0$이라는 사실(5강)과 $\zeta(s)$가 해석 함수라는 사실(2강)을 결합하여, Euler 곱 공식에 로그를 취하고 $s$에 대해 미분함으로써 로그 미분 $\zeta'(s)/\zeta(s)$를 구한다. 증명에는 연쇄 법칙, 등비급수 전개, 합산 재인덱싱 논리가 순차적으로 활용된다. 최종 결과로 도출되는 von Mangoldt 함수는 이후 $\operatorname{Re}(s) = 1$ 위에서 $\zeta(s)$가 영점을 가지지 않음을 증명하는 데 핵심적으로 사용된다.

**Contents**

- 강의 도입: 선수 결과 복습 및 로그 미분의 목표
- 연쇄 법칙과 로그 미분의 정의
- $\log \zeta(s)$에 Euler 곱 공식 적용
- $s$에 대한 미분과 균등 수렴 조건
- 연쇄 법칙으로 각 항 계산
- 등비급수를 이용한 전개
- 합산 재인덱싱의 설명: 두 가지 예시
- 소수 거듭제곱에 대한 재인덱싱과 von Mangoldt 함수
- Recap 및 향후 활용

---

## 1. 강의 목표와 선수 결과

이 강의의 목표는 $\operatorname{Re}(s) > 1$에서 $\zeta(s)$의 로그 미분에 대한 명시적 공식을 유도하는 것이다. 도출될 결과는 von Mangoldt 함수(von Mangoldt function) $\Lambda(n)$을 이용하여 다음과 같이 표현된다.

$$
\frac{\zeta'(s)}{\zeta(s)} = -\sum_{n=1}^{\infty} \Lambda(n)\, n^{-s}
$$

여기서 $\Lambda(n)$은 정수론에서 등장하는 함수로, 이 강의에서 자연스럽게 도출된다. 이 공식의 유도에는 앞선 강의들에서 확립한 두 결과가 핵심적으로 사용된다.

- **2강**: $\operatorname{Re}(s) > 1$에서 $\zeta(s)$는 해석 함수이다.
- **5강**: $\operatorname{Re}(s) > 1$에서 $\zeta(s) \neq 0$이다.

이 두 조건 덕분에 $\log(\zeta(s))$를 이 영역에서 안전하게 정의할 수 있다. 로그함수는 $0$에서 특이점을 가지므로, $\zeta(s) \neq 0$이라는 조건이 필수적이다.

---

## 2. 연쇄 법칙과 로그 미분

### 연쇄 법칙

복소 미분에서 연쇄 법칙(chain rule)은 실수 미분과 동일한 형태로 성립한다. 해석 함수 $f$, $g$에 대해

$$
\frac{d}{dz} g(f(z)) = f'(z)\, g'(f(z))
$$

이다.

### 로그 미분의 정의

$g = \log$로 놓으면 $g'(w) = 1/w$이므로, 어떤 영역에서 해석적이고 영점을 가지지 않는 함수 $f(z)$에 대해

$$
\begin{equation}
\frac{d}{dz} \log(f(z)) = \frac{f'(z)}{f(z)}
\end{equation}
$$

가 성립한다. 이 양 $f'(z)/f(z)$을 $f$의 **로그 미분**이라 한다.

> **주의**: 복소 로그함수는 $z = 0$에서 특이점을 가지며 일반적으로 다치(multi-valued) 함수이다. 따라서 $\log(f(z))$를 정의하려면 $f(z) \neq 0$이 반드시 요구된다. 5강에서 $\operatorname{Re}(s) > 1$에서 $\zeta(s) \neq 0$임을 증명하였으므로, 이 영역에서 $\log(\zeta(s))$를 안전하게 다룰 수 있다.

$f = \zeta$를 대입하면 $\frac{d}{ds}\log(\zeta(s)) = \frac{\zeta'(s)}{\zeta(s)}$이다. $\zeta(s)$의 무한급수 표현 $\sum_{n=1}^{\infty} n^{-s}$에 대해서는 로그를 직접 다루기 어렵다. 그러나 Euler 곱 공식은 $\zeta(s)$를 무한 곱으로 표현하므로, 무한 곱의 로그를 각 항의 로그들의 합으로 변환할 수 있다.

---

## 3. $\log \zeta(s)$의 전개

$\operatorname{Re}(s) > 1$에서 Euler 곱 공식에 로그를 취한다.

$$
\begin{align*}
\log(\zeta(s))
&= \log\!\left(\prod_p \frac{1}{1 - p^{-s}}\right)
\qquad \text{(Euler 곱 공식, $\zeta(s) \neq 0$)} \\
&= \sum_p \log\!\left(\frac{1}{1 - p^{-s}}\right)
\qquad \text{(로그의 성질, 절대수렴 조건)} \\
&= -\sum_p \log(1 - p^{-s})
\qquad \text{($\log(1/a) = -\log(a)$)}
\end{align*}
$$

두 번째 단계에서 무한 곱의 로그를 로그들의 무한 합으로 변환하였다. 유한 곱에서 $\log(\prod a_k) = \sum \log a_k$는 귀납법으로 자명하다. 무한 곱에 이를 적용하기 위해서는 절대수렴이 보장되어야 하며, $\sigma > 1$에서 $\sum_p |\log(1/(1-p^{-\sigma}))| \leq \sum_p p^{-\sigma} \leq \zeta(\sigma) < \infty$이므로 이 조건이 충족된다.

---

## 4. $s$에 대한 미분

$\log(\zeta(s)) = -\sum_p \log(1 - p^{-s})$의 양변을 $s$에 대해 미분한다.

$$
\frac{\zeta'(s)}{\zeta(s)} = -\frac{d}{ds} \sum_p \log(1 - p^{-s})
$$

무한 합에서 미분과 합산의 순서를 교환하기 위해서는 균등 수렴이 필요하다. $a > 0$을 고정하면 $\operatorname{Re}(s) \geq 1 + a$ 영역에서 균등 수렴이 성립하고(3강의 논리와 동일), $a > 0$이 임의로 작을 수 있으므로 $\operatorname{Re}(s) > 1$ 전체에서 다음이 허용된다.

$$
\frac{\zeta'(s)}{\zeta(s)} = -\sum_p \frac{d}{ds} \log(1 - p^{-s})
$$

각 항에 연쇄 법칙을 적용한다. $\frac{d}{ds}(1 - p^{-s}) = (\log p)\, p^{-s}$이므로

$$
\frac{d}{ds} \log(1 - p^{-s}) = \frac{(\log p)\, p^{-s}}{1 - p^{-s}}
$$

이다. 따라서

$$
\begin{equation}
\frac{\zeta'(s)}{\zeta(s)} = -\sum_p (\log p)\, \frac{p^{-s}}{1 - p^{-s}}
\end{equation}
$$

가 성립한다.

---

## 5. 등비급수를 이용한 전개

$\operatorname{Re}(s) > 1$이면 $p \geq 2$이므로 $|p^{-s}| = p^{-\sigma} < 1$이다. 등비급수 공식

$$
\frac{x}{1 - x} = x + x^2 + x^3 + \cdots \quad (|x| < 1)
$$

을 $x = p^{-s}$에 적용하면 $\frac{p^{-s}}{1 - p^{-s}} = \sum_{n=1}^{\infty} p^{-ns}$이다. 이를 (2)에 대입하면

$$
\frac{\zeta'(s)}{\zeta(s)} = -\sum_p (\log p) \sum_{n=1}^{\infty} p^{-ns}
$$

를 얻는다. 이 이중 합산에서 $p^{-ns} = (p^n)^{-s}$임에 주목한다. 변수 $p^n$은 소수 $p$의 $n$제곱인 소수 거듭제곱(prime power)이며, 이를 이용한 합산 재인덱싱이 다음 단계이다.

---

## 6. 합산 재인덱싱의 예시

이중 합산에서 단일 합산으로의 재인덱싱 원리를 이해하기 위해, 먼저 단순한 두 예시를 살펴본다.

### 예시 1: 짝수에 걸친 합산

다음의 합산을 고려한다.

$$
\sum_{n=1}^{\infty} \frac{1}{(2n)^2}
= \frac{1}{2^2} + \frac{1}{4^2} + \frac{1}{6^2} + \cdots
$$

이 합산에는 짝수의 제곱만 등장한다. 지시 함수(indicator function)를 도입하면

$$
\sum_{n=1}^{\infty} \frac{1}{(2n)^2}
= \sum_{m=1}^{\infty} \frac{\text{IsEven}(m)}{m^2}
= \frac{0}{1^2} + \frac{1}{2^2} + \frac{0}{3^2} + \frac{1}{4^2} + \cdots
$$

으로 쓸 수 있다. 여기서 $\text{IsEven}(m) = \begin{cases} 1 & \text{$m$이 짝수인 경우} \\ 0 & \text{그 외} \end{cases}$이다. 합산 방식은 변하지만 합산의 값은 동일하다.

### 예시 2: 분자에 로그가 있는 경우

$$
\sum_{n=1}^{\infty} \frac{\log(2n)}{(2n)^2}
= \frac{\log 2}{2^2} + \frac{\log 4}{4^2} + \frac{\log 6}{6^2} + \cdots
= \sum_{m=1}^{\infty} \frac{\text{LogIfEven}(m)}{m^2}
$$

여기서 $\text{LogIfEven}(m) = \begin{cases} \log m & \text{$m$이 짝수인 경우} \\ 0 & \text{그 외} \end{cases}$이다. 전개하면 $0/1^2 + \log(2)/2^2 + 0/3^2 + \log(4)/4^2 + \cdots$가 된다.

이 두 예시에서 핵심 원리는 동일하다. 특정 성질을 가진 $n$에 대해서만 정의된 합산을, 모든 자연수 $m$에 걸치되 그 성질을 가지지 않는 $m$에 대해 기여가 $0$인 함수를 이용하여 재표현할 수 있다.

---

## 7. von Mangoldt 함수와 최종 결과

위의 예시에서 짝수가 맡았던 역할이, 이 문제에서는 소수 거듭제곱으로 대체된다. 이중 합산 $-\sum_p (\log p) \sum_{n=1}^{\infty} p^{-ns}$에서 $p^{-ns} = (p^n)^{-s}$이므로, $m = p^n$으로 치환하면 자연수 $m$이 소수 거듭제곱인 경우에만 $(\log p)\, m^{-s}$가 기여한다. 이를 단일 계수 함수로 정의한 것이 von Mangoldt 함수이다.

$$
\begin{equation}
\Lambda(n) =
\begin{cases}
\log p & \text{$n = p^k$인 경우 ($p$ 소수, $k \geq 1$)} \\
0 & \text{그 외}
\end{cases}
\end{equation}
$$

처음 몇 개의 값을 확인하면 다음과 같다.

| $n$ | $\Lambda(n)$ | 이유 |
|-----|-------------|------|
| 1 | 0 | $1$은 소수 거듭제곱이 아님 |
| 2 | $\log 2$ | $2 = 2^1$ |
| 3 | $\log 3$ | $3 = 3^1$ |
| 4 | $\log 2$ | $4 = 2^2$ |
| 5 | $\log 5$ | $5 = 5^1$ |
| 6 | 0 | $6 = 2 \times 3$, 소수 거듭제곱이 아님 |
| 7 | $\log 7$ | $7 = 7^1$ |
| 8 | $\log 2$ | $8 = 2^3$ |
| 9 | $\log 3$ | $9 = 3^2$ |

절대수렴이 보장되면 이중 합산의 재인덱싱이 허용된다. 이에 의해

$$
\begin{equation}
\frac{\zeta'(s)}{\zeta(s)} = -\sum_{n=1}^{\infty} \Lambda(n)\, n^{-s}
\end{equation}
$$

가 성립한다. 우변은 von Mangoldt 함수 $\Lambda(n)$을 계수로 갖는 Dirichlet 급수이다.

---

## 8. Recap 및 향후 활용

이 강의에서 $\operatorname{Re}(s) > 1$에서 $\zeta(s)$의 로그 미분에 대한 명시적 공식을 확립하였다. 공식 (4)는 $\zeta'(s)/\zeta(s)$를 von Mangoldt 함수 $\Lambda(n)$을 계수로 갖는 Dirichlet 급수로 표현하며, 이 결과의 향후 활용은 다음과 같다.

**$\operatorname{Re}(s) = 1$ 위에서의 영점 없음**: 이 공식은 이후 강의에서 $\operatorname{Re}(s) = 1$인 직선 위에서 $\zeta(s)$가 영점을 가지지 않음을 증명하는 데 핵심적으로 사용된다.

**해석적 연속**: 현재의 모든 결과는 $\operatorname{Re}(s) > 1$이라는 조건 아래서만 성립한다. 이 영역 왼쪽에서 $\zeta(s)$가 어떤 값을 갖는지 분석하려면 해석적 연속(analytic continuation)이 필요하다. 다음 강의에서 이 주제를 다룬다.

![복소평면에서 로그 미분 공식이 성립하는 영역과 향후 결과](images/fig-006-001.png)

**Figure 1.** 복소평면에서 로그 미분 공식이 성립하는 영역 $\operatorname{Re}(s) > 1$

복소평면에서 로그 미분 공식 $\zeta'(s)/\zeta(s) = -\sum_{n=1}^{\infty} \Lambda(n) n^{-s}$이 성립하는 영역 $\operatorname{Re}(s) > 1$(녹색 음영)을 나타낸다. 가로축은 $\operatorname{Re}(s)$, 세로축은 $\operatorname{Im}(s)$이며, $s = 1$은 $\zeta(s)$의 극점으로 열린 원으로 표시된다. 이 강의에서 유도된 로그 미분 공식은 이후 $\operatorname{Re}(s) = 1$인 직선 위에서 영점이 없음을 증명하는 데 활용된다. 다음 강의에서는 해석적 연속을 통해 $\zeta(s)$를 이 영역 왼쪽으로 확장한다.

---

## 9. Summary

- $\operatorname{Re}(s) > 1$에서 $\zeta(s) \neq 0$(5강)이고 $\zeta(s)$가 해석 함수(2강)임을 이용하여, 이 영역에서 $\log(\zeta(s))$를 안전하게 정의할 수 있다.
- $f(z)$가 해석 함수이고 $f(z) \neq 0$이면, 연쇄 법칙에 의해 $\frac{d}{dz}\log(f(z)) = f'(z)/f(z)$가 성립한다. 이 양을 $f$의 로그 미분이라 한다.
- Euler 곱 공식에 로그를 취하면 $\log(\zeta(s)) = -\sum_p \log(1 - p^{-s})$를 얻는다. 이 변환에는 절대수렴이 전제된다.
- $s$에 대해 미분하면 $\zeta'(s)/\zeta(s) = -\sum_p (\log p)\, p^{-s}/(1-p^{-s})$이다. 미분과 합산의 교환에는 균등 수렴이 필요하며, $\operatorname{Re}(s) \geq 1 + a$ ($a > 0$) 영역에서 성립한다.
- 등비급수 $p^{-s}/(1-p^{-s}) = \sum_{n=1}^{\infty} p^{-ns}$를 적용하면 이중 합산 $-\sum_p (\log p) \sum_{n=1}^{\infty} p^{-ns}$가 도출된다.
- $p^{-ns} = (p^n)^{-s}$임을 이용하여 $m = p^n$으로 재인덱싱하면, von Mangoldt 함수 $\Lambda(n)$을 계수로 갖는 단일 합산 $-\sum_{n=1}^{\infty} \Lambda(n) n^{-s}$가 얻어진다.
- von Mangoldt 함수 $\Lambda(n)$은 $n = p^k$ ($p$ 소수, $k \geq 1$)인 경우 $\log p$를, 그 외에는 $0$을 취한다. 이 함수는 이중 합산이 소수 거듭제곱에서만 기여한다는 사실을 하나의 계수 함수로 압축한 것이다.
- 이 공식은 이후 강의에서 $\operatorname{Re}(s) = 1$ 위에서의 영점 없음을 증명하는 데 핵심적으로 활용된다.

---

## 10. Review Questions

1. 이 강의에서 로그 미분을 계산하기 위해 Euler 곱 공식이 필수적으로 사용되는 이유를 설명하라. $\zeta(s)$의 급수 표현 $\sum_{n=1}^{\infty} n^{-s}$에 대해 직접 로그를 취하는 방법이 왜 적합하지 않은가?
2. $f(z)$가 어떤 영역에서 해석적이고 $f(z) \neq 0$이면 $\frac{d}{dz}\log(f(z)) = f'(z)/f(z)$가 성립함을 연쇄 법칙으로부터 유도하라.
3. $\operatorname{Re}(s) > 1$에서 $\log(\zeta(s)) = -\sum_p \log(1 - p^{-s})$가 성립함을 단계적으로 서술하라. 이 변환에서 절대수렴이 필요한 이유를 설명하라.
4. 무한 합산에서 미분과 합산의 순서를 교환하기 위해 균등 수렴이 필요한 이유를 설명하라. $\operatorname{Re}(s) > 1$ 전체가 아닌 $\operatorname{Re}(s) \geq 1 + a$에서 균등 수렴을 먼저 확립하는 이유는 무엇인가?
5. $\frac{d}{ds}\log(1 - p^{-s}) = \frac{(\log p)\,p^{-s}}{1 - p^{-s}}$를 연쇄 법칙을 이용하여 증명하라.
6. 등비급수 $x/(1-x) = \sum_{n=1}^{\infty} x^n$ ($|x| < 1$)이 이 증명에서 어떻게 활용되는가? $\operatorname{Re}(s) > 1$에서 $x = p^{-s}$를 대입할 때 수렴이 보장되는 이유를 설명하라.
7. $-\sum_p (\log p) \sum_{n=1}^{\infty} p^{-ns}$를 $-\sum_{m=1}^{\infty} \Lambda(m) m^{-s}$로 재인덱싱하는 과정을 서술하라. 재인덱싱이 허용되기 위해 필요한 조건은 무엇인가?
8. von Mangoldt 함수 $\Lambda(n)$을 정의하고, $n = 1, 2, 3, 4, 5, 6, 7, 8, 9, 12$에 대한 함수값을 구하라.
9. 예시 1의 $\sum_{n=1}^{\infty} \frac{1}{(2n)^2} = \sum_{m=1}^{\infty} \frac{\text{IsEven}(m)}{m^2}$이 성립하는 이유를 설명하라. 이 예시가 von Mangoldt 함수를 이용한 재인덱싱과 어떻게 유사한가?
10. 이 강의에서 유도된 로그 미분 공식의 향후 활용을 서술하라. 지금까지 확립된 결과들을 종합하여 현재 알려진 $\zeta(s)$의 영점 없는 영역을 설명하고, 다음 강의의 주제가 필요한 이유를 논하라.
