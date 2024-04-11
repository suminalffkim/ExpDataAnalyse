import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy.odr import ODR, Model, RealData
import numpy as np
import csv
import os
import pandas as pd


# auch alternative zeigen wie man direkt aus ods/xlsx liest
# Hier wird der Input im CSV-Format eingelesen.
# Als Argument bekomment die Funktion den Pfad zur Datei.
# Achtung: es wird erwartet, dass die erste Zeile Ueberschriften
# enthaelt!
def read_csv_input(filename):
    # Datei wird lesend geoeffnet.
    with open(filename, "r") as file:
        # Ein "Reader" wird aufgesetzt, der die Datei liest.
        # Ausserdem wird das Trennungszeichen zwischen den Spalten
        # definiert.
        dictR = csv.DictReader(file, delimiter=",")
        # Es wurden keine fieldnames beim Aufruf von DictReader definiert,
        # deswegen werden als Default die Werte aus der ersten Zeile als
        # fieldnames aka Header genommen.
        # Diese Zeile erstellt ein Python-Dictionary, welches als Keys
        # die Ueberschriften enthaelt und ansonsten leer ist.
        data = {hdr: [] for hdr in dictR.fieldnames}
        # Loope durch jede Zeile
        for row in dictR:
            # Loope durch jede Spalte in jeder Zeile
            for field in row:
                # Fuege den aktuellen Wert der aktuellen Spalte hinzu.
                # Falls der Wert keine Zahl ist (z.B. eine leere Zelle),
                # soll er als Null interpretiert werden.
                try:
                    data[field].append(float(row[field]))
                except ValueError:
                    data[field].append(0.)
    # Das fertige Python-Dictionary wird zurueckgegeben
    return data


# Definition einer linearen Funktion, welche gefittet werden soll
def linear_func(x, m, b):
    return m * x + b

def chi2(x, y, s, f, a, b):
    chi = (y - f(x, a, b)) / s
    return np.sum(chi**2)

# Als Argument bekommt die Funktion das Werte-Dictionary von
# der Funktion read_csv_input()
def auswertung_102d(data):
    # Hier könnte Ihre Auswertung stehen!
    # Ein kurzes Tutorial dazu wie man Daten graphisch darstellen kann, finden Sie unter:
    # https://matplotlib.org/stable/tutorials/pyplot.html
    # Einige Beispiele zum Fitten von Funktionen finden Sie etwa unter:
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

    # Startwerte für die Parameterbestimmung (chisqrFit)
    x0 = np.array([1.0, 0.0])

    fitParams1, fitCovariances1 = optimize.curve_fit(f, xdata, ydata1, x0, sigma=sigma1, absolute_sigma=True)

    slope1 = fitParams1[0]
    intercept1 = fitParams1[1]

    fitErrors1 = np.sqrt(np.diag(fitCovariances1))

    thischi2_1 = chi2(xdata, ydata1, sigma1, f, fitParams1[0], fitParams1[1])   


    fig, ax = plt.subplots()
    
    fig = plt.figure(figsize=(10, 6))

    # Die Achsen brauchen auf jeden Fall eine Beschriftung
    plt.ylabel('U [V]', fontsize=16)
    plt.xlabel('Frequenz/Umdrehung [1/s]', fontsize=16)
    # plt.xlim(10, 40)
    # plt.ylim(0, 15)

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
    plt.savefig('102d.png', dpi=400) 

    # # Parameter ausgeben
    # print('Fit 1 - slope: {0:.3f} +- {1:.3f}, intercept: {2:.3f} +- {3:.3f}'.format(slope1, fitErrors1[0], intercept1, fitErrors1[1]))


    # Gebe die Fitparameter zurueck, um sie in der naechsten Aufgabe weiter-
    # verwenden zu koennen.
    print(optimizedParameters, np.sqrt(np.diag(pcov)))
    return optimizedParameters


if __name__ == '__main__':
    input_dir = "Daten_Versuch_102"
    params = None
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".csv"):
            data = read_csv_input(os.path.join(input_dir, filename))
            data_tex = pd.DataFrame.from_dict(data)
            data_tex = data_tex.to_latex(index=False)
            print(data_tex)

            xdata=1/(data[:,0]/10)
            print(xdata)
            #hier weiter machen
            params = auswertung_102d(data)
