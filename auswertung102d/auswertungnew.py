import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize

# Deklariere eine neue Funktion
def f(x, a, b):
    return a * x + b

def chi2(x, y, s, f, a, b):
    chi = (y - f(x, a, b)) / s
    return np.sum(chi**2)

# Ihre Messdaten kommen hier hin
xdata = np.array([31.43,21.16,14.23,11.5])
ydata1 = np.array([5,7,10,12])
sigma1 = np.array([0.1,0.1,0.1,0.1])
xerr = np.array([0.5,0.5,0.5,0.5])


# Startwerte für die Parameterbestimmung
x0 = np.array([1.0, 0.0])

fitParams1, fitCovariances1 = optimize.curve_fit(f, xdata, ydata1, x0, sigma=sigma1, absolute_sigma=True)

slope1 = fitParams1[0]
intercept1 = fitParams1[1]

fitErrors1 = np.sqrt(np.diag(fitCovariances1))

thischi2_1 = chi2(xdata, ydata1, sigma1, f, fitParams1[0], fitParams1[1])

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)

# Die Achsen brauchen auf jeden Fall eine Beschriftung
plt.ylabel('U [V]', fontsize=16)
plt.xlabel('Zeit [t]', fontsize=16)
plt.xlim(10, 40)
plt.ylim(0, 15)

# Plotte die Funktion mit Label und Linienstil
t = np.arange(1, 10, 0.0001)
plt.plot(t, f(t, slope1, intercept1), color='c', label='Fit 1')
plt.title('Motenspannung gegen Zeit')
plt.errorbar(xdata, ydata1, sigma1, xerr, fmt='mv', )

plt.grid(linestyle='-', color='0.9', linewidth=2)
plt.legend()

# Zeige den Plot
plt.show()

# Speichere den Plot
plt.savefig('uebung'.jpg', dpi=400) 

# Parameter ausgeben
print('Fit 1 - slope: {0:.3f} +- {1:.3f}, intercept: {2:.3f} +- {3:.3f}'.format(slope1, fitErrors1[0], intercept1, fitErrors1[1]))