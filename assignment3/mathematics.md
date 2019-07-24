已知每条河宽度 $S_i$

每条河流速 $V_i$

人的固定游泳速度 $v$

游泳的总时间 $T$

求沿河流方向最大距离时，各河流游泳角度$a_i$

-------

设有沿河方向游泳距离函数$h(a_1, a_2,...,a_n)$

则需求：
$$
\begin{gather}
min h(a_1, a_2, a_3,...,a_n)\\
s.t.   \displaystyle\sum\limits_{i=1}^n \frac {S_i}{v\cos{a_i}} = T 
\end{gather}
$$
以下将$h(a_1, a_2,...,a_n)$略写为$h(a_i)$
$$
\begin{gather}
h(a_i) = \displaystyle\sum\limits_{i=1}^n (V_i + v\sin{a_i})\frac{S_i}{v\cos{a_i}}
\end{gather}
$$
Lagrange Multiplier:
$$
\begin{gather}
F(a_1, a_2,...,a_n, \lambda) = \sum\limits_{i=1}^n \frac{(V_i + v\sin{a_i})S_i}{v\cos{a_i}} + \lambda(\sum\limits_{i=1}^n \frac{S_i}{v\cos{a_i}}-T)
\end{gather}
$$
对上式各变量求偏导有：
$$
\begin{gather}
\frac{\partial F}{\partial a_i} = (\frac{((V_i+ \lambda ) \sin {a_i}+v)S_i}{v \cos ^2{a_i}})\tag 1\\\\
\frac{\partial F}{\partial \lambda} = (\sum\limits_{i=1}^n \frac{S_i}{v\cos{a_i}}) - T \tag {n+1}
\end{gather}
$$
最大值时，各偏导数为0，且依照常识，取值范围有：
$$
\begin{gather}
S_i > 0\\
a_i \in (0, \frac{\pi}{2})\\
v>0
\end{gather}
$$
因此有：
$$
\begin{gather}
\frac{S_i}{v\cos^2{a_i}}>0
\end{gather}
$$
所以：
$$
\begin{gather}
(V_i+\lambda)\sin{a_i} + v = 0
\end{gather}
$$
方程组：
$$
\begin{gather}
(V_1+\lambda)\sin{a_1} + v = 0 \tag 1\\
(V_2+\lambda)\sin{a_2} + v = 0 \tag 2\\
...\\
(V_n+\lambda)\sin{a_n} + v = 0 \tag n\\
(\sum\limits_{i=1}^n \frac{S_i}{v\cos{a_i}}) = T \tag {n+1}
\end{gather}
$$
根据以上前n个方程组解得各$a_{i}$：
$$
\begin{gather}
a_i = \arcsin{\frac{-v}{V_i + \lambda}}
\end{gather}
$$
带入(n+1)式可得$\lambda$值，进而可求得每个$a_i$的值



下附$\frac{\partial F}{\partial a_i}$求解过程：



![98849cde533238f22ba99ac6f7d7cfd](C:\Users\jetech67\AppData\Local\Temp\WeChat Files\98849cde533238f22ba99ac6f7d7cfd.jpg)