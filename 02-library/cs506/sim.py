def euclidean_dist(x, y):
    if x == [] and y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")

    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)


def manhattan_dist(x, y):
    if x == [] and y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")

    res = 0
    for i in range(len(x)):
        res += abs(x[i] - y[i])
    return res


def jaccard_dist(x, y):
    if x == [] and y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")

    setx = set(x)
    sety = set(y)
    intersect = setx & sety
    union = setx | sety
    return 1 - len(intersect)/len(union)


def dotProduct (x, y):
    res = 0
    for i in range(len(x)):
        res += x[i] * y[i]
    return res


def norm(x):
    res = 0
    for i in range(len(x)):
        res += x[i] ** 2
    return res**(1/2)


def cosine_sim(x, y):
    if x == [] and y == []:
        raise ValueError("lengths must not be zero")
    if len(x) != len(y):
        raise ValueError("lengths must be equal")

    return dotProduct(x,y) / (norm(x)*norm(y))

# Feel free to add more
# if x == [] and y == []:
#        raise ValueError("lengths must not be zero")
#    if len(x) != len(y):
#        raise ValueError("lengths must be equal")
