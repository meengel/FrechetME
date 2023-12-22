### Michael Engel ### 2023-12-22 ### TEST_FrechetME.py
import numpy as np
from functools import partial

from FrechetME import getFrechetMean, geodesicMeanLonLat

points = np.array([[-55,-11],[55,-11],[22,88]], ndmin=2)
radius = 1

result = getFrechetMean(
        points = points,
        distance = partial(geodesicMeanLonLat, R=radius),
        startpoint = None,
        threshold = 1e-9,
        threshold_order = 1,
        optimizer = None,
        optimizerkwargs = {"lr":1e-2, "weight_decay":0},
        maxiter = 50000
)