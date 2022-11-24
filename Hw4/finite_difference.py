import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

# Use part of the code from hw3 example solution.
def a2ab(N, a, l, u):
    # Initialize ab
    ab = np.zeros((l + u + 1, N))
    # Transform a to ab
    for i in range(N):
        for j in range(max(i - l, 0), min(u + i + 1, N)):
            # print((i,j), '=>', (u + i - j, j))
            ab[u + i - j, j] = a[i, j]
    return ab

def func(t):
    return t**3-t+1

N = 19
A = np.zeros((N, N))

for i in range(1, N-1):
    A[i, i] = -2
    A[i, i+1] = A[i, i-1] = 1

A[0, 0] = A[N-1, N-1] = -2
A[0, 1] = A[N-1, N-2] = 1

print(np.shape(A))

b = np.zeros((N, 1))
h = 0.05
k = 6*h
b[0] = k * (h**2) - 1
b[N-1] = (N-1) * k * (h**2) - 1
for i in range(1, N-1):
    print(i)
    b[i] = (i+1) * k * (h**2)
print((b))

# For matrix A, there is two nonzero diagonal below the main diagonal (l = 1),
# and two above (u = 1). The diagonal banded form of the matrix is:
AB = a2ab(N=N, a=A, l=1, u=1)

'''
ab = np.zeros((3, N))
for i in range(1, N-1):
    ab[0][i] = 1
    ab[1][i] = -2
    ab[2][i] = 1
ab[1][0] = ab[1][N-1] = -2
print(np.shape(ab))
'''

y = solve_banded((1, 1), AB, b)
#print(y)

print(np.allclose(A @ y - b, np.zeros((N,))))

y_plot = np.zeros((N+2, 1))
y_plot[0] = y_plot[N+1] = 1
for i in range(1, N+1):
    y_plot[i] = y[i-1]
t = np.zeros((N+2, 1))
#print(np.shape(t))
for i in range(N+2):
    t[i] = 0 + h*i
#print(t)

ana_y = np.zeros((N+2, 1))
for i in range(N+2):
    ana_y[i] = func(t[i])
#print(ana_y)
fig = plt.figure(figsize = (7, 5), dpi = 100)
ax = fig.add_subplot(1, 1, 1)

ax.plot(t, ana_y, 'g-', linestyle = 'solid', label='Analytical')
ax.plot(t, y_plot, 'bo', markersize = 4, label='Numerical')

ax.set_xlabel('time', fontsize = 13)
ax.set_ylabel('y value', fontsize = 13)
plt.legend()

ax.set_title('finite-difference method')
fig.tight_layout()
plt.grid()
plt.show()
fig.savefig('finite_diff.png')

