import matplotlib.pyplot as plt
import numpy as np
from database import fetch_x, fetch_y
from config import connection_pool

def best_fit(x, y):
    m, b = np.polyfit(x, y, deg=1)
    return m, b

def quadInterpolation(xValue, yValue):
    x = []
    y = []
    
    xValue = [x[0] for x in fetch_x()]
    yValue = [y[0] for y in fetch_y()]
    
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

def mean(x, y):
    # Handle empty dataset
    if len(x)==0 or len(y)==0:
        print("No data points available.")
        mean = (None, None)  # Return None for both x and y if no data exists
    else:
        # Round the mean values to two decimal places
        mean = (round((sum(x) / len(x)), 2), round((sum(y) / len(y)), 2))

    return mean

def median(x, y):
    # Get the total number of points
    x.sort()
    y.sort()
    count = len(x)
    if count == 0:
        print("No data points available.")
        return None  # Return None if there are no rows

    # For even count, fetch the two middle rows and calculate the median
    if count % 2 == 0:
        medianlist =(x[(count//2)-1], y[(count//2)-1]), (x[count//2], y[count//2])
        median = [
            round((medianlist[0][0] + medianlist[1][0]) / 2, 2),  # Median for x_value
            round((medianlist[0][1] + medianlist[1][1]) / 2, 2)   # Median for y_value
        ]
    else:
        # For odd count, fetch the middle row
        result = (x[count // 2], y[count // 2])  # Get the middle element
        median = (round(result[0], 2), round(result[1], 2))  # Round the median values

    return median


def mode(x, y):
    x.sort()
    y.sort()
    y_count = 0
    x_count = 0
    x_id = None
    y_id = None
    temp_x_count = 0
    temp_y_count = 0
    for i in range(len(x)):
        temp_x_count+=1
        if i == len(x)-1 or x[i] != x[i+1]:
            if temp_x_count > x_count:
                x_count = temp_x_count
                x_id = x[i]
            elif temp_x_count == x_count:
                x_id = None
            temp_x_count = 0
    for i in range(len(y)):
        temp_y_count+=1
        if i == len(y)-1 or y[i] != y[i+1]:
            if temp_y_count > y_count:
                y_count = temp_y_count
                y_id = y[i]
            elif temp_y_count == y_count:
                y_id = None
            temp_y_count = 0
    
    result = (x_id, y_id)

    return result

