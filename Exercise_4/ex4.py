#This is the in-class exercise of Lecture_4
#Calculate the second derivate of cos(x) using the central different algorithm.

import numpy as np
import math
import matplotlib.pyplot as plt

x = 1
y = math.cos(x)
N = 10000

# The second derivate is called de2, using equation 1
def de2(x, h):
    return (((math.cos(x+h)-math.cos(x)) - (math.cos(x)-math.cos(x-h)))/h**2)
def de2eq2(x, h):
    return((math.cos(x+h) + math.cos(x-h) - 2*math.cos(x))/h**2)

'''
pi = math.pi
h = pi/10

# The real answer of secend derivate of cos(1)
real = -1*math.cos(1)

# The relative error when x=1
re_error = (de2(1, h)-real)/real
print("The relative error when x=1 is ", re_error)
'''

computed_ans = []
error_plot = []
error_log = []
h_plot = []
h_log = []
real_ans = -1 * math.cos(x)
print(f"real answer is {real_ans}")
pi = math.pi
x = 1
h = pi/10

for i in range(N):
    if h < 0:
        break
    print(f"{i}th h is {h}")
    computed_ans.append(de2(x, h))
    print(f"{i}th computed ans is {computed_ans[i]}")
    error = (computed_ans[i]-real_ans)/real_ans
    error_plot.append(error)
    print(f"{i}th error is {error}")
    error_log.append(math.log(abs(error), 10))
    h_log.append(math.log(abs(h), 10))
    h_plot.append(h)
    h -= 1/10000
    if i != 0 and error_log[i] > error_log[i-1]:
        print(f"At {i} has the smallest error.")
        break


computed_ans2 = []
error_plot2 = []
error_log2 = []
h_plot2 = []
h_log2 = []
x = 1
h2 = pi/10

for i in range(N):
    if h2 < 0:
        break
    #print(f"{i}th h2 is {h2}")
    computed_ans2.append(de2eq2(x, h2))
    #print(f"{i}th computed ans2 is {computed_ans[i]}")
    error = (computed_ans2[i]-real_ans)/real_ans
    error_plot2.append(error)
    print(f"{i}th error2 is {error}")
    error_log2.append(math.log(abs(error), 10))
    h_log2.append(math.log(abs(h2), 10))
    h_plot2.append(h2)
    h2 -= 1/10000
    if i != 0 and error_log2[i] > error_log2[i-1]:
        print(f"At {i} has the smallest error.")
        break



fig = plt.figure(figsize = (7, 5), dpi = 100)
ax1 = fig.add_subplot(1, 1, 1)
line1, = ax1.plot(h_log, error_log, 'b-', linewidth = 2, label = 'equation 1')
line2, = ax1.plot(h_log2, error_log2, 'r--', linewidth = 2, label = 'equation 2')
ax1.legend(handles=[line1, line2])
ax1.invert_xaxis()
ax1.set_xlabel('$log_{10}$h', fontsize = 13)
ax1.set_ylabel('$log_{10}$relative error', fontsize = 13)

'''
ax2 = fig.add_subplot(2, 1, 2)
ax2.plot(h_log2, error_log2, 'g-', linewidth = 2)
ax2.set_xlabel('$log_{10}$h', fontsize = 13)
ax2.set_ylabel('$log_{10}$relative error', fontsize = 13)
ax2.set_title('Equation 2')
'''
fig.tight_layout()
plt.grid()
plt.show()


