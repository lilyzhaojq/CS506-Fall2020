def euclidean_dist(x, y):
<<<<<<< HEAD
    if (len(x) != len(y)):
        raise ValueError("lengths must be equal")

    if (len(x) == 0 and len(y) == 0 ):
        raise ValueError("lengths must not be zero")


    dim = len(x)

    sum = 0

    for i in range(dim):
       sum += (x[i] - y[i]) ** 2

    return sum ** (1/2)

=======
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)
>>>>>>> eb2e6f704bd9a389f973d364da1d68e917e2966a

def manhattan_dist(x, y):
    dim = len(x)

    sum = 0

    for i in range(dim):
       sum += abs(x[i] - y[i])

    return sum

def jaccard_dist(x, y):
    if (x==[] and y == []):
        raise ValueError("lengths must not be zero")

    if(len(x) != len(y)):
        raise ValueError("lengths must be equal")


    jaccard_sim = len(set(x) & set(y))/len(set(x) | set(y))
    return (1 - jaccard_sim)

def cosine_sim(x, y):
    if (x==[] and y == []):
        raise ValueError("lengths must not be zero")

    if(len(x) != len(y)):
        raise ValueError("lengths must be equal")

    dim = len(x)

    dot = 0
    xsum = 0
    ysum = 0

    for i in range(dim):
        dot += x[i] * y[i]
        xsum += x[i] ** 2
        ysum += y[i] ** 2

    return dot/(xsum * ysum ** (1/2))


# Feel free to add more
