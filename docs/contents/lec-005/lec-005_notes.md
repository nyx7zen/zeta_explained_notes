# Proof that Zeta has No Zeros with Re(s)>1

> Euler 곱 공식을 출발점으로 삼아 부등식 연쇄를 통해 $|\zeta(s)| > 0$을 확립함으로써, $\operatorname{Re}(s) > 1$인 영역이 $\zeta(s)$의 첫 번째 영점 없는 영역(zero-free region)임을 증명한다.

- **Source**: [Zeta Explained #005](https://youtu.be/z78NzbhUrWE)
- **Reference**: *The Riemann Zeta-Function* by Aleksandar Ivić (1985)

**Overview**

Riemann 제타 함수를 설명하는 시리즈의 다섯 번째 강의이다. 이전 강의에서 증명한 Euler 곱 공식을 이용하여, $\operatorname{Re}(s) > 1$인 영역이 $\zeta(s)$의 영점 없는 영역임을 증명한다. 증명의 핵심 전략은 $s = \sigma + it$로 쓸 때 $|\zeta(s)|$에 등식과 부등식을 차례로 적용하는 부등식 연쇄를 구성하여, 그 값이 항상 양수임을 보이는 것이다. 구체적으로는 삼각 부등식으로 하한을 잡고, 지수-로그 변환을 통해 무한 곱을 무한 합으로 전환한 뒤, $\log(1+x)$의 Taylor 급수와 교대급수 부등식을 적용하여 최종 결론을 이끌어낸다.

**Contents**

- 강의 도입: Euler 곱 공식 복습 및 증명 목표
- 증명 1단계: Euler 곱과 절댓값의 분리
- 삼각 부등식: 복소평면에서의 기하학적 해석과 하한 도출
- 지수-로그 변환: 무한 곱을 무한 합으로 전환
- $\log(1+x)$의 Taylor 급수 전개와 교대급수 부등식에 의한 하한 추정
- Recap: 확립된 결과와 향후 증명될 영점 분포 전망

---

## 1. 증명의 목표와 전략

이전 강의에서 $\operatorname{Re}(s) > 1$인 복소수 $s$에 대해 Euler 곱 공식이 성립함을 증명하였다.

$$
\begin{equation}
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_p \frac{1}{1 - p^{-s}}
\end{equation}
$$

여기서 무한 곱은 모든 소수 $p$에 걸쳐 취해진다. 이 강의의 목표는 이 공식을 이용하여, $\operatorname{Re}(s) > 1$이면 $\zeta(s) \neq 0$임을 증명하는 것이다.

$s = \sigma + it$ ($\sigma = \operatorname{Re}(s) > 1$, $t = \operatorname{Im}(s)$)로 쓸 때, 증명 전략은 $|\zeta(s)|$에 여러 등식과 부등식을 차례로 적용하여 최종적으로 $|\zeta(s)| > 0$을 보이는 것이다. $|\zeta(s)| > 0$이 성립하면 $\zeta(s) = 0$이 불가능하므로 이것으로 충분하다.

![복소평면에서 영점 없는 영역 Re(s) > 1](images/fig-005-001.png)

**Figure 1.** 복소평면에서 영점 없는 영역 $\operatorname{Re}(s) > 1$

복소평면에서 $\zeta(s)$의 영점 없는 영역 $\operatorname{Re}(s) > 1$(녹색 음영)을 나타낸다. 가로축은 $\operatorname{Re}(s)$, 세로축은 $\operatorname{Im}(s)$이며, 경계선 $\operatorname{Re}(s) = 1$은 점선으로 표시된다. $s = 1$은 $\zeta(s)$의 극점이므로 영역에 포함되지 않는다. 이 강의에서는 녹색 음영 영역 전체에서 $|\zeta(s)| > 0$임을 증명하여 $\zeta(s)$가 이 영역에서 영점을 가지지 않음을 확립한다.

---

## 2. Euler 곱과 절댓값의 분리

$\operatorname{Re}(s) > 1$인 $s = \sigma + it$에 대해 Euler 곱 공식에 절댓값을 취하는 것으로 증명을 시작한다.

복소수 $a, b$에 대해 $|ab| = |a||b|$가 성립한다. 이 성질은 유한 곱에 대해서는 귀납법으로 자명하게 확인되며, 무한 곱에 대해서는 절댓값 함수의 연속성과 Euler 곱의 수렴성을 결합하여 정당화된다. 구체적으로, Euler 곱의 부분 곱에 절댓값을 취한 함수열이 수렴할 때, 연속 함수인 $|\cdot|$을 통한 극한과 절댓값의 순서를 교환할 수 있다.

$$
|\zeta(s)| = \left|\prod_p \frac{1}{1 - p^{-s}}\right| = \prod_p \left|\frac{1}{1 - p^{-s}}\right|
$$

---

## 3. 삼각 부등식의 적용

각 소수 $p$에 대해 분모의 절댓값 $|1 - p^{-s}|$에 삼각 부등식을 적용한다.

복소수에 대한 삼각 부등식은 $|a + b| \leq |a| + |b|$이다. $1 - p^{-s} = 1 + (-p^{-s})$에 적용하면

$$
\begin{equation}
|1 - p^{-s}| \leq |1| + |-p^{-s}| = 1 + |p^{-s}| = 1 + p^{-\sigma}
\end{equation}
$$

를 얻는다. 마지막 등호에서 $|p^{-s}| = p^{-\sigma}$를 이용하였다. 이를 확인하면, $p = e^{\log p}$이므로 $p^{-s} = p^{-\sigma} \cdot e^{-it\log p}$이고, $|e^{-it\log p}| = 1$이 성립하여 $|p^{-s}| = p^{-\sigma}$이다.

부등식 (2)에서 역수를 취하면 부등호 방향이 반전된다. 분모의 상한이 $1 + p^{-\sigma}$이므로 역수의 하한은 $1/(1 + p^{-\sigma})$이다. 이를 모든 소수에 대해 곱하면

$$
\prod_p \left|\frac{1}{1 - p^{-s}}\right| \geq \prod_p \frac{1}{1 + p^{-\sigma}}
$$

를 얻는다.

![삼각 부등식의 기하학적 해석](images/fig-005-002.png)

**Figure 2.** 삼각 부등식의 기하학적 해석

복소평면에서 벡터 $1$, $p^{-s}$, 그리고 그 차 $1 - p^{-s}$를 나타낸 두 경우의 비교이다. 왼쪽 그림에서 $p^{-s}$는 반지름 $p^{-\sigma}$인 원 위의 임의의 점으로, 회전각 $\theta = t\log p$에 따라 위치가 결정된다. $|1 - p^{-s}|$(적색 화살표의 길이)는 두 벡터의 절댓값의 합 $1 + p^{-\sigma}$보다 작거나 같다. 오른쪽 그림은 두 벡터가 같은 방향일 때, 즉 $p^{-s}$가 양의 실수 방향으로 놓인 경우를 나타내며, 이때 등호 $|1 - p^{-s}| = 1 + p^{-\sigma}$가 성립한다. $p^{-s}$의 절댓값은 $p^{-\sigma}$로 일정하며, 허수부의 회전에 무관하게 실수 $\sigma$에만 의존한다.

---

## 4. 지수-로그 변환

$\prod_p 1/(1 + p^{-\sigma})$를 다루기 위해, 모든 양의 실수 $z$에 대해 $z = \exp(\log z)$가 성립함을 이용한다.

$$
\begin{align*}
\prod_p \frac{1}{1 + p^{-\sigma}}
&= \exp\!\left(\log \prod_p \frac{1}{1 + p^{-\sigma}}\right) \\
&= \exp\!\left(\sum_p \log \frac{1}{1 + p^{-\sigma}}\right) \\
&= \exp\!\left(\sum_p -\log(1 + p^{-\sigma})\right)
\end{align*}
$$

두 번째 단계에서 $\log(\prod_p a_p) = \sum_p \log a_p$를 이용하였다. 이 등식을 무한 곱에 적용하기 위해서는 급수 $\sum_p |\log(1/(1+p^{-\sigma}))|$가 수렴함을 먼저 확인하여야 한다. $\log(1+x) \leq x$ ($x \geq 0$)이므로 $|\log(1+p^{-\sigma})| \leq p^{-\sigma}$이고, $\sigma > 1$에서 $\sum_p p^{-\sigma} \leq \zeta(\sigma) < \infty$이므로 절대수렴이 보장된다. 세 번째 단계에서는 $\log(1/a) = -\log(a)$를 이용하였다.

> **주의**: 복소 로그함수는 일반적으로 다치(multi-valued) 함수이므로, 복소수 범위에서 $\log(ab) = \log a + \log b$를 무조건 적용할 수 없다. 이 단계에서 $\sigma$는 실수이고 $1 + p^{-\sigma} > 0$이므로 실수 로그함수를 사용한다.

---

## 5. Taylor 급수 전개와 교대급수 부등식

### $\log(1 + x)$의 Taylor 급수

$\log(1 + x)$의 $x = 0$ 근방에서의 Taylor 급수는 다음과 같다.

$$
\begin{equation}
\log(1 + x) = x - \frac{1}{2}x^2 + \frac{1}{3}x^3 - \frac{1}{4}x^4 + \cdots
\end{equation}
$$

이 급수는 $-1 < x \leq 1$에서 수렴한다. $\sigma > 1$이면 $p \geq 2$이므로 $0 < p^{-\sigma} \leq 2^{-\sigma} < 1$이고, 따라서 $x = p^{-\sigma}$를 대입하는 것이 허용된다. 대입하면

$$
-\log(1 + p^{-\sigma}) = -p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma} + \frac{1}{4}p^{-4\sigma} - \cdots
$$

