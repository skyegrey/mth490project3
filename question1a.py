import sklearn


def model(c_vector, t, a):
    return c_vector[0] + c_vector[1]*t + c_vector[2]*a + c_vector[3]*(t**2) + c_vector[4]*(a**2) + c_vector[5]*(a*t)


def linear_regression():
    pass


def gradient_descent():
    pass

# Get the data