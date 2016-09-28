from stats import *
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

setseed(int(round(time.time() * 1000)))

fancy = False
TRIALS = 40
if len(sys.argv) > 1:
    TRIALS = int(sys.argv[1])
    if len(sys.argv) > 2 and sys.argv[2]=='-fancy':
        fancy=True

# Get the data and add the numbers into a list
prices = []
f = open("prices.txt")
for line in f:
    v = float(line.strip())
    prices.append(v)

def sample(data):
    """
    Return a random sample of data values with replacement.
    The returned array has same length as data.
    """
    indexarray = [np.random.randint(0, len(data)) for i in range(len(data))]
    result = [data[j] for j in indexarray]
    return result

# Perform TRIALS number of samplings of prices and add the mean of each sample to X_

X_ = [mean(sample(prices)) for i in range(TRIALS)]
X_.sort()
inside = [X_[i] for i in range(int(TRIALS * 0.025), int(TRIALS * 0.975) + 1)]
inside_list = [inside[0], inside[-1]]
# print out the values on 95% boundary
print inside_list

fig = plt.figure()
ax = fig.add_subplot(111)

x = np.arange(1.05, 1.25, 0.001)
plt.axis([1.10, 1.201, 0, 30])
normal = [normpdf(i, mean(X_), np.sqrt(var(X_))) for i in x]
plt.plot(x, normal, '-r')
plt.plot(inside_list, [0, 0], '^')

mean = mean(X_)
stddev = np.sqrt(var(X_))
clt_left = mean - 1.96 * stddev
clt_right = mean + 1.96 * stddev
ci_x = np.arange(clt_left, clt_right, 0.001)
ci_y = normpdf(ci_x, mean, stddev)
# shade under (ci_x, ci_y) curve
plt.fill_between(ci_x, ci_y, color = "#F8ECE0")
plt.text(0.02, 0.95, '$TRIALS = %d$' % TRIALS, transform = ax.transAxes)
plt.text(0.02, 0.9, '$mean(prices)$ = %f' % np.mean(prices), transform = ax.transAxes)
plt.text(.02,.85, '$mean(\\overline{X})$ = %f' % np.mean(X_), transform = ax.transAxes)
plt.text(.02,.80, '$stddev(\\overline{X})$ = %f' % np.std(X_,ddof=1), transform = ax.transAxes)
plt.text(.02,.75, '95%% CI = ($%1.2f,\\ %1.2f$)' % (clt_left, clt_right), transform = ax.transAxes)
plt.text(1.135, 11.5, "Expected", fontsize=16)
plt.text(1.135, 10, "95% CI $\\mu \\pm 1.96\\sigma$", fontsize=16)
plt.title("95% Confidence Intervals: $\\mu \\pm 1.96\\sigma$", fontsize=16)
ax.annotate("Empirical 95% CI", xy=(clt_left, 0), xycoords="data", xytext=(1.13,4), textcoords='data',
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"), fontsize=16)

plt.savefig('bootstrap-'+str(TRIALS)+('-basic' if not fancy else '')+'.pdf', format="pdf")
plt.show()
