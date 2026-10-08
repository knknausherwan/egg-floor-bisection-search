# 🥚 Egg Floor Bisection Search

A simple Python implementation of **bisection (binary) search** to find the floor where an egg does not break.

## 🎯 How It Works

The algorithm starts with a minimum and maximum floor and repeatedly checks the middle floor.

```text
min floor → middle floor → max floor
```

If the target floor is higher, the minimum is moved up.
If it is lower, the maximum is moved down.

This reduces the search space by roughly **half on every step**.

## 🧠 Mathematical Idea

After `x` bisection steps, we can distinguish between:

$$
2^x
$$

possibilities.

For `N` floors, we need:

$$
2^x \geq N
$$

Therefore:

$$
x \geq \log_2(N)
$$

For 102 floors:

$$
\log_2(102) \approx 6.67
$$

So approximately **7 steps** are needed.

This gives binary search its:

$$
\boxed{O(\log N)}
$$

time complexity.

## 📚 Concepts

* Bisection / Binary Search
* Divide and Conquer
* \(2^x\) and \(\log_2(N)\)
* Algorithmic Complexity
* Python Loops

## 🚀 Key Takeaway

Instead of checking floors one by one, bisection **cuts the search space in half at every step**, making the search much more efficient for large numbers of floors.