를 얻는다.

### 교대급수 부등식에 의한 하한

위 급수는 각 항의 절댓값이 단조 감소하는 교대급수이다. 첫 번째 항 $-p^{-\sigma}$를 따로 두고, 나머지 항들을 두 개씩 묶으면

$$
\begin{align*}
&-p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma}
+ \frac{1}{4}p^{-4\sigma} - \frac{1}{5}p^{-5\sigma} + \cdots \\
&= -p^{-\sigma}
+ \left(\frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma}\right)
+ \left(\frac{1}{4}p^{-4\sigma} - \frac{1}{5}p^{-5\sigma}\right) + \cdots
\end{align*}
$$

이다. 일반적인 괄호 항을 분석하면, $\sigma > 1$에서 $p^{-\sigma} < 1$이므로

$$
\frac{1}{2k}p^{-2k\sigma} - \frac{1}{2k+1}p^{-(2k+1)\sigma}
= p^{-2k\sigma}\!\left(\frac{1}{2k} - \frac{p^{-\sigma}}{2k+1}\right) > 0
$$

이 성립한다. 따라서

$$
\begin{equation}
-p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma} + \cdots > -p^{-\sigma}
\end{equation}
$$

가 성립한다.

### exp의 단조 증가성에 의한 결론

