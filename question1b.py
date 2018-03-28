# import question1a as q1a #loss_derivative, gradient_descent
import pandas as pd
import math
import sklearn

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


def regularized_model():
    lam = .01


def regularize_loss(c_vector, t, a, r, lam):
    standard_loss = loss(c_vector, t, a, r)
    reg_term = 0
    for i in range(1, len(c_vector)):
        reg_term += c_vector[i]**2
    return standard_loss + (lam/2)*reg_term


def reg_loss_derivative(c_vector, t, a, r, index, lam, change=.001):
    test_vec = list(c_vector)
    test_vec[index] += change

    difference = regularize_loss(test_vec, t, a, r, lam) - regularize_loss(c_vector, t, a, r, lam)

    return difference/change


def gradient_descent_regularized(c_vector, t, a, r, lam):
    converged = False
    cycles = 0
    limit = 10000
    gamma = .0001

    index = 0

    while not converged:
        if cycles > limit:
            break

        dev = reg_loss_derivative(c_vector, t, a, r, index, lam)
        c_vector[index] = c_vector[index] - gamma*dev

        cycles += 1
        index = (index + 1) % len(c_vector)

    print(f"loss after descent:{regularize_loss(c_vector, t, a, r, index)}")


# Get the data
data_frame = pd.read_excel("HotChocSales.xlsx", header=0)
temps = list(data_frame['Temp'])
ads = list(data_frame['Ads'])
rev = data_frame['Revenue']

# Normalize Data
for i in range(0, len(temps)):
    temps[i] = (float(temps[i]) + 10)
    ads[i] = (float(ads[i]) + 1)
    rev[i] = rev[i]
weights = [1, 1, 1, 1, 1, 1]

# Calculate regularized gradient descent
print(f"loss before:{regularize_loss(weights, temps, ads, rev, 1)}")
gradient_descent_regularized(weights, temps, ads, rev, .01)

predicted = []
for i in range(0, len(rev)):
    predicted.append(model(weights, temps[i], ads[i]))
comparison = pd.DataFrame({'predicted': predicted, 'actual': rev})
print(comparison)