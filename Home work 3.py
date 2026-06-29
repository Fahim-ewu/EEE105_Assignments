def f(x):
    x = x**3 - 6*x + 2
x = input("Enter the value of x: ")
tolerance = 10**(-4)
low = 0
high = x
iteration = 0
g = (low + high)/2
while abs(f(g)) >= tolerance:
    iteration += 1
    if f(g) < 0:
        low = g
    else:
        high = g
    g = (low + high)/2
print(f"The root is approximately {g}")
print(f"Number of iterations: {iteration}")
