# A Zero-Free Region

> Euler product formula를 이용하여 $\operatorname{Re}(s) > 1$인 영역에서 $\zeta(s)$의 zeros가
> 존재하지 않음을 chain of inequalities로 증명한다.

- **Source**: [Zeta Explained #005](https://youtu.be/VIDEO_ID)
- **Reference**: *The Riemann Zeta-Function* by Aleksandar Ivić (1985)

**Overview**

Riemann zeta function을 설명하는 시리즈의 다섯 번째 강의이다. 이 시리즈는 기초부터
시작하여 고급 주제까지 단계적으로 다루며, 수강자는 calculus와 complex numbers에 대한
기본 지식을 갖추고 있다고 가정한다. Complex analysis의 관련 개념은 강의 중에 필요에
따라 설명한다. 이 강의에서는 이전 강의에서 증명한 Euler product formula를 이용하여
$\operatorname{Re}(s) > 1$인 영역이 zero-free region임을 증명한다. 증명의 핵심 전략은
$|\zeta(s)|$의 하한을 chain of inequalities를 통해 단계적으로 구성하여 이 값이 항상
양수임을 보이는 것이다.

**Contents**

- 강의 도입: Euler product formula 복습 및 zero-free region의 증명 목표
- 증명 1단계: Euler product와 절댓값의 곱 분리
- Triangle inequality: 복소평면에서의 기하학적 해석과 product 부등식 도출
- exp-log 변환: 무한 곱을 무한 합으로 전환
- $\log(1+x)$의 Taylor series 전개와 교대급수 부등식에 의한 하한 추정
- Recap: 확립된 결과와 향후 증명될 zero-free regions 전망

---

## 1. Zero-Free Region의 증명 목표

이전 강의에서 $\operatorname{Re}(s) > 1$인 복소수 $s$에 대해 Euler product formula가
성립함을 증명하였다.

$$
\begin{equation}
\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s} = \prod_p \frac{1}{1 - p^{-s}}
\end{equation}
$$

여기서 무한 곱은 모든 소수 $p$에 대해 취해진다. 이 강의의 목표는 이 공식을 이용하여
다음 명제를 증명하는 것이다.

**Theorem.** $\operatorname{Re}(s) > 1$이면 $\zeta(s) \neq 0$이다.

증명 전략은 $s = \sigma + it$ ($\sigma = \operatorname{Re}(s) > 1$, $t = \operatorname{Im}(s)$)로
쓸 때, $|\zeta(s)|$에 여러 등식과 부등식을 차례로 적용하여 최종적으로 $|\zeta(s)| > 0$을
보이는 것이다. $|\zeta(s)| > 0$이면 $\zeta(s) = 0$이 불가능하므로, 이것으로 충분하다.

![복소평면에서 zero-free region Re(s) > 1](images/fig-005-001.png)

**Figure 1. 복소평면에서 zero-free region $\operatorname{Re}(s) > 1$**

복소평면에서 $\zeta(s)$의 zero-free region $\operatorname{Re}(s) > 1$(녹색 음영)을 나타낸다.
가로축은 $\operatorname{Re}(s)$, 세로축은 $\operatorname{Im}(s)$이며, 경계선 $\operatorname{Re}(s) = 1$은
점선으로 표시된다. $s = 1$은 $\zeta(s)$의 pole이므로 영역에 포함되지 않는다. 이 강의에서는
녹색 음영 영역 전체에서 $|\zeta(s)| > 0$임을 증명하여 $\zeta(s)$가 이 영역에서 zero를 가지지
않음을 확립한다.

---

## 2. Euler Product와 절댓값 분리

$\operatorname{Re}(s) > 1$인 $s = \sigma + it$에 대해 Euler product formula에 절댓값을
취하는 것으로 증명을 시작한다.