$\exp(x)$는 실수 위에서 단조 증가 함수이므로, $a > b$이면 $\exp(a) > \exp(b)$이다. 부등식 (4)의 양변에 소수 전체에 걸친 합산을 취하고 $\exp$를 적용하면

$$
\exp\!\left(\sum_p\!\left(-p^{-\sigma} + \frac{1}{2}p^{-2\sigma}
- \frac{1}{3}p^{-3\sigma} + \cdots\right)\right)
> \exp\!\left(\sum_p -p^{-\sigma}\right)
$$

이다. 소수 집합은 자연수 집합의 부분집합이므로 $\sum_p p^{-\sigma} \leq \zeta(\sigma) < \infty$이고, 따라서 $\sum_p p^{-\sigma}$는 어떤 유한한 양의 실수 $c$로 수렴한다. 모든 실수 $x$에 대해 $e^x > 0$이므로 $\exp\!\left(\sum_p -p^{-\sigma}\right) = e^{-c} > 0$이다.

지금까지의 부등식 연쇄를 종합하면 다음과 같다.

$$
\begin{align*}
|\zeta(s)|
&= \prod_p \left|\frac{1}{1 - p^{-s}}\right| \\
&\geq \prod_p \frac{1}{1 + p^{-\sigma}} \\
&= \exp\!\left(\sum_p -\log(1 + p^{-\sigma})\right) \\
&= \exp\!\left(\sum_p\!\left(-p^{-\sigma} + \frac{1}{2}p^{-2\sigma}
   - \frac{1}{3}p^{-3\sigma} + \cdots\right)\right) \\
