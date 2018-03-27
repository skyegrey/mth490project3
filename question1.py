def predictor_function(data):
    return 7


####The RMSE function assumes the data is a list where each entry is (temp,ads)
def RMSE(data):
    MSE = 0
    for i in data:
        MSE += (predictor_function(i)-i)**2
    MSE = MSE / len(data)
    return (MSE)**.5



####Spearman's coefficient can use this function as well, just need to rank the ytrue and ypredicted
y_predicted = (1,2,3,4,5)
y_true = (5,3,2,4,1)

def Pearson(y_predicted, y_true):
    
    u_predicted = 0
    u_true = 0
    for i in range(0,len(y_predicted)):
        u_predicted += y_predicted[i]
        u_true += y_true[i]
    u_predicted = u_predicted / len(y_predicted)
    u_true= u_true / len(y_true)
    
    numerator = 0
    denom1 = 0
    denom2 = 0
    for i in range(0,len(y_predicted)):
        numerator += (y_predicted[i]-u_predicted)*(y_true[i]-u_true)
        denom1 += (y_predicted[i]-u_predicted)**2
        denom2 += (y_true[i]-u_true)**2

    return numerator / (denom1*denom2)**.5


def Kendall_Tau(y_predicted,y_true):
    P = 0
    Q = 0
    for i in range(0,len(y_predicted)):
        for j in range(0,len(y_predicted)):
            if y_predicted[i]>y_predicted[j] and y_true[i]>y_true[j]:
                P += 1
            if y_predicted[i]<y_predicted[j] and y_true[i]<y_true[j]:
                P += 1
            if y_predicted[i]<y_predicted[j] and y_true[i]>y_true[j]:
                Q += 1
            if y_predicted[i]>y_predicted[j] and y_true[i]<y_true[j]:
                Q += 1
    return 2*(P-Q) / (len(y_predicted)*(len(y_predicted)-1))
######no idea if this works, but it looks pretty good
                
####print(Kendall_Tau(y_predicted,y_true))
