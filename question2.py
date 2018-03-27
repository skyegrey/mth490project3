########################################################
#2222222222222222222222222222222222222222222222222222222
def euclidean_distance(x_data, y_data, x_cluster, y_cluster):
    squared_distance = (x_data - x_cluster)**2 + (y_data - y_cluster)**2
    return squared_distance**.5

def manhattan_distance(x_data, y_data, x_cluster, y_cluster):
    return abs(x_data-x_cluster) + abs(y_data-y_cluster)

def chebyshev_distance(x_data, y_data, x_cluster, y_cluster):
    x_distance = abs(x_data - x_cluster)
    y_distance = abs(y_data - y_cluster)
    return max(x_distance,y_distance)

##test stuff
##x_data = 1
##y_data = -7
##x_cluster = 2
##y_cluster = 7
##print(chebyshev_distance(x_data,y_data,x_cluster,y_cluster))
  
test_data = (3,4)
x_data = test_data[0]
y_data = test_data[1]

training_data = [(3,5,1),(4,7,1),(5,8,0),(6,6,0),(4,9,0)]    ###training data entries are (study,sleep,pass/fail)

    
def k_nn_euclidean(k,test_data,training_data,distance_function):  
    
    distance_list = []
    
    for i in training_data:
        x_training = i[0]
        y_training = i[1]
        label_training = i[2]
        distance = distance_function(x_data,y_data, x_training, y_training)
        distance_list += [(distance,label_training)]

    distance_list.sort()
    distance_list = distance_list[:k]
    
    pass_counter = 0
    fail_counter = 0
    
    for i in distance_list:
        if i[1] == 1:
            pass_counter += 1
        if i[1] == 0:
            fail_counter += 1
    
    if pass_counter > fail_counter:
        return 1
    if fail_counter > pass_counter:
        return 0          
    
#####print(k_nn_euclidean(3,test_data,training_data))
########################################################
