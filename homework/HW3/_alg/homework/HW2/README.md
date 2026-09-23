# Homework 2: 遞迴方程式求解與時間複雜度分析 (Recurrence Relations & Big-O)

## 👨‍🎓 Student Information

- **Name**: 范權榮
- **University**: 國立金門大學 (NQU)
- **Department**: 資訊工程學系 (CSIE)
- **Student ID**: 111210557

---

## 📌 Problem Overview

本作業針對演算法課程提出的四個典型遞迴方程式進行嚴謹的數學推導，分別計算出其閉合形式精確解（Closed-form Solution）與對應的漸進時間複雜度（Big-O）[cite: 3]。

---

## 📝 Detailed Mathematical Derivation

### Problem 1

$$T(n) = T(n-1) + 8, \quad T(1) = 1$$[cite: 3]

#### 1. 代換法展開 (Iteration / Expansion Method)

$$
\begin{aligned}
T(n) &= T(n-1) + 8 \\
&= [T(n-2) + 8] + 8 = T(n-2) + 2 \times 8 \\
&= [T(n-3) + 8] + 2 \times 8 = T(n-3) + 3 \times 8 \\
&\dots \\
&= T(n-k) + k \times 8
\end{aligned}
$$

#### 2. 代入邊界條件

令 $n - k = 1 \implies k = n - 1$：

$$
\begin{aligned}
T(n) &= T(1) + (n - 1) \times 8 \\
&= 1 + 8n - 8 \\
&= 8n - 7
\end{aligned}
$$

- **精確解 (Exact Solution)**: $T(n) = 8n - 7$
- **時間複雜度 (Big-O)**: $O(n)$

---

### Problem 2

$$T(n) = 2T(n-1) + 9, \quad T(1) = 1$$[cite: 3]

#### 1. 代換法展開 (Iteration / Expansion Method)

$$
\begin{aligned}
T(n) &= 2T(n-1) + 9 \\
&= 2[2T(n-2) + 9] + 9 = 2^2 T(n-2) + 2 \times 9 + 9 \\
&= 2^2[2T(n-3) + 9] + 2 \times 9 + 9 = 2^3 T(n-3) + 9(2^2 + 2^1 + 1) \\
&\dots \\
&= 2^k T(n-k) + 9 \sum_{i=0}^{k-1} 2^i
\end{aligned}
$$

#### 2. 代入邊界條件

令 $n - k = 1 \implies k = n - 1$：

$$
\begin{aligned}
T(n) &= 2^{n-1} T(1) + 9 \sum_{i=0}^{n-2} 2^i \\
&= 2^{n-1} \times 1 + 9 \times \frac{2^{n-1} - 1}{2 - 1} \\
&= 2^{n-1} + 9(2^{n-1} - 1) \\
&= 10 \times 2^{n-1} - 9 \\
&= 5 \times 2^n - 9
\end{aligned}
$$

- **精確解 (Exact Solution)**: $T(n) = 10 \times 2^{n-1} - 9 = 5 \times 2^n - 9$
- **時間複雜度 (Big-O)**: $O(2^n)$

---

### Problem 3

$$T(n) = 2T(n/2) + 1, \quad T(1) = 1$$[cite: 3]

#### 1. 代換法展開（假設 $n = 2^k \implies k = \log_2 n$）

$$
\begin{aligned}
T(n) &= 2T\left(\frac{n}{2}\right) + 1 \\
&= 2\left[2T\left(\frac{n}{4}\right) + 1\right] + 1 = 2^2 T\left(\frac{n}{2^2}\right) + 2 + 1 \\
&= 2^2\left[2T\left(\frac{n}{8}\right) + 1\right] + 2 + 1 = 2^3 T\left(\frac{n}{2^3}\right) + 2^2 + 2^1 + 1 \\
&\dots \\
&= 2^k T\left(\frac{n}{2^k}\right) + \sum_{i=0}^{k-1} 2^i
\end{aligned}
$$

#### 2. 代入邊界條件 $\frac{n}{2^k} = 1$

$$
\begin{aligned}
T(n) &= 2^k T(1) + \frac{2^k - 1}{2 - 1} \\
&= n \times 1 + (n - 1) \\
&= 2n - 1
\end{aligned}
$$

_(註：若使用主定理 Master Theorem：$a = 2, b = 2, f(n) = 1$。因 $n^{\log_b a} = n^{\log_2 2} = n^1$，而 $f(n) = O(n^{1-\epsilon})$，符合 Case 1，故 $T(n) = \Theta(n)$)_

- **精確解 (Exact Solution)**: $T(n) = 2n - 1$
- **時間複雜度 (Big-O)**: $O(n)$

---

### Problem 4

$$T(n) = T(n/2) + 1, \quad T(1) = 1$$[cite: 3]

#### 1. 代換法展開（假設 $n = 2^k \implies k = \log_2 n$）

$$
\begin{aligned}
T(n) &= T\left(\frac{n}{2}\right) + 1 \\
&= \left[T\left(\frac{n}{4}\right) + 1\right] + 1 = T\left(\frac{n}{2^2}\right) + 2 \\
&= \left[T\left(\frac{n}{8}\right) + 1\right] + 2 = T\left(\frac{n}{2^3}\right) + 3 \\
&\dots \\
&= T\left(\frac{n}{2^k}\right) + k
\end{aligned}
$$

#### 2. 代入邊界條件 $\frac{n}{2^k} = 1$

$$
\begin{aligned}
T(n) &= T(1) + \log_2 n \\
&= 1 + \log_2 n
\end{aligned}
$$

_(註：此即經典的二元搜尋法 Binary Search 遞迴式。使用主定理 Master Theorem：$a = 1, b = 2, f(n) = 1$。因 $n^{\log_b a} = n^0 = 1 = \Theta(f(n))$，符合 Case 2，故 $T(n) = \Theta(\log n)$)_

- **精確解 (Exact Solution)**: $T(n) = \log_2 n + 1$
- **時間複雜度 (Big-O)**: $O(\log n)$

---

## 📊 Summary Table

| 題號  | 遞迴方程式                    | 經典對應演算法模型              | 精確閉合解 $T(n)$  | 時間複雜度  |
| :---: | :---------------------------- | :------------------------------ | :----------------: | :---------: |
| **1** | $T(n) = T(n-1) + 8$[cite: 3]  | 線性掃描 / 單重迴圈             |      $8n - 7$      |   $O(n)$    |
| **2** | $T(n) = 2T(n-1) + 9$[cite: 3] | 滿二元樹遞迴 (如未優化之河內塔) | $5 \times 2^n - 9$ |  $O(2^n)$   |
| **3** | $T(n) = 2T(n/2) + 1$[cite: 3] | 遍歷二元樹節點 / 分治簡化版     |      $2n - 1$      |   $O(n)$    |
| **4** | $T(n) = T(n/2) + 1$[cite: 3]  | 二元搜尋 (Binary Search)        |   $\log_2 n + 1$   | $O(\log n)$ |
