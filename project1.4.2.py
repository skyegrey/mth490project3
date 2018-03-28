import math
import pandas
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Predictor function based on sigmoid function
# Input: Vector of X variables, Vector of C variables
# Output: Predicted values from the function (between 1 and 0)
def predictor_function(x_vector, c_vector):
    exponent = -c_vector[0]
    for i in range(0, len(x_vector)):
        exponent += -c_vector[i + 1]*x_vector[i]
    denominator = 1 + math.exp(exponent)
    if denominator != 0:
        return 1/denominator
    else:
        print('Denominator error')
        return None


def loss_function(x_vector, y_vector, c_vector, p=predictor_function):
    loss = 0
    m = len(y_vector)
    for i in range(0, len(x_vector)):
        #
        if y_vector[i] == 0:
            loss += -math.log(1 - p(x_vector[i], c_vector))
        #
        else:
            loss += -math.log(p(x_vector[i], c_vector))
    loss = loss/m
    # print('Loss:', loss)
    return loss


def div(h, x_vector, y_vector, c_vector, c_cord, f=loss_function):
    c_step = list(c_vector)
    c_step[c_cord] += h
    # print('c_vecs:', c_step, c_vector)
    y1 = f(x_vector, y_vector, c_vector)
    y2 = f(x_vector, y_vector, c_step)
    return (y2 - y1)/h


# Read in the data
sleep_data_frame = pandas.read_excel("StudySleep.xlsx")
sleep_data = sleep_data_frame.as_matrix()

# print("Sleep data:", sleep_data)

# Change classification to 0 for fail, and 1 for pass
for i in range(0, len(sleep_data)):
    if sleep_data[i][2] == 'Fail':
        sleep_data[i][2] = 0
    else:
        sleep_data[i][2] = 1

# Separate out the training data and test data
training_data = sleep_data[:10]
test_data = sleep_data[10:]

# Separate Y training and Y test values/data
y_training_data = training_data[:, 2]
y_test_data = test_data[:, 2]
y_training_data = y_training_data.astype("int")


# Separate X training and X test data/values
x_training_data = training_data[:, [0,1]]
x_test_data = test_data[:, [0,1]]
# print("\nX_training_data:\n", x_training_data)

# Start with a baseline C value
c_weights = [-1, 1, 1]
# c_weights = [-.82, 2.68, -3.01]
# c_weights = [0, 2, 0]
# print(predictor_function([10, 2], [0, 0, 0]))
print('loss before gradient descent:', loss_function(x_training_data, y_training_data, c_weights))

# Gradient Descent


# Numeric Differentiation:


print('c_weights before gradient descent:', c_weights)
# Descend C0
for n in range(0, 3):
    loss_last = loss_function(x_training_data, y_training_data, c_weights)
    derivative = div(.00001, x_training_data, y_training_data, c_weights, n)
    learning_rate = .01
    precision = .00001

    # print('c_weights before', c_weights)
    # Derivative is positive with respect to c0, reduce c0
    while abs(derivative) > precision:
        if derivative > 0:
            c_weights[n] += -learning_rate*derivative
        else:
            c_weights[n] += -learning_rate*derivative
        derivative = div(.001, x_training_data, y_training_data, c_weights, n)
        # print('derivative:', derivative)


# tc_weights = [-.82, 2.68, -3.01]
# print('Loss function test:', loss_function(x_training_data, y_training_data, tc_weights))
print('loss after:', loss_function(x_training_data, y_training_data, c_weights))
print('c_weigths after:', c_weights)

grid_x = []
grid_y = []
grid_z = []
for i in range(0, 16):
    for n in range(0, 10):
        grid_x.append(i)
        grid_y.append(n)
        grid_z.append(predictor_function([i,n], c_weights))

grid_x = np.asarray(grid_x)
grid_y = np.asarray(grid_y)
grid_z = np.asarray(grid_z)

# grid_matrix = np.matrix(grid)



# print(grid_x)

print('Probability that a person who sleeps 7 hours and studies 12 passes:', predictor_function([12, 7], c_weights))
study_list = []
sleep_list = []
for item in x_training_data:
    study_list.append(item[0])
    sleep_list.append(item[1])

x2_0 = -c_weights[0]/c_weights[2]
x1_0 = -c_weights[0]/c_weights[1]

plt.ylim([5, 9])
plt.plot([0, x2_0], [x1_0, 0], color='red')
plt.scatter(study_list, sleep_list)
plt.show()

fig = plt.figure()
ax = fig.gca(projection='3d')

# grid_x, grid_y = np.matrix(grid_x, grid_y)
# grid_z = np.array([grid_z])
# print('arrays:', grid_x)

surf = ax.scatter(grid_x, grid_y, grid_z)
plt.show()

# surface = Axes3D.plot_surface(grid_x, grid_y, grid_z)