복소수 $a, b$에 대해 $|ab| = |a||b|$가 성립한다. 이 성질은 유한 곱에 대해서는 귀납법으로
자명하게 성립하며, 무한 곱에 대해서는 절댓값 함수의 연속성과 Euler product의 수렴성을
결합하여 정당화된다. 구체적으로, Euler product의 부분 곱(partial product)에 절댓값을
취한 함수열이 수렴할 때, 연속 함수인 $|\cdot|$을 통한 극한과 절댓값의 순서를 교환할
수 있다.

$$
\begin{align*}
|\zeta(s)| &= \left|\prod_p \frac{1}{1 - p^{-s}}\right|
          = \prod_p \left|\frac{1}{1 - p^{-s}}\right|
\end{align*}
$$

---

## 3. Triangle Inequality의 적용

각 소수 $p$에 대해 분모의 절댓값 $|1 - p^{-s}|$에 triangle inequality를 적용한다.

복소수에 대한 triangle inequality는 $|a + b| \leq |a| + |b|$이다. 이를
$1 - p^{-s} = 1 + (-p^{-s})$에 적용하면

$$
\begin{equation}
|1 - p^{-s}| \leq |1| + |-p^{-s}| = 1 + p^{-\sigma}
\end{equation}
$$

를 얻는다. 여기서 $|p^{-s}| = p^{-\sigma}$임을 이용하였다. 이를 확인하면,
$p = e^{\log p}$이므로 $p^{-s} = p^{-\sigma} \cdot p^{-it} = p^{-\sigma} \cdot e^{-it\log p}$이고,
$|e^{i\theta}| = 1$이므로 $|p^{-it}| = 1$이 성립하여 $|p^{-s}| = p^{-\sigma}$이다.

역수를 취하면 부등호 방향이 반전된다.

$$
\frac{1}{|1 - p^{-s}|} \geq \frac{1}{1 + p^{-\sigma}}
$$

이를 모든 소수에 대해 곱하면

$$
\prod_p \left|\frac{1}{1 - p^{-s}}\right| \geq \prod_p \frac{1}{1 + p^{-\sigma}}
$$

를 얻는다.

![Triangle inequality의 기하학적 해석](images/fig-005-002.png)

**Figure 2. Triangle inequality의 기하학적 해석**

복소평면에서 벡터 $1$, $p^{-s}$, 그리고 그 차 $1 - p^{-s}$를 나타낸 두 경우의 비교이다.
왼쪽 그림에서 $p^{-s}$는 반지름 $p^{-\sigma}$인 원 위의 임의의 점으로, 허수부의 크기가
회전각 $\theta = t\log p$에 따라 결정된다. $1 - p^{-s}$의 절댓값(적색 화살표의 길이)은
두 벡터의 절댓값의 합 $1 + p^{-\sigma}$보다 작거나 같다. 오른쪽 그림은 두 벡터가 같은
방향일 때, 즉 $p^{-s}$가 양의 실수 방향으로 놓인 경우를 나타내며, 이때 등호
$|1 - p^{-s}| = 1 + p^{-\sigma}$가 성립한다. $p^{-s}$의 절댓값은 $p^{-\sigma}$로 일정하며,
허수부의 회전에 무관하게 실수 $\sigma = \operatorname{Re}(s)$에만 의존한다.

> **주의**: Triangle inequality는 $|1 - p^{-s}|$의 상한을 $1 + p^{-\sigma}$로 제공한다.
> 분모의 상한이 커지면 역수의 하한이 작아지므로, 부등호 방향이 반전된다. 이로써
> $|\zeta(s)|$의 하한 $\prod_p 1/(1+p^{-\sigma})$가 확보된다.

---

## 4. exp-log 변환과 급수 변환

$\prod_p 1/(1 + p^{-\sigma})$를 다루기 위해, 모든 양의 실수 $z$에 대해 $z = \exp(\log z)$가
성립함을 이용한다.

$$
\begin{align*}
\prod_p \frac{1}{1 + p^{-\sigma}}
&= \exp\!\left(\log \prod_p \frac{1}{1 + p^{-\sigma}}\right) \\
&= \exp\!\left(\sum_p \log \frac{1}{1 + p^{-\sigma}}\right) \\
&= \exp\!\left(\sum_p -\log(1 + p^{-\sigma})\right)
\end{align*}
$$

