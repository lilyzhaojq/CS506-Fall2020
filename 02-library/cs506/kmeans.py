from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    for p in points:
        if p == [] or (len(p) != len(p[0])):
            raise ValueError()

    center = [0 for dim in range(len(p[0]))]
    
    for i in range(len(center_coords)):
        center[i] = sum([p[i] for p in points]) / len(points)
    
    return center


def update_centers(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    cl = {}

    for i in range(0,len(dataset)):
        if assignments[i] in cl:
            cl[assignments[i]].append(dataset[i])
        else:
            cl[assignments[i]] = [dataset[i]]

    list_centers = []

    for key in cl:
        list_centers += [point_avg(cl[key])]

    return list_centers 

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """
    psum = 0

    for i in range(len(a)):
        psum += (a[i]-b[i]) ** 2
	
    return psum ** (1/2)

def distance_squared(a, b):
    return distance(a,b) ** 2

def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    dlist = [i for i in range(len(dataset))]
	
    choice = random.choices(dlist, k = k)
    
    newset = [ dataset[i] for i in choice]
	
    return newset

def cost_function(clustering):
    cost = 0

    for point in clustering:
        centroid = point_avg(clustering[point])
        
        for axis in clustering[point]:
            cost += distance_squared(axis, centroid)
    
    return cost


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    centers = generate_k(dataset, 1)

    while(k != 0):
        dst = []

        for p in dataset:
            dst += [min([distance_squared(p, center) for center in centers])]

        prob = [x/sum(distances) for x in distances]

        centers += random.choices(dataset, weights = prob, k = 1)

        k -= 1

    return centers[1:]


def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
