import matplotlib.pyplot as plt
import numpy as np
from services.database import fetch_x, fetch_y
from collections import Counter

def mean(x, y):
    x_mean = float(np.mean(x)) if x else None
    y_mean = float(np.mean(y)) if y else None
    return x_mean,y_mean

def median(x, y):
    x_median = float(np.median(x)) if x else None
    y_median = float(np.median(y)) if y else None
    return x_median, y_median

def mode(x, y):
    def strict_mode(arr):
        if not arr:
            return None
        counts = Counter(arr)
        max_freq = max(counts.values())
        # If the highest frequency occurs only once or multiple values tie, return None
        modes = [val for val, freq in counts.items() if freq == max_freq]
        if len(modes) != 1:
            return None
        return modes[0]

    x_mode = strict_mode(x)
    y_mode = strict_mode(y)
    return x_mode, y_mode

def best_fit(x: list[float], y: list[float]):
    m, b = np.polyfit(x, y, deg=1)
    return m, b

def quadInterpolation(xValue, yValue):
    x = []
    y = []
    
    size=len(xValue)
    for row in range(size):
        x.append(np.array(xValue[row]))
        y.append(np.array(yValue[row]))

    # Sort x and y values based on x
    sorted_indices = np.argsort(x)
    x = np.array(x)[sorted_indices]
    y = np.array(y)[sorted_indices]
    
    interpolated_points = []
    if(x[0] == x[1]):
        m = (y[1]-y[0])/(0.1) # to avoid division by zero
        x_range = [x[0]] * 50
        y_range = np.linspace(y[0], y[1], 50)
        interpolated_points.extend(zip(x_range, y_range))
    else:
        m = (y[1] - y[0]) / (x[1] - x[0])
        x_range = np.linspace(x[0], x[1], 50)
        y_range = m*(x_range - x[0]) + y[0]
        interpolated_points.extend(zip(x_range, y_range))
    
    for i in range(1, size - 1):
        # if x[i] == x[i+1], then it is a vertical segment
        if x[i] == x[i+1]:
            m = (y[i+1] - y[i]) / (0.1)
            x_range = [x[i]] * 50
            y_range = np.linspace(y[i], y[i + 1], 50)
            interpolated_points.extend(zip(x_range, y_range))
            continue
       
    
        a = ((y[i+1]-y[i]) - m*(x[i+1]-x[i]))/(x[i+1]-x[i])**2
        b = m - 2*a*x[i]
        c = y[i+1] - a*x[i+1]**2 + 2*a*x[i]*x[i+1] - m*x[i+1]
        x_range = np.linspace(x[i], x[i+1], 50)
        y_range = a*(x_range)**2 + b*(x_range) + c
        interpolated_points.extend(zip(x_range, y_range))
        m = 2*a*x[i+1] + b

    return interpolated_points




