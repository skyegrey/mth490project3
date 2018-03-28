
def euclidean_distance(x_data, y_data, x_cluster, y_cluster):
    squared_distance = (x_data - x_cluster)**2 + (y_data - y_cluster)**2
    return squared_distance**.5

# Select two clusters at random


data = [[-7,-5,'No'],[2,-1,'Yes'],[8,-5,'No'],[-4,-3,'Yes'],[-1,-7,'No'],[-3,10,'No'],[5,1,'No']]


def k_means(data):

    cluster1 = [2,2]
    cluster2 = [-2,-1]
    new_cluster1 = ''
    new_cluster2 = ''
    
    for i in data:
        
        x_data = i[0]
        y_data = i[1]
        
        distance1 = euclidean_distance(x_data,y_data,cluster1[0],cluster1[1])
        distance2 = euclidean_distance(x_data,y_data,cluster2[0],cluster2[1])
        
        if distance1 < distance2:
            i.append('cluster1')
            
        if distance2 < distance1:
            i.append('cluster2')

    
    new_cluster1 = [0,0]
    new_cluster2 = [0,0]
    counter_1 = 0
    counter_2 = 0
    
    
    for i in data:
        if i[3] == 'cluster1':
            new_cluster1[0] += i[0]
            new_cluster1[1] += i[1]
            counter_1 += 1
    
        if i[3] == 'cluster2':
            new_cluster2[0] += i[0]
            new_cluster2[1] += i[1]
            counter_2 += 1
    
    
    new_cluster1[0] = float(new_cluster1[0])
    new_cluster1[1] = float(new_cluster1[1])
    new_cluster2[0] = float(new_cluster2[0])
    new_cluster2[1] = float(new_cluster2[1])
    
    new_cluster1[0] = new_cluster1[0] / counter_1
    new_cluster1[1] = new_cluster1[1] / counter_1
    new_cluster2[0] = new_cluster2[0] / counter_2
    new_cluster2[1] = new_cluster2[1] / counter_2
    
    print(new_cluster1)
    print(cluster1)
    print(new_cluster2)
    print(cluster2)


    return [new_cluster1,new_cluster2]

k_means(data)
