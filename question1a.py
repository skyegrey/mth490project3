import sklearn
import pandas as pd
import math
# from question1b import regularize_loss
# import * from question1c as 1c


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


def loss_derivative(c_vector, t, a, r, location, change=.0001, reg=False):
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
    derivatives = []
    for index in range(0, len(c_vector)):
        derivatives.append(abs(loss_derivative(c_vector, t, a, r, index)))

    max_derivative = max(derivatives)
    print(f'max_derivative: {max_derivative}')
    best_index = derivatives.index(max_derivative)
    print(f'best_index: {best_index}')

    print(f'derivatives: {derivatives}')



    while not converged:
        if cycles > limit:
            break


        i = derivatives.index(max(derivatives))
        dev = loss_derivative(c_vector, t, a, r, i)
        derivatives[i] = abs(dev)
        # print(f"loss_derivate: {dev}")
        # print(f"c_vector: {c_vector}")
        c_vector[i] = c_vector[i] - (gamma*loss_derivative(c_vector, t, a, r, i))

        cycles = cycles + 1

        #i = (i + 1) % len(c_vector)

        # gamma += .000001

    print(f"dev: {derivatives}")
    print(f"c_vector: {c_vector}")
    print(f"avg error: {math.sqrt(loss(c_vector, t, a, r)/len(c_vector))}")
    return (loss(c_vector, t, a, r))


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

print(f"temp, ads: {temps}, {ads}")

# Start with a c_value
# Rough approximates of a previous gradient
# weights = [190, -16, 170, 1, 9, -21]
weights = [1, 1, 1, 1, 1, 1, 1]

# Get initial loss
# gradient_descent(weights, temps, ads, rev)
print(f"loss: {loss(weights, temps, ads, rev)}")
print(f"loss after gradient descent: {gradient_descent(weights, temps, ads, rev)}")
predicted = []
for i in range(0, len(rev)):
    predicted.append(model(weights, temps[i], ads[i]))
comparison = pd.DataFrame({'predicted': predicted, 'actual': rev})
print(comparison)

#print(f"loss after reg: {gradient_descent(weights, temps, ads, rev, True)}")






