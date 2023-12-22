# FrechetME
A small functionality for efficiently finding the Frechet mean of points for an arbitrary distance measure. 

## Key Features
The package is of particular importance if you want to find the centroid of a polygon on a sphere, for example. Suppose, you would like to build a new airport which is as close to all other airports as possible. Then, you would have to compute the Frechet mean of all airports with respect to the geodesic distance to get the desired location. You may also implement distance measures with Karush-Kuhn-Tucker conditions.

## Installation
Currently, we did not provide the package via pip or conda. However, You may install it with `pip install -e /PATH/TO/FrechetME-repository`.