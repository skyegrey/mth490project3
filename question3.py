
def euclidean_distance(x_data, y_data, x_cluster, y_cluster):
    squared_distance = (x_data - x_cluster)**2 + (y_data - y_cluster)**2
    return squared_distance**.5

##select two clusters at random

cluster1 = [2,2]
cluster2 = [-2,-1]

data = [[-7,-5,'No'],[2,-1,'Yes'],[8,-5,'No'],[-4,-3,'Yes']]


for i in data:
    
    x_data = i[0]
    y_data = i[1]
    
    distance1 = euclidean_distance(x_data,y_data,cluster1[0],cluster1[1])
    distance2 = euclidean_distance(x_data,y_data,cluster2[0],cluster2[1])
    
    class_1 = []
    class_2 = []
    
    if distance1 < distance2:
        i.append('cluster1')
        
    if distance2 < distance1:
        i.append('cluster2')


cluster1 = [0,0]
cluster2 = [0,0]
counter_1 = 0
counter_2 = 0

for i in data:
    if i[3] == 'cluster1':
        cluster1[0] += i[0]
        cluster1[1] += i[1]
        counter_1 += 1

    if i[3] == 'cluster2':
        cluster2[0] += i[0]
        cluster2[1] += i[1]
        counter_2 += 1

cluster1[0] = float(cluster1[0])
cluster1[1] = float(cluster1[1])
cluster2[0] = float(cluster2[0])
cluster2[1] = float(cluster2[1])

cluster1[0] = cluster1[0] / counter_1
cluster1[1] = cluster1[1] / counter_1
cluster2[0] = cluster2[0] / counter_2
cluster2[1] = cluster2[1] / counter_2

print(cluster1)
print(cluster2)
