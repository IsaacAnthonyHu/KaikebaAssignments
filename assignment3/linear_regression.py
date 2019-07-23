import random
import numpy as np

def predict_y(theta0, theta1, x):

    pred_y = theta1 * x + theta0

    return pred_y


def seperate_xy(data):

    x_list = np.array([coord[0] for coord in data])
    y_list = np.array([coord[1] for coord in data])

    return x_list, y_list


def step_gradient(x_list, y_list, eta, theta0, theta1):

    d_theta0 = (sum(theta1 * x_list) + len(x_list) * theta0 - sum(y_list)) / len(x_list)

    d_theta1 = (sum(theta1 * x_list ** 2) + sum(theta0 * x_list) - sum(x_list * y_list)) / len(x_list)

    return d_theta0, d_theta1

def evaluate_lost(x_list, y_list, theta0, theta1):

    lost = 0

    for x in range(len(x_list)):

        lost += (theta1 * x_list[x] + theta0 - y_list[x])**2

    return lost/(2*len(x_list))



def train(data, eta, max_iter, thres=0.001):

    x_list, y_list = seperate_xy(data)

    num_coord = len(data)

    theta0, theta1 = 0, 0

    lost_history = []

    for i in range(max_iter):

        d_theta0, d_theta1 = step_gradient(x_list, y_list, eta, theta0, theta1)

        theta0 -= eta * d_theta0
        
        theta1 -= eta * d_theta1

        lost = evaluate_lost(x_list, y_list, theta0, theta1)
        
        lost_history.append(lost)

        print('''
        -----
        theta0:  %r
        theta1:  %r
        lost:    %r
        -----
        '''%(theta0, theta1, lost))

        if lost <= thres:
            break

    return theta0, theta1, lost_history

def gen_test_data_set():

    data_points = [(2,3), (-1,1), (3,4), (5,5), (-6,-2)]

    return data_points

def run():

    data = gen_test_data_set()

    theta0, theta1, lost_history = train(data, 0.001, 10000, thres = 0.0011)

    #print(lost_history)

if __name__ == '__main__':
    run()
