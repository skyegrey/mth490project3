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
    return (1/len(r))*total_loss


def loss_derivative(c_vector, t, a, r, location, change=.01):
    test_vector = list(c_vector)
    test_vector[location] += change
    dev_diff = loss(test_vector, t, a, r) - loss(c_vector, t, a, r)
    return dev_diff/change


def linear_regression():
    pass


def gradient_descent(c_vector, t, a, r):
    converged = False
    print(f"c_vector before: {c_vector}")
    limit = 10000
    cycles = 0
    gamma = .0001
    i = 0
    while not converged:
        if cycles > limit:
            break

        dev = loss_derivative(c_vector, t, a, r, i)
        # print(f"loss_derivate: {dev}")
        c_vector[i] += -gamma*dev

        i = (i + 1)%len(c_vector)
        cycles = cycles + 1

    print(f"c_vector: {c_vector}")
    return loss(c_vector, t, a, r)


# Get the data
data_frame = pd.read_excel("HotChocSales.xlsx", header=0)
temps = data_frame['Temp']
for i in range(0, len(temps)):
    temps[i] = temps[i] + 10
ads = data_frame['Ads']
rev = data_frame['Revenue']

# Start with a c_value
weights = [1,1,1,1,1,1]

# Get initial loss
# gradient_descent(weights, temps, ads, rev)
print(f"loss: {loss(weights, temps, ads, rev)}")
print(f"loss_test: {loss([3,1,1,1,1,1], temps, ads, rev)}")
print(f"loss after gradient descent: {gradient_descent(weights, temps, ads, rev)}")
print(f"model estimation of 6, 4, 1112: {model(weights, 6, 4)}")




