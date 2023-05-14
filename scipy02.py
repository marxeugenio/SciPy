from scipy import linalg

a = [1,1,1], [0,2,5], [2,5, -1]
b = [6, -4, 27]

x = linalg.solve(a,b)

print(x)