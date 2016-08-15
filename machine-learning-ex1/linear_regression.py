import numpy as np


def get_X(df):
    return df.iloc[:, :-1].as_matrix()


def get_y(df):
    '''assume the last column is the target'''
    return np.array(df.iloc[:, -1])


def compute_cost(X, y, theta):
    """
    X: R(m*n), m records, n features
    y: R(m)
    theta : R(n), linear regression parameters
    """
    inner = X @ theta - y  # R(m*1)
    square_sum = inner.transpose() @ inner  # 1*m @ m*1 = 1*1

    cost = square_sum / (2 * (len(X)))

    return cost


def batch_update_theta(X, y, theta, alpha):
    """ return whole batch updated parameters
    n*m @ (m*1 - (m*n @ n*1)) -> n*1
    where n = n features
    """
    inner = X.transpose() @ (X @ theta - y)  # R(n*1)

    new_theta = theta - (alpha / len(X)) * inner  # don't forget the alpha/m, this is n*1

    return new_theta  # return theta vector R(1*n)


def batch_gradient_decent(X, y, theta, alpha, epoch):
    """ return the parameter and cost per batch
    epoch: how many pass to run through whole batch
    """
    cost = [compute_cost(X, y, theta)]

    for i in range(epoch):
        theta = batch_update_theta(X, y, theta, alpha)
        cost.append(compute_cost(X, y, theta))

    return theta, cost


def normalize_feature(df):
    return df.apply(lambda s: (s - s.mean()) / s.std())