## Rewrite Linear Regression in Python

try pseudocode with Linear Regression:

```pseudocode
Given:
	eta - learning rate
	data - a set of data points % e.g. [(x,y),(a,b)...]
Return:
	theta0 - a parameter of model (h = theta1 * x + theta0)
	theta1 - a parameter of model (h = theta1 * x + theta0)
	loss - result of loss function under theta0 and theta1

theta0 = 0
theta1 = 0
% set default theta values
x_list = a set of x axis value from data
y_list = a set of y axis value from data
sample_numbers = the number of all samples

theta0 = theta0 - eta * (sum of all points in (theta1*x + theta0 + y))
theta1 = theta1 - eta * (sum of all points in (theta1*x + theta0 + y)*x)

```

try 不出来，直接写代码吧

---

代码中定义了以下几个函数：

#### seperate_xy()

将数据点集拆分为x轴与y轴的列表

#### step_gradient()

计算每一步的梯度值

#### evaluate_lost()

计算每一步损失函数的值

#### train()

输入原数据集，learning_rate, 最大迭代次数，损失函数下限

将输出每一步的各θ与损失函数的值，超过最大迭代次数或损失函数到达下限都将结束循环

#### gen_test_data_set()

测试数据集

#### run()

结合以上函数，进行处理

## Rewrite Logistic Regression in Python

逻辑回归和线性回归其实差不多，只是回归函数不同

写好了，和上面线性回归差不过，稍微优化了一下代码

遇到了一个问题，逻辑回归的lost好像降不到很低的样子，前一个线性回归能降到0.001，逻辑回归就只能降到0.46，我想应该是数据点的问题吧

## Mathematics

A person is swimming across several rivers.

Speeds of those rivers are different: [v1, v2, v3, v4,...,vn], consider vertical speed only.

Width of rivers is known as [S1, S2, S3, S4,...,Sn]

The person's speed is v, the swimming angle of velocity to horizontal line is [a1, a2, a3, a4,...,an]

The person must pass all those rivers, the total time for swimming is T

##### Task:

Find out an equation to determine by choosing what angles the person can get maximum distance in vertical direction (maximize dh by determining [a1, a2, a3,...,an])



$$
\begin{gather}
\displaystyle\sum\limits_{i=1}^n \frac {v * cos(a_i)} {S_i} = T \tag{1}\\\\
h = \displaystyle\sum\limits_{i=1}^n \frac {(v_i + v*sin(a_i))* S_i} {v * cos(a_i)} \tag{2}
\end{gather}
$$

$$
\begin{gather}

\end{gather}
$$

已知1式求$h_{max}$