두 번째 단계에서 $\log(\prod_p a_p) = \sum_p \log a_p$를 이용하였다. 이 등식을 무한 곱에
적용하기 위해서는 급수 $\sum_p |\log(1/(1+p^{-\sigma}))|$가 수렴함을 먼저 확인하여야 한다.
$\log(1+x) \leq x$ ($x \geq 0$)이므로 $\log(1+p^{-\sigma}) \leq p^{-\sigma}$이고,
$\sum_p p^{-\sigma} \leq \zeta(\sigma) < \infty$ ($\sigma > 1$)이므로 absolute convergence가
보장된다. 세 번째 단계에서는 $\log(1/a) = -\log(a)$를 이용하였다.

> **주의**: 복소 logarithm은 일반적으로 multi-valued function이므로, 복소수 범위에서
> $\log(ab) = \log a + \log b$를 무조건 적용할 수 없다. 이 단계에서 $\sigma$는 실수이고
> $1 + p^{-\sigma} > 0$이므로 실수 logarithm을 사용한다.

---

## 5. Taylor Series 전개와 교대급수 부등식

### $\log(1 + x)$의 Taylor Series

$\log(1 + x)$의 $x = 0$ 근방에서의 Taylor series는 다음과 같다.

$$
\begin{equation}
\log(1 + x) = x - \frac{1}{2}x^2 + \frac{1}{3}x^3 - \frac{1}{4}x^4 + \cdots
\end{equation}
$$

이 급수는 $-1 < x \leq 1$에서 수렴한다. $\sigma > 1$이면 $p \geq 2$이므로
$0 < p^{-\sigma} \leq 2^{-\sigma} < 1$이고, 따라서 $x = p^{-\sigma}$를 대입하는 것이
허용된다.

$$
-\log(1 + p^{-\sigma}) = -p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma}
+ \frac{1}{4}p^{-4\sigma} - \cdots
$$

### 교대급수 부등식에 의한 하한

위 급수는 각 항의 절댓값이 단조 감소하는 교대급수이다. 첫 번째 항 $-p^{-\sigma}$를 따로
두고, 나머지 항들을 두 개씩 묶으면

$$
\begin{align*}
&-p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma}
+ \frac{1}{4}p^{-4\sigma} - \frac{1}{5}p^{-5\sigma} + \cdots \\
&= -p^{-\sigma}
+ \left(\frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma}\right)
+ \left(\frac{1}{4}p^{-4\sigma} - \frac{1}{5}p^{-5\sigma}\right) + \cdots
\end{align*}
$$

이다. 각 괄호 안의 일반항을 분석한다.

$$
\frac{1}{2k}p^{-2k\sigma} - \frac{1}{2k+1}p^{-(2k+1)\sigma}
= p^{-2k\sigma}\!\left(\frac{1}{2k} - \frac{p^{-\sigma}}{2k+1}\right)
$$

$p \geq 2$이고 $\sigma > 1$이면 $p^{-\sigma} < 1$이므로,
$\frac{p^{-\sigma}}{2k+1} < \frac{1}{2k+1} < \frac{1}{2k}$가 성립한다. 따라서
각 괄호 안의 값은 양수이고,

$$
\begin{equation}
-p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma} + \cdots > -p^{-\sigma}
\end{equation}
$$

이 성립한다.

### 단조성에 의한 최종 결론

$\exp(x)$는 실수 위에서 단조 증가 함수이므로, $a > b$이면 $\exp(a) > \exp(b)$이다.
위 부등식에 $\exp$를 취하면

$$
\exp\!\left(\sum_p\!\left(-p^{-\sigma} + \frac{1}{2}p^{-2\sigma}
- \frac{1}{3}p^{-3\sigma} + \cdots\right)\right)
> \exp\!\left(\sum_p -p^{-\sigma}\right)
$$

