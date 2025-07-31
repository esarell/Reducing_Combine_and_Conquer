import numpy as np


def Black_Scholes(x,K,s):
    #Genrates the distribution
    y = []
    test = np.log(K * s)
    print(-test)
    for i in x:
        if -test <= i < 0:
            y.append(K - (np.exp(-i) / s))
        elif 0 < i <= test:
            y.append(K - (np.exp(i) / s))
        else:
            print("inf")
            y.append(0.0000001)
    return y

def prob_normalised(data):
    """
    :param data:
    :return:
    """
    data = np.array(data)
    result=[]
    for x in data:
        square = x*x
        norm = np.sqrt(square/sum(data*data))
        result.append(norm)
    return result


def gsp_thetas(amps,m,n):
    gsp_angles=[]
    for i in range(m):
        j=pow(2,i)
        for x in range(j):
            start=int(x*pow(2,n-i))
            mid = int((x+0.5)*pow(2,n-i))
            end = int((x+1)*pow(2,n-i))
            upper = sum(amps[start:(mid)])
            lesser =sum(amps[start:(end)])
            costheta2 = upper/lesser
            costheta = np.sqrt(costheta2)
            theta = np.arccos(costheta)
            gsp_angles.append(theta*2)
    print("gsp_len",len(gsp_angles))
    return gsp_angles

def indexed_theta(amps,m,n,index):
    indexed_angles=[]
    for current_index in index:
        temp_start=current_index
        place = current_index/pow(2,n-m)
        increment = int(pow(2,n)/pow(2,m))
        mid =int((place+0.5)*pow(2,n-m))
        end=int((place+1)*pow(2,n-m))
        upper = sum(amps[current_index:mid])
        lesser =sum(amps[current_index:end])
        cos_theta2 = upper/lesser
        cos_theta = np.sqrt(cos_theta2)
        theta = np.arccos(cos_theta)
        indexed_angles.append(theta*2)
    return indexed_angles

def GenerateRC_C_C_angles():
    x_values = np.linspace(-8,8,num=pow(2,5),endpoint=True)
    y_values = Black_Scholes(x_values,45,(45*3))
    values= prob_normalised(y_values)
    angels= gsp_thetas(values,5,5)
    return angels
