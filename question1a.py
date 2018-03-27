import sklearn
import pandas as pd


def model(c_vector, t, a):
    return c_vector[0] + c_vector[1]*t + c_vector[2]*a + c_vector[3]*(t**2) + c_vector[4]*(a**2) + c_vector[5]*(a*t)


# Numerical differentiation with respect to c_location
def model_derivative(c_vector, t, a, location, change=.1):
    test_vector = list(c_vector[location] + change)
    dev_diff = model(test_vector, t, a) - model(c_vector, t, a)
    return dev_diff/change


def loss(c_vector, t, a, r):
    total_loss = 0
    difference = 0
    for i in range(0, len(t)):
        difference = model(c_vector, t[i], a[i]) - r[i]
        total_loss += difference**2
    return total_loss



def linear_regression():
    pass


def gradient_descent(f, c_vector, t, a, r):
    converged = False
    cycles = 100
    i = 0
    while not converged:
        




# Get the data
data_frame = pd.read_excel("HotChocSales.xlsx", header=0)
temps = data_frame['Temp']
ads = data_frame['Ads']
rev = data_frame['Revenue']

# Start with a c_value
weights = [1,1,1,1,1,1]

# Get initial loss
print(f"loss: {loss(weights, temps, ads, rev)}")