&> \exp\!\left(\sum_p -p^{-\sigma}\right) \\
&> 0
\end{align*}
$$

따라서 $\operatorname{Re}(s) > 1$인 모든 $s$에 대해 $|\zeta(s)| > 0$이 성립하며, $\zeta(s) \neq 0$이다. $\square$

---

## 6. 영점의 분포 전망

이 강의에서 $\operatorname{Re}(s) > 1$이 $\zeta(s)$의 첫 번째 영점 없는 영역임을 확립하였다. $\zeta(s)$의 영점(zero)의 전체 분포를 이해하기 위해서는 추가적인 결과들이 필요하며, 이후 강의에서 다음 사항들이 순차적으로 증명된다.

**$\operatorname{Re}(s) > 1$**: 이 강의에서 영점이 없음을 증명하였다.

**$\operatorname{Re}(s) = 1$**: $\zeta(s)$는 직선 $\operatorname{Re}(s) = 1$ 위에서도 영점을 가지지 않는다. 이 결과는 이후 강의에서 증명되며, 그 증명은 이 강의의 방법과 성격이 전혀 다른 방식을 사용한다.

**$\operatorname{Re}(s) \leq 0$**: 음의 짝수 정수 $s = -2, -4, -6, \ldots$에서만 영점이 존재한다. 이것이 자명한 영점(trivial zero)이며, 그 외의 $\operatorname{Re}(s) \leq 0$ 영역에는 영점이 없다.

**임계 띠 $0 < \operatorname{Re}(s) < 1$**: 이 영역에 비자명한 영점(nontrivial zero)이 무한히 많이 존재함이 이후 강의에서 증명된다. 영점의 밀도에 대한 점근 추정, 즉 Riemann–von Mangoldt 방정식도 다룬다.

**Riemann 가설**: 모든 비자명한 영점이 임계선(critical line) $\operatorname{Re}(s) = 1/2$ 위에 놓인다는 주장이다. 이는 아직 증명되지 않은 추측(conjecture)으로, 증명 또는 반례 발견에 100만 달러의 상금이 걸려 있다. 현재까지 수치적으로 확인된 모든 비자명한 영점은 이 추측을 만족한다.

![복소평면에서 ζ(s)의 영점 분포 전망](images/fig-005-003.png)

**Figure 3.** 복소평면에서 $\zeta(s)$의 영점 분포 전망

복소평면에서 $\zeta(s)$의 영점 분포와 영점 없는 영역을 함께 나타낸다. 자명한 영점(녹색)은 음의 짝수 정수 $s = -2, -4, -6, \ldots$에 위치하며, 비자명한 영점(적색)은 임계 띠 $0 < \operatorname{Re}(s) < 1$ 내부에 위치한다. 수치적으로 확인된 처음 몇 개의 비자명한 영점은 모두 임계선 $\operatorname{Re}(s) = 1/2$ 위에 놓여 있으며, 그 허수부 값 $\pm 14.13$, $\pm 21.02$, $\pm 25.01$은 무리수를 반올림한 근삿값이다. $\operatorname{Re}(s) > 1$의 영역(녹색 음영)은 이 강의에서 영점 없음을 증명한 영역이며, $\operatorname{Re}(s) \leq 0$ 중 자명한 영점을 제외한 부분도 영점 없는 영역이다.

---

## 7. Summary