이다. 소수 집합은 자연수 집합의 부분집합이므로 $\sum_p p^{-\sigma} \leq \zeta(\sigma) < \infty$
이고, 따라서 $\sum_p p^{-\sigma}$는 어떤 유한한 실수 $c > 0$으로 수렴한다. 모든 실수 $x$에
대해 $e^x > 0$이므로 $\exp\!\left(\sum_p -p^{-\sigma}\right) = e^{-c} > 0$이다.

지금까지의 chain of inequalities를 종합하면 다음과 같다.

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

## 6. Zeros의 분포 전망

이 강의에서 $\operatorname{Re}(s) > 1$이 $\zeta(s)$의 첫 번째 zero-free region임을 확립하였다.
$\zeta(s)$의 zeros의 전체 분포를 이해하기 위해서는 추가적인 결과들이 필요하며, 이후 강의에서
다음 사항들이 순차적으로 증명된다.

**$\operatorname{Re}(s) > 1$**: 이 강의에서 zero-free임을 증명하였다.

**$\operatorname{Re}(s) = 1$**: $\zeta(s)$는 직선 $\operatorname{Re}(s) = 1$ 위에서도 zero를
가지지 않는다. 이 결과는 이후 강의에서 증명되며, 그 증명은 이 강의의 방법과 성격이 전혀
다른 방식을 사용한다.

**$\operatorname{Re}(s) \leq 0$**: 음의 짝수 정수 $s = -2, -4, -6, \ldots$에서만 zeros가
존재한다. 이것이 trivial zeros이며, 그 외의 $\operatorname{Re}(s) \leq 0$ 영역에는 zeros가
없다.

**Critical strip $0 < \operatorname{Re}(s) < 1$**: 이 영역에 nontrivial zeros가 무한히 많이
존재함이 이후 강의에서 증명된다. Zeros의 밀도에 대한 점근 추정, 즉 Riemann–von Mangoldt
equation도 다룬다.

**Riemann Hypothesis**: 모든 nontrivial zeros가 critical line $\operatorname{Re}(s) = 1/2$
위에 놓인다는 주장이다. 이는 아직 증명되지 않은 conjecture로, 증명 또는 반례 발견에
$1,000,000달러의 상금이 걸려 있다. 현재까지 수치적으로 확인된 모든 nontrivial zeros는
이 conjecture를 만족한다.

![복소평면에서 ζ(s)의 zeros 분포 전망](images/fig-005-003.png)

**Figure 3. 복소평면에서 $\zeta(s)$의 zeros 분포 전망**

복소평면에서 $\zeta(s)$의 zeros 분포와 zero-free regions를 함께 나타낸다. Trivial zeros(녹색)는
음의 짝수 정수 $s = -2, -4, -6, \ldots$에 위치한다. Nontrivial zeros(적색)는 critical strip
$0 < \operatorname{Re}(s) < 1$ 내부에 위치하며, 수치적으로 확인된 처음 몇 개는 모두 critical
line $\operatorname{Re}(s) = 1/2$ 위에 있다. $\operatorname{Re}(s) = 1$의 오른쪽(녹색 음영)은
이 강의에서 zero-free임을 증명한 영역이다. $\operatorname{Re}(s) \leq 0$ 중 trivial zeros를
제외한 부분도 zero-free이며, 이 결과는 이후 강의에서 functional equation을 통해 증명된다.
Riemann hypothesis는 모든 nontrivial zeros가 critical line 위에만 있다는 미증명 conjecture이다.

---

## 7. Summary

- Euler product formula를 이용하여 $\operatorname{Re}(s) > 1$인 영역에서 $\zeta(s) \neq 0$임을
  증명하였다. 증명의 전략은 $|\zeta(s)|$의 하한을 chain of inequalities를 통해 구성하여
  양수임을 보이는 것이다.
- 첫 번째 등식: $|ab| = |a||b|$의 성질과 절댓값 함수의 연속성으로부터
  $|\zeta(s)| = \prod_p |1/(1-p^{-s})|$이 성립한다.
