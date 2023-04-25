#!/usr/bin/env python

import numpy as np

def fitness_1(x):
    # Himmelblau's function
    # f = (x^2 + y - 11)^2 + (x + y^2 -7)^2
    X = np.array(X).reshape(-1,1)
    x,y = X[0,0], X[1][0]
    f = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
    return f