- Euler 곱 공식을 이용하여 $\operatorname{Re}(s) > 1$인 영역에서 $\zeta(s) \neq 0$임을 증명하였다. 증명의 전략은 $|\zeta(s)|$의 하한을 부등식 연쇄를 통해 구성하여 양수임을 보이는 것이다.
- 첫 번째 등식: $|ab| = |a||b|$의 성질과 절댓값 함수의 연속성으로부터 $|\zeta(s)| = \prod_p |1/(1-p^{-s})|$이 성립한다.
- 삼각 부등식 $|1 - p^{-s}| \leq 1 + p^{-\sigma}$로부터 $\prod_p |1/(1-p^{-s})| \geq \prod_p 1/(1+p^{-\sigma})$를 얻는다. 이때 $|p^{-s}| = p^{-\sigma}$임이 핵심이다.
- $z = \exp(\log z)$와 로그의 성질을 적용하여 무한 곱을 $\exp(\sum_p -\log(1+p^{-\sigma}))$로 변환한다. 이 변환은 $\sigma > 1$에서 보장되는 절대수렴이 전제된다.
- $\log(1+x)$의 Taylor 급수를 대입하면 지수 내부의 합은 $\sum_p (-p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \cdots)$가 되며, $\sigma > 1$에서 $p^{-\sigma} < 1$임을 이용한 항 묶기를 통해 이 값이 $\sum_p -p^{-\sigma}$보다 큼을 보인다.
- $\exp$의 단조 증가 성질과 $\sum_p p^{-\sigma} \leq \zeta(\sigma) < \infty$ ($\sigma > 1$)로부터 $|\zeta(s)| > \exp(\sum_p -p^{-\sigma}) > 0$이 성립한다.
- $\operatorname{Re}(s) > 1$이 $\zeta(s)$의 첫 번째 영점 없는 영역이다. 이후 강의에서 $\operatorname{Re}(s) = 1$도 영점 없는 영역임이 증명되며, 임계 띠 $0 < \operatorname{Re}(s) < 1$에는 무한히 많은 비자명한 영점이 존재함이 확립된다.

---

## 8. Review Questions

1. 이 강의에서 $|\zeta(s)| > 0$을 증명하기 위해 Dirichlet 급수 정의 대신 Euler 곱 공식을 출발점으로 선택한 이유를 설명하라.
2. 복소수 $a, b$에 대해 $|ab| = |a||b|$가 성립함을 보여라. 이 성질이 무한 곱으로 확장되기 위해 필요한 조건은 무엇인가?
3. $s = \sigma + it$일 때 $|p^{-s}| = p^{-\sigma}$임을 증명하라. 이때 $|e^{i\theta}| = 1$이 어떻게 사용되는가?
4. 삼각 부등식 $|1 - p^{-s}| \leq 1 + p^{-\sigma}$를 증명하라. 등호가 성립하는 조건은 무엇인가?
5. $\prod_p 1/(1+p^{-\sigma})$를 $\exp(\sum_p -\log(1+p^{-\sigma}))$로 변환하는 과정에서 사용된 로그의 성질 두 가지를 서술하라. 이 변환이 절대수렴을 요구하는 이유를 설명하고, $\sigma > 1$에서 절대수렴이 보장됨을 보여라.
6. $\log(1+x)$의 Taylor 급수를 서술하고, $x = p^{-\sigma}$ ($\sigma > 1$)를 대입할 때 수렴이 보장되는 이유를 설명하라.
7. 교대급수 $-p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma} + \cdots > -p^{-\sigma}$를 항 묶기를 통해 증명하라. 각 괄호 안의 값이 양수임을 보이는 핵심 조건은 무엇인가?
8. $\exp(x)$의 단조 증가 성질이 이 증명에서 어떻게 사용되는가? 이 단계에서 지수 내부의 합이 실수여야 하는 이유를 설명하라.
9. $\sum_p p^{-\sigma} \leq \zeta(\sigma)$가 성립하는 이유를 설명하고, 이로부터 $\exp(\sum_p -p^{-\sigma}) > 0$임을 논증하라.
10. 이 강의에서 확립된 영점 없는 영역과 향후 증명될 결과들을 종합하여 $\zeta(s)$의 영점이 어느 영역에 위치할 수 있는지 설명하라. 자명한 영점, 비자명한 영점, Riemann 가설을 포함하여 서술하라.
