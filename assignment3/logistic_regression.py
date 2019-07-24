import numpy as np
import random

def predict_y(theta0, theta1, x):

    pred_y = 1/(1+np.e ** (-theta1 * x - theta0))

    return pred_y

def seperate_xy(data):

    x_list = np.array([coord[0] for coord in data])
    y_list = np.array([coord[1] for coord in data])
    data_length = len(data)

    return x_list, y_list, data_length

def step_gradient(data, theta0, theta1):

    x_list, y_list, data_length = seperate_xy(data)
    d_theta0, d_theta1 = 0,0
    for x in range(data_length):
        d_theta0 += predict_y(theta0, theta1, x_list[x]) - y_list[x]
        d_theta1 += (predict_y(theta0, theta1, x_list[x]) - y_list[x]) * x_list[x]
    d_theta0 /= data_length
    d_theta1 /= data_length

    return d_theta0, d_theta1

def evaluate_lost(data, theta0, theta1):

    x_list, y_list,data_length = seperate_xy(data)
    lost = 0
    for x in range(data_length):
        lost += -(y_list[x] * np.log(predict_y(theta0, theta1, x_list[x])) + (1 - y_list[x]) * np.log(1 - predict_y(theta0, theta1, x_list[x])))

    return lost/data_length

def train(data, eta, max_iter, thres=0.001):

    theta0, theta1 = 0, 0
    lost_history = []
    for i in range(max_iter):
        d_theta0, d_theta1 = step_gradient(data, theta0, theta1)
        theta0 -= eta * d_theta0
        theta1 -= eta * d_theta1
        lost = evaluate_lost(data, theta0, theta1)
        lost_history.append(lost)
        print('''
        -----
        theta0:  %r
        theta1:  %r
        lost:    %r
        -----
        '''%(theta0, theta1, lost))

        if lost <= thres:
            print("Acceptable Lost.")
            break

    return theta0, theta1, lost_history

def gen_test_dataset():

    data_points = [(3,0.9), (2,0.8), (5,0.92), (1,0.6), (-1, 0.5), (-2, 0.75), (-4, 0.9), (-5, 0.95), (-100, 0.99)]

    return data_points

def run():

    data = gen_test_dataset()
    theta0, theta1, lost_history = train(data, 0.01, 10000)

    #print(lost_history[0], lost_history[-1])

if __name__ == '__main__':
    run()