- Triangle inequality $|1 - p^{-s}| \leq 1 + p^{-\sigma}$로부터
  $\prod_p |1/(1-p^{-s})| \geq \prod_p 1/(1+p^{-\sigma})$를 얻는다. 이때
  $|p^{-s}| = p^{-\sigma}$임이 핵심이다.
- $z = \exp(\log z)$와 로그의 성질을 적용하여 무한 곱을 $\exp(\sum_p -\log(1+p^{-\sigma}))$로
  변환한다. 이 변환은 absolute convergence가 보장될 때 유효하다.
- $\log(1+x)$의 Taylor series를 대입하면 지수 내부의 합은
  $\sum_p (-p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \cdots)$가 되며, 항 묶기를 통해
  이 값이 $\sum_p -p^{-\sigma}$보다 큼을 보인다. 각 괄호 안이 양수인 이유는
  $p^{-\sigma} < 1$이기 때문이다.
- $\exp$의 단조 증가 성질과 $\sum_p p^{-\sigma} \leq \zeta(\sigma) < \infty$ ($\sigma > 1$)로부터
  $|\zeta(s)| > \exp(\sum_p -p^{-\sigma}) = e^{-c} > 0$이 성립한다.
- $\operatorname{Re}(s) > 1$이 $\zeta(s)$의 첫 번째 zero-free region이다. 이후 강의에서
  $\operatorname{Re}(s) = 1$도 zero-free임이 증명되며, critical strip $0 < \operatorname{Re}(s) < 1$에는
  무한히 많은 nontrivial zeros가 존재함이 확립된다.

---

## 8. Review Questions

1. 이 강의에서 $|\zeta(s)| > 0$을 증명하기 위해 Dirichlet series 정의 대신 Euler product
   formula를 출발점으로 선택한 이유를 설명하라.
2. 복소수 $a, b$에 대해 $|ab| = |a||b|$가 성립함을 보여라. 이 성질이 무한 곱으로 확장되기
   위해 필요한 조건은 무엇인가?
3. $s = \sigma + it$일 때 $|p^{-s}| = p^{-\sigma}$임을 증명하라. 이때 $|e^{i\theta}| = 1$이
   어떻게 사용되는가?
4. Triangle inequality $|1 - p^{-s}| \leq 1 + p^{-\sigma}$를 증명하라. 등호가 성립하는 조건은
   무엇인가?
5. $\prod_p 1/(1+p^{-\sigma})$를 $\exp(\sum_p -\log(1+p^{-\sigma}))$로 변환하는 과정에서 사용된
   로그의 성질 두 가지를 서술하라. 이 변환이 absolute convergence를 요구하는 이유를 설명하고,
   $\sigma > 1$에서 absolute convergence가 보장됨을 보여라.
6. $\log(1+x)$의 Taylor series를 서술하고, $x = p^{-\sigma}$ ($\sigma > 1$)를 대입할 때
   수렴이 보장되는 이유를 설명하라.
7. 교대급수 $-p^{-\sigma} + \frac{1}{2}p^{-2\sigma} - \frac{1}{3}p^{-3\sigma} + \cdots > -p^{-\sigma}$를
   항 묶기를 통해 증명하라. 각 괄호 안의 값이 양수임을 보이는 핵심 부등식은 무엇인가?
8. $\exp(x)$의 단조 증가 성질이 이 증명에서 어떻게 사용되는가? 이 단계에서 지수 내부의 합이
   실수여야 하는 이유를 설명하라.
9. $\sum_p p^{-\sigma} \leq \zeta(\sigma)$가 성립하는 이유를 설명하고, 이로부터
   $\exp(\sum_p -p^{-\sigma}) > 0$임을 논증하라.
10. 이 강의에서 확립된 zero-free region과 향후 증명될 결과들을 종합하여 $\zeta(s)$의 zeros가
    어느 영역에 위치할 수 있는지 설명하라. Trivial zeros, nontrivial zeros, Riemann hypothesis를
    포함하여 서술하라.
