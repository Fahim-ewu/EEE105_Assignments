x  = 36
tolerance = 10**(-4)
low = 0 
high = x 
iteration = 0
g = (low + high)/2
while abs(g**2 - x) >= tolerance:
    iteration += 1
    if g**2 < x:
        low = g
    else:
        high = g
    g = (low + high)/2
print(iteration)
print(g)