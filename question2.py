
import pandas

def euclidean_distance(x_data, y_data, x_cluster, y_cluster):
    squared_distance = (x_data - x_cluster)**2 + (y_data - y_cluster)**2
    return squared_distance**.5

def manhattan_distance(x_data, y_data, x_cluster, y_cluster):
    return abs(x_data-x_cluster) + abs(y_data-y_cluster)

def chebyshev_distance(x_data, y_data, x_cluster, y_cluster):
    x_distance = abs(x_data - x_cluster)
    y_distance = abs(y_data - y_cluster)
    return max(x_distance,y_distance)



# Getting the data
sleep_data_frame = pandas.read_excel("StudySleep.xlsx")
sleep_data = sleep_data_frame.as_matrix()

training_data = sleep_data[:10]
test_data = sleep_data[10:12]

    
def k_nn(k,test_point,training_data,distance_function):  
    
    distance_list = []
    
    x_test = test_point[0]
    y_test = test_point[1]

    for i in training_data:
        x_training = i[0]
        y_training = i[1]
        label_training = i[2]
        distance = distance_function(x_test,y_test, x_training, y_training)
        distance_list += [(distance,label_training)]

    distance_list.sort()
    distance_list = distance_list[:k]
    
    pass_counter = 0
    fail_counter = 0
    
    for i in distance_list:
        if i[1] == "Pass":
            pass_counter += 1
        if i[1] == "Fail":
            fail_counter += 1
    
    if pass_counter > fail_counter:
        return "Pass"
    if fail_counter > pass_counter:
        return "Fail"

 
# Output of results
# To change value of k, change the first argument of the k_nn_euclidean function
print("Based on 3-NN, Euclidean, the prediction for test point 1 is:")
print(k_nn(3,test_data[0],training_data,euclidean_distance))
print("Based on 3-NN, Euclidean the prediction for test point 2 is:")
print(k_nn(3,test_data[1],training_data,euclidean_distance))

print("\nBased on 3-NN, Manhattan, the prediction for test point 1 is:")
print(k_nn(3,test_data[0],training_data,manhattan_distance))
print("Based on 3-NN, Manhattan the prediction for test point 2 is:")
print(k_nn(3,test_data[1],training_data,manhattan_distance))

print("\nBased on 3-NN, Chebyshev, the prediction for test point 1 is:")
print(k_nn(3,test_data[0],training_data,chebyshev_distance))
print("\nBased on 3-NN, Chebyshev, the prediction for test point 2 is:")
print(k_nn(3,test_data[1],training_data,chebyshev_distance))
