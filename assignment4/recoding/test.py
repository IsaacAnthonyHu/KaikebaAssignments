import numpy as np
import sklearn.datasets
import sklearn.linear_model

# Generate DataSets
np.random.seed(0) # set same random seed (ensure same random samples)
X, y = sklearn.datasets.make_moons(200, noise=0.2)

num_examples = len(X)  # train size
nn_input_dim = 2  # input dimension
nn_output_dim = 1 # output dimension

lr = 0.01  # learning rate
reg_lambda = 0.01  # ?

def sigmoid(input):

    output = 1 / (1 + np.e ** (-input))

    return output


def build_model(nn_hdim, num_passes=30000, print_loss=False):

    # Can't set all parameter to 0 in Initializing
    weight_1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
    weight_2 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)

    bias_1 = np.zeros((1, nn_hdim))
    bias_2 = np.zeros((1, nn_output_dim))

    model = {}

    # Gradient descent

    for i in range(num_passes):

        z1 = X.dot(weight_1) + bias_1
        a1 = sigmoid(z1)
        z2 = a1.dot(weight_2) + bias_2
        a2 = sigmoid(z2)